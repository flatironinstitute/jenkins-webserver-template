#!/usr/bin/env python3

import yaml
import os.path as op
from glob import glob
from packaging.version import Version

REDIRECT_HTML="""<head>
  <meta http-equiv="Refresh" content="0; URL={}" />
</head>
"""

# throughout this, we do something like `op.split(variable[:-1])[-1]` to grab the folder
# name. that's because we glob strings that end in /, so we need to drop that before
# using op.split
for site in glob('{{ cookiecutter.push_target_dir }}/*/'):
    md_file = {}
    redirect_url = None
    md_file['base_url'] = site
    with open(op.join(site, '.gh_path')) as f:
        md_file['gh_repo'] = 'https://github.com/' + f.read().strip()
    md_file['name'] = op.split(site[:-1])[-1].replace('-', ' ')
    branches = glob(op.join(site, 'branch', '*/'))
    md_file['branches'] = []
    md_file['main_url'] = ''
    for branch in branches:
        if 'main' in branch:
            md_file['main_url'] = op.join(site, 'branch', 'main')
            if redirect_url is None:
                redirect_url = "branch/main/"
        else:
            md_file['branches'].append(op.split(branch[:-1])[-1])
    md_file['releases'] = sorted([op.split(p[:-1])[-1] for p in glob(op.join(site, 'tags/*/'))],
                                 key=Version)[::-1]
    if redirect_url is None and len(md_file['releases']) > 0:
        redirect_url = f"tags/{md_file['releases'][0]}"
    md_file['pulls'] = sorted([op.split(p[:-1])[-1] for p in glob(op.join(site, 'pulls/*/'))])[::-1]
    if redirect_url is None and len(md_file['pulls']) > 0:
        redirect_url = f"pulls/{md_file['pulls'][0]}"
    if redirect_url is None and len(md_file['branches']) > 0:
        redirect_url = f"branch/{md_file['branches'][0]}"
    with open(f'site/_{{ cookiecutter.push_target_dir }}/{op.split(site[:-1])[-1]}.md', 'w') as f:
        f.write('---\n')
        yaml.safe_dump(md_file, f)
        f.write('---')
    with open(op.join(site, 'index.html'), 'w') as f:
       f.write(REDIRECT_HTML.format(redirect_url))
    if op.exists(op.join(site, 'branch')):
        with open(op.join(site, 'branch', 'index.html'), 'w') as f:
           f.write(REDIRECT_HTML.format('../' + redirect_url))
    if op.exists(op.join(site, 'pulls')):
        with open(op.join(site, 'pulls', 'index.html'), 'w') as f:
           f.write(REDIRECT_HTML.format('../' + redirect_url))
    if op.exists(op.join(site, 'tags')):
        with open(op.join(site, 'tags', 'index.html'), 'w') as f:
           f.write(REDIRECT_HTML.format('../' + redirect_url))
