---
layout: default
title: {{ cookiecutter.project_name }}
---

# {{ cookiecutter.project_name }}

[![Github Repo](https://img.shields.io/badge/GitHub-gray?logo=github)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.__github_repo }})

{{ cookiecutter.home_page_text }}

{% raw -%}
{% include cards.html %}
{% endraw -%}
