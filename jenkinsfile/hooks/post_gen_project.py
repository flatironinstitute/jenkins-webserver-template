#!/usr/bin/env python3

to_print = """\nCopy the created jenkins directory into your project,
{{ cookiecutter.github_user }}/{{ cookiecutter.github_source_repo }}

Then go to
https://github.com/flatironinstitute/neurorse-internal/blob/main/docs/jenkins.md to see
how to configure Jenkins and Github Pages."""
print(to_print)
