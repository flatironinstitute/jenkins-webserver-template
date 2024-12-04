#!/usr/bin/env python3

to_print = """\nCopy the created jenkins directory into your project, {{ cookiecutter.github_user }}/{{ cookiecutter.github_source_repo }}

Then go to
https://github.com/flatironinstitute/neurorse-internal/blob/main/docs/jenkins.md to see
how to configure Jenkins and Github Pages.

If you already have a Jenkinsfile (e.g., to run tests using the GPU), you should just
take the stage('docs') section of the generated Jenkinsfile, and add that to your
existing one, after your existing stage sections. You may additionally want to:

1. Use the Jenkins parallel section (https://www.jenkins.io/doc/book/pipeline/syntax/#parallel)

2. Add a when block, if your existing Jenkinsfile has additional triggers.

For both, see plenoptic's Jenkinsfile for an example
(https://github.com/plenoptic-org/plenoptic-cshl-vision-2024/tree/main/jenkins/Jenkinsfile)

"""
print(to_print)
