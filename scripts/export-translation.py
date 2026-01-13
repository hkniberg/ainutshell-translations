#!/usr/bin/env python3
"""
Export a translation from ainutshell-translations to ainutshell repo.

This is the main publishing script. Use this after a translator submits
improvements to push the translation to the appropriate preview branch.

See also: import-translation.py (for the reverse direction)

This script:
1. Checks out the preview-<lang> branch in the ainutshell repo
2. Copies manuscript from this repo
3. Updates the LEANPUB_METADATA.* files from metadata-<lang>.md
4. Handles translated images if they exist (renames and updates references)

Usage:
    python scripts/export-translation.py <language-code>
    
Example:
    python scripts/export-translation.py da
"""

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path


def run_cmd(cmd, cwd=None, check=True):
    """Run a shell command and return output."""
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=check)
    return result.stdout.strip()


def has_uncommitted_changes(repo_path):
    """Check if repo has uncommitted changes."""
    status = run_cmd(["git", "status", "--porcelain"], cwd=repo_path)
    return bool(status)


def get_current_branch(repo_path):
    """Get current git branch."""
    return run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=repo_path)


def parse_metadata(metadata_path):
    """Parse metadata.md and return a dict of section name -> content."""
    with open(metadata_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    sections = {}
    current_section = None
    current_content = []
    
    for line in content.split('\n'):
        if line.startswith('# '):
            # Save previous section
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            # Start new section
            current_section = line[2:].strip().lower().replace(' ', '_')
            current_content = []
        else:
            current_content.append(line)
    
    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return sections


def update_leanpub_metadata(manuscript_dir, metadata_sections):
    """Update LEANPUB_METADATA files from parsed metadata sections."""
    # Mapping from metadata section names to LEANPUB_METADATA file names
    section_to_file = {
        'title': 'LEANPUB_METADATA.title',
        'subtitle': 'LEANPUB_METADATA.subtitle',
        'tagline': 'LEANPUB_METADATA.tagline',
        'about_the_book': 'LEANPUB_METADATA.about_the_book',
        'meta_description': 'LEANPUB_METADATA.meta_description',
        # author_blurb has a variable suffix, handled separately
    }
    
    updated_count = 0
    
    for section_name, filename in section_to_file.items():
        if section_name in metadata_sections:
            filepath = manuscript_dir / filename
            if filepath.exists():
                # LEANPUB_METADATA files have a leading newline
                new_content = f"\n{metadata_sections[section_name]}\n"
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"  Updated {filename}")
                updated_count += 1
    
    # Handle author_blurb separately (has variable suffix like .95667)
    if 'author_blurb' in metadata_sections:
        for filepath in manuscript_dir.glob('LEANPUB_METADATA.author_blurb*'):
            new_content = f"\n{metadata_sections['author_blurb']}\n"
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  Updated {filepath.name}")
            updated_count += 1
    
    return updated_count


