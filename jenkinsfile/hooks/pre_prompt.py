#!/usr/bin/env python3

to_print = """The following will walk you through the setup of the jenkinsfile and
Dockerfile. Together, these files will build the static site, push it to a different
github repo, and, if built from a pull request, post to Github with the link.

This is intended for use with sphinx, and will need editing before it can work with
another static site generator.

The built site will live at:

{site_url}/{site_baseurl}/{push_target_dir}/{built_site_name}.

Of those, site_baseurl and built_site_name can (and probably should) be empty.

Examples:

1. https://docs.plenoptic.org/docs
  - site_url: "https://docs.plenoptic.org"
  - site_baseurl: ""
  - push_target_dir: "docs"
  - built_site_name: ""

2. https://workshops.plenoptic.org/workshops/CSHL-vision-course-2024/
  - site_url: "https://workshops.plenoptic.org"
  - site_baseurl: ""
  - push_target_dir: "workshops"
  - built_site_name: "CSHL-vision-course-2024"

See https://github.com/plenoptic-org/plenoptic-cshl-vision-2024/tree/main/jenkins for an
example output of this template.

Note that if `built_site_name` is empty, we assume that this will be the *only* source
repo pushing to the corresponding webserver. So, if you are planning on adding other
sources later, put something in that variable.

"""

print(to_print)
