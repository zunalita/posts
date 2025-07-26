import os
import re
from github import Github
from pathlib import Path

import json

# Get the PR number robustly
event_path = os.environ.get('GITHUB_EVENT_PATH')
if not event_path or not os.path.exists(event_path):
    print('::error::GITHUB_EVENT_PATH not found!')
    exit(1)
with open(event_path) as f:
    event = json.load(f)
pr_number = event.get('number') or (event.get('pull_request', {}) or {}).get('number')
if not pr_number:
    print('::error::PR number not found in event payload!')
    exit(1)
repo_name = os.environ.get('GITHUB_REPOSITORY', '')
token = os.environ.get('GITHUB_TOKEN', '')

keywords_path = Path('.github/assets/auto-close-requests-dict.txt')
if not keywords_path.exists():
    print('::error::Keyword dictionary not found!')
    exit(1)

with open(keywords_path) as f:
    keywords = []
    for line in f:
        line = line.strip().lower()
        if not line or line.startswith('#'):
            continue
        keywords.extend([w.strip() for w in line.split(';') if w.strip()])

if not keywords:
    print('::error::No keywords found!')
    exit(1)

# Connect to GitHub
repo = Github(token).get_repo(repo_name)
pr = repo.get_pull(int(pr_number))

# Gather PR content
content = (pr.title or '') + '\n' + (pr.body or '')
for file in pr.get_files():
    try:
        content += '\n' + (file.patch or '')
    except Exception:
        continue

# Count keyword occurrences
found = []
for word in keywords:
    if re.search(r'\b' + re.escape(word) + r'\b', content, re.IGNORECASE):
        found.append(word)

should_close = len(found) > 10

# Set outputs for GitHub Actions
def set_output(name, value):
    print(f"::set-output name={name}::{value}")

set_output('should_close', str(should_close).lower())
if should_close:
    set_output('comment', f"[Beta auto closer]: This pull request was automatically closed because it contains more than 10 forbidden keywords: {', '.join(found)}.\nSome of your content may be used to improve the keyword dictionary. Your request can still be accepted in the future, even if this PR was closed automatically.")
else:
    set_output('comment', '')