def main():
    parser = argparse.ArgumentParser(description="Export translation to ainutshell repo")
    parser.add_argument("lang", help="Language code (e.g., 'da' for Danish)")
    args = parser.parse_args()
    
    lang = args.lang
    
    # Determine repo paths (assume sibling directories)
    script_dir = Path(__file__).resolve().parent
    translations_repo = script_dir.parent
    ainutshell_repo = translations_repo.parent / "ainutshell"
    
    print(f"translations repo: {translations_repo}")
    print(f"ainutshell repo: {ainutshell_repo}")
    print()
    
    # Validate repos exist
    if not (translations_repo / ".git").exists():
        print(f"Error: {translations_repo} is not a git repository")
        sys.exit(1)
    
    if not ainutshell_repo.exists():
        print(f"Error: ainutshell repo not found at {ainutshell_repo}")
        sys.exit(1)
    
    if not (ainutshell_repo / ".git").exists():
        print(f"Error: {ainutshell_repo} is not a git repository")
        sys.exit(1)
    
    # Validate translation files exist
    manuscript_src = translations_repo / "manuscript" / f"manuscript-{lang}.md"
    metadata_src = translations_repo / "metadata" / f"metadata-{lang}.md"
    resources_src = translations_repo / "manuscript" / f"resources-{lang}"
    
    if not manuscript_src.exists():
        print(f"Error: Manuscript not found: {manuscript_src}")
        sys.exit(1)
    
    if not metadata_src.exists():
        print(f"Error: Metadata not found: {metadata_src}")
        sys.exit(1)
    
    # Check for uncommitted changes in ainutshell
    if has_uncommitted_changes(ainutshell_repo):
        print("Error: ainutshell repo has uncommitted changes. Please commit or stash them first.")
        sys.exit(1)
    
    # Remember current branch to return to it if something fails
    original_branch = get_current_branch(ainutshell_repo)
    preview_branch = f"preview-{lang}"
    
    print(f"Exporting {lang} translation...")
    print()
    
    try:
        # Pull latest translations (this repo)
        print("Pulling latest from ainutshell-translations...")
        run_cmd(["git", "pull"], cwd=translations_repo)
        
        # Checkout preview branch in ainutshell
        print(f"Checking out {preview_branch} in ainutshell...")
        run_cmd(["git", "checkout", preview_branch], cwd=ainutshell_repo)
        run_cmd(["git", "pull"], cwd=ainutshell_repo)
        
        # Copy manuscript
        manuscript_dst = ainutshell_repo / "manuscript" / "manuscript.md"
        print(f"Copying manuscript...")
        shutil.copy2(manuscript_src, manuscript_dst)
        
        # Update LEANPUB_METADATA files (metadata.md in ainutshell is not used by Leanpub)
        print("Updating LEANPUB_METADATA files...")
        metadata_sections = parse_metadata(metadata_src)
        manuscript_dir = ainutshell_repo / "manuscript"
        updated_count = update_leanpub_metadata(manuscript_dir, metadata_sections)
        if updated_count == 0:
            print("  No LEANPUB_METADATA files found to update")
        
        # Handle translated images if they exist
        if resources_src.exists() and resources_src.is_dir():
            print(f"Processing translated images from {resources_src.name}...")
            resources_dst = ainutshell_repo / "manuscript" / "resources"
            
            # Build a mapping of old filename -> new filename for manuscript updates
            image_renames = {}  # old_name -> new_name
            image_count = 0
            
            for image_file in resources_src.iterdir():
                if image_file.is_file():
                    old_name = image_file.name
                    stem = image_file.stem  # filename without extension
                    ext = image_file.suffix  # .png, .jpg, etc.
                    
                    # Remove -<lang> suffix if present
                    # Supports both: "020-roles-da.jpg" and "020-roles.jpg"
                    lang_suffix = f"-{lang}"
                    if stem.endswith(lang_suffix):
                        new_stem = stem[:-len(lang_suffix)]
                        new_name = f"{new_stem}{ext}"
                    else:
                        # No language suffix - use filename as-is
                        new_name = old_name
                    
                    dst_path = resources_dst / new_name
                    shutil.copy2(image_file, dst_path)
                    
                    if old_name != new_name:
                        print(f"  {old_name} -> {new_name}")
                    else:
                        print(f"  {old_name}")
                    
                    image_renames[old_name] = new_name
                    image_count += 1
            
            print(f"Copied {image_count} translated images")
            
            # Update image references in manuscript
            print("Updating image references in manuscript...")
            with open(manuscript_dst, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Replace all references from resources-<lang>/ to resources/
            # This handles both naming conventions:
            #   (resources-da/020-roles-da.jpg) -> (resources/020-roles.jpg)
            #   (resources-da/020-roles.jpg) -> (resources/020-roles.jpg)
            new_content = content
            
            for old_name, new_name in image_renames.items():
                old_ref = f"resources-{lang}/{old_name}"
                new_ref = f"resources/{new_name}"
                if old_ref in new_content:
                    new_content = new_content.replace(old_ref, new_ref)
            
            # Also handle any remaining resources-<lang>/ references not in our rename map
            # (in case manuscript references images that weren't in the translated folder)
            pattern = rf'resources-{lang}/'
            remaining_matches = len(re.findall(pattern, new_content))
            if remaining_matches > 0:
                print(f"  Warning: {remaining_matches} references to resources-{lang}/ not matched to translated images")
            
            if new_content != content:
                with open(manuscript_dst, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated image references")
            else:
                print("No image references needed updating")
        else:
            print(f"No translated images folder found (checked for {resources_src.name})")
        
        print()
        print("=" * 60)
        print("Export complete!")
        print("=" * 60)
        print()
        
        # Show git status
        print("Changes made in ainutshell repo:")
        status = run_cmd(["git", "status", "--short"], cwd=ainutshell_repo)
        print(status)
        print()
        
        # Show next steps
        commit_msg = f"Import {lang} translation from ainutshell-translations"
        print("Next steps:")
        print(f"  cd {ainutshell_repo}")
        print(f"  git add .")
        print(f"  git commit -m \"{commit_msg}\"")
        print(f"  git push origin {preview_branch}")
        
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        
        # Try to return to original branch
        try:
            run_cmd(["git", "checkout", original_branch], cwd=ainutshell_repo, check=False)
        except:
            pass
        
        sys.exit(1)


if __name__ == "__main__":
    main()
