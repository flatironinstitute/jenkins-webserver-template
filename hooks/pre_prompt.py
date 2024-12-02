#!/usr/bin/env python3

to_print = """The following will walk you through the setup of a "jenkins-webserver".
The directory created should live on github and will be pushed to by Jenkins in order to
host a static site. This repo is intended to have its git history removed periodically;
the source for the built pages should live in some other repository (e.g., the software
package whose documentation you're building), and any changes made to the site
architecture (e.g., the jekyll templates) should also be made in *this* repository.

See https://github.com/plenoptic-org/plenoptic-documentation for an example output of
this template. The provided default values correspond to those used by
plenoptic-documentation, so you can check what they do.

"""
print(to_print)
