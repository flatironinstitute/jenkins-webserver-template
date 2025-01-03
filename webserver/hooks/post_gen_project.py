#!/usr/bin/env python3

import os
from pathlib import Path
import subprocess

jekyll_output_dir = Path('_site')
symlink_path = jekyll_output_dir / "{{ cookiecutter.push_target_dir }}"
target_path = "../{{ cookiecutter.push_target_dir }}"
os.makedirs(jekyll_output_dir)
os.symlink(target_path, symlink_path)

subprocess.run("git init", shell=True)
subprocess.run("git remote add origin https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.__github_repo }}",
               shell=True)
subprocess.run("git add -f .", shell=True)
subprocess.run("git commit -m 'Adds template-generated files'", shell=True)

print(f"\nCreating symlink from {symlink_path} to {target_path}.")

REMOVE_PATHS = [
    '{% if cookiecutter.remove_prs_auto != true %}.github/workflows/remove_prs.yml{% endif %}',
]
for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        os.unlink(path)
        print(f"\nAs remove_prs_auto was set to false, we are removing the associated github action. "
              "Note that we have left scripts/remove_closed_prs.py in project, for manual use.")

# make them actual newlines
for file in ["site/index.md"]:
    with open(file) as f:
        txt = f.read()
    with open(file, 'w') as f:
        f.write(txt.replace("\\n", "\n"))

git_org = "{{ cookiecutter.github_user }}"
git_name = "{{ cookiecutter.__github_repo }}"
asset_path = "{{ cookiecutter.__project_slug }}/site/assets"
asset_names = [
    '{% if cookiecutter.light_mode_logo_name != "03-FI-primary-logo-white.png" %}images/{{ cookiecutter.light_mode_logo_name }}{% endif %}',
    '{% if cookiecutter.dark_mode_logo_name != "01-FI-primary-logo-color.png" %}images/{{ cookiecutter.dark_mode_logo_name }}{% endif %}',
    '{% if cookiecutter.favicon_name != "ccn_small.png" %}{{ cookiecutter.favicon_name }}{% endif %}',
]

next_steps = f"""\nWebsite local directory created at {Path('.').resolve().as_posix()}! Next steps:

**SET UP GIT/GITHUB**
1. Initialize the remote git repository with name "{git_name}": https://github.com/organizations/{git_org}/repositories/new

2. The local git repo has already been initialized, made its first commit, and had the origin remote added -- check that you can push/pull!

**SET UP JEKYLL**
1. Install prerequisites (run once per machine): https://jekyllrb.com/docs/installation/, then run `gem install jekyll bundler`

2. Run `bundle install`

3. Then, to build and serve, run `bundle exec jekyll serve --watch --livereload`

4. Copy the following files to {asset_path}: {asset_names}

**SET UP JENKINS AND GITHUB PAGES**
1. Run this cookiecutter again to generate the jenkins/ directory to place in your source directory.

2. See https://github.com/flatironinstitute/neurorse-internal/blob/main/docs/jenkins.md for how to set up Jenkins to build the site, and GitHub Pages to host it.

If you have any issues with this, ask Billy!
"""
print(next_steps)
