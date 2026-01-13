#!/usr/bin/env python3
"""
Import a translation from ainutshell repo to ainutshell-translations.

This is the REVERSE of export-translation.py. Use this to pull changes
from someone who edited directly on a preview branch in ainutshell,
or to initially populate this repo from ainutshell branches.

This script:
1. Finds preview-<lang> branches in the ainutshell repo
2. Copies manuscript.md to manuscript-<lang>.md
3. Combines LEANPUB_METADATA.* files into metadata-<lang>.md

Usage:
    python scripts/import-translation.py [language-code]
    
Examples:
    python scripts/import-translation.py da    # Import Danish only
    python scripts/import-translation.py       # Import all languages
"""

import os
import subprocess
import shutil
import re
import sys
import argparse

def run_command(command, cwd=None):
    """Run a shell command and return the output."""
    result = subprocess.run(
        command,
        shell=True,
        check=True,
        text=True,
        capture_output=True,
        cwd=cwd
    )
    return result.stdout.strip()

def read_file_content(file_path):
    """Read and return the content of a file if it exists."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    return ""

def create_metadata_file(source_repo, lang_code, target_file):
    """Create a combined metadata file from individual metadata files."""
    # Define the source files in the manuscript folder
    manuscript_dir = os.path.join(source_repo, "manuscript")
    
    # Find the metadata files in the manuscript directory
    title_file = os.path.join(manuscript_dir, "LEANPUB_METADATA.title")
    subtitle_file = os.path.join(manuscript_dir, "LEANPUB_METADATA.subtitle")
    tagline_file = os.path.join(manuscript_dir, "LEANPUB_METADATA.tagline")
    about_book_file = os.path.join(manuscript_dir, "LEANPUB_METADATA.about_the_book")
    meta_description_file = os.path.join(manuscript_dir, "LEANPUB_METADATA.meta_description")
    
    # For author_blurb, we need to handle the numeric suffix
    author_blurb_file = None
    for file in os.listdir(manuscript_dir):
        if file.startswith("LEANPUB_METADATA.author_blurb"):
            author_blurb_file = os.path.join(manuscript_dir, file)
            break
    
    # Read content from each file
    title_content = read_file_content(title_file)
    subtitle_content = read_file_content(subtitle_file)
    tagline_content = read_file_content(tagline_file)
    about_book_content = read_file_content(about_book_file)
    meta_description_content = read_file_content(meta_description_file)
    author_blurb_content = read_file_content(author_blurb_file) if author_blurb_file else ""
    
    # Create the combined metadata content
    combined_content = f"""# Title

{title_content}

# Subtitle

{subtitle_content}

# Tagline

{tagline_content}

# About the book

{about_book_content}

# Author blurb

{author_blurb_content}

# Meta description

{meta_description_content}

# Translator credits

This translation was originally done by AI, and then reviewed and improved by <insert your name here>.
"""
    
    # Write the combined content to the target file
    with open(target_file, 'w', encoding='utf-8') as file:
        file.write(combined_content)
    
    print(f"Created combined metadata file: {target_file}")

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Copy translations from ainutshell repository.')
    parser.add_argument('lang_code', nargs='?', help='Language code to copy (e.g., "sv" or "zh-Hant"). If not provided, all languages will be copied.')
    args = parser.parse_args()
    
    # Source repository path
    source_repo = "../ainutshell"
    
    # Target repository path (current repository)
    target_repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"Source repository: {source_repo}")
    print(f"Target repository: {target_repo}")
    
    # Ensure metadata directory exists
    metadata_dir = os.path.join(target_repo, "metadata")
    if not os.path.exists(metadata_dir):
        os.makedirs(metadata_dir)
        print(f"Created metadata directory: {metadata_dir}")
    
    # Store the current branch in the source repository to restore it later
    original_branch = run_command("git branch --show-current", cwd=source_repo)
    print(f"Original branch in source repository: {original_branch}")
    
    try:
        # Fetch all remote branches to ensure we have the latest information
        print("Fetching all remote branches...")
        run_command("git fetch --all", cwd=source_repo)
        
        # Get all branches in the source repository (including remote branches)
        branches_output = run_command("git branch -a", cwd=source_repo)
        branches = [branch.strip() for branch in branches_output.split('\n')]
        
        # Find branches matching the pattern preview-xx or preview-xx-Xxxx
        preview_branches = []
        for branch in branches:
            # Remove the asterisk and leading/trailing whitespace that marks the current branch
            clean_branch = branch.replace('*', '').strip()
            
            # Handle remote branches by removing the 'remotes/origin/' prefix if present
            if clean_branch.startswith('remotes/origin/'):
                clean_branch = clean_branch[len('remotes/origin/'):]
            
            # Match both simple (preview-xx) and extended (preview-xx-Xxxx) language codes
            match = re.match(r'preview-([a-z]{2}(?:-[A-Za-z]+)?)$', clean_branch)
            if match:
                lang_code = match.group(1)
                preview_branches.append((clean_branch, lang_code))
        
        # Remove duplicates (local and remote branches with the same name)
        unique_preview_branches = []
        seen_lang_codes = set()
        for branch, lang_code in preview_branches:
            if lang_code not in seen_lang_codes:
                unique_preview_branches.append((branch, lang_code))
                seen_lang_codes.add(lang_code)
        
        preview_branches = unique_preview_branches
        print(f"Found preview branches: {preview_branches}")
        
        # Check if the requested language exists
        if args.lang_code:
            available_langs = [lang for _, lang in preview_branches]
            if args.lang_code not in available_langs:
                print(f"Error: Language code '{args.lang_code}' not found in available branches.")
                print(f"Available language codes: {', '.join(sorted(available_langs))}")
                return 1
        
        # Track if any branches were processed
        processed_count = 0
        
        # Process branches based on command line argument
        for branch, lang_code in preview_branches:
            # If a specific language code was provided, only process that one
            if args.lang_code and lang_code != args.lang_code:
                continue
                
            processed_count += 1
            print(f"Processing branch: {branch} for language: {lang_code}")
            
            # Checkout the branch
            try:
                # Try to checkout the branch directly
                run_command(f"git checkout {branch}", cwd=source_repo)
            except subprocess.CalledProcessError:
                # If that fails, try to checkout the remote branch
                print(f"Local branch not found, trying to checkout from remote: origin/{branch}")
                run_command(f"git checkout -b {branch} origin/{branch}", cwd=source_repo)
            
            print(f"Checked out branch: {branch}")
            
            # Copy manuscript file
            source_manuscript = os.path.join(source_repo, "manuscript", "manuscript.md")
            target_manuscript = os.path.join(target_repo, "manuscript", f"manuscript-{lang_code}.md")
            
            # Check if source file exists
            if os.path.exists(source_manuscript):
                # Copy the file
                shutil.copy2(source_manuscript, target_manuscript)
                print(f"Copied {source_manuscript} to {target_manuscript}")
            else:
                print(f"Source file {source_manuscript} does not exist!")
            
            # Create combined metadata file
            target_metadata = os.path.join(target_repo, "metadata", f"metadata-{lang_code}.md")
            create_metadata_file(source_repo, lang_code, target_metadata)
        
        # If no branches were processed and no specific language was requested, show a message
        if processed_count == 0 and not args.lang_code:
            print("No preview branches found to process.")
    
    finally:
        # Restore the original branch in the source repository
        run_command(f"git checkout {original_branch}", cwd=source_repo)
        print(f"Restored original branch: {original_branch}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 