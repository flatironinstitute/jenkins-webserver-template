---
layout: default
title: {{ cookiecutter.home_page_title }}
---

# {{ cookiecutter.home_page_title }}

[![Github Repo](https://img.shields.io/badge/GitHub-gray?logo=github)](https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.github_repo }})

{{ cookiecutter.home_page_text }}

{% raw -%}
{% include cards.html %}
{% endraw -%}
