#!/usr/bin/env python3

import os
from pathlib import Path

jekyll_output_dir = Path('_site')
symlink_path = jekyll_output_dir / "{{ cookiecutter.push_target_dir }}"
target_path = "../{{ cookiecutter.push_target_dir }}"
print(f"Creating symlink from {symlink_path} to {target_path}.")
os.makedirs(jekyll_output_dir)
os.symlink(target_path, symlink_path)

REMOVE_PATHS = [
    '{% if cookiecutter.remove_prs_auto != "true" %}.github/workflows/remove_prs.yml{% endif %}',
]
for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path)
        print(f"As remove_prs_auto was set to false, we are removing the associated github action. "
              "Note that we have left scripts/remove_closed_prs.py in project, for manual use.")

git_org = "{{ cookiecutter.github_user }}"
git_name = "{{ cookiecutter.github_repo }}"
asset_path = "{{ cookiecutter.project_slug }}/site/assets"
asset_names = ["images/{{ cookiecutter.light_mode_logo_name }}",
               "images/{{ cookiecutter.dark_mode_logo_name }}",
               "{{ cookiecutter.favicon_name }}"]

next_steps = f"""Website local directory created at {Path('.').resolve().as_posix()}! Next steps:

**SET UP GIT/GITHUB**
1. Initialize the local git repository: `git init`

2. Initialize the remote git repository with name "{git_name}": https://github.com/organizations/{git_org}/repositories/new

3. Follow github's instructions to set the git remote.

**SET UP JEKYLL**
1. Install prerequisites (may not be necessary): https://jekyllrb.com/docs/installation/, then run `gem install jekyll bundler`

2. Run `bundle install`

3. Then, to build and serve, run `bundle exec jekyll serve --watch --livereload`

4. Copy the following files to {asset_path}: {asset_names}

**SET UP JENKINS**
1. See https://github.com/flatironinstitute/neurorse-internal/blob/main/docs/jenkins.md for how to set up Jenkins
"""
print(next_steps)
