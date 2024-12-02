# jenkins-webserver-template

Template repo to serve as recipient of jenkins documentation build pushes, using [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/index.html).

To use:

```sh
pipx install cookiecutter
cookiecutter gh:flatironinstitute/jenkins-webserver-template
```

And answer the prompts. After completion, next steps will be printed to stdout --- pay attention to them!

There are two templates this will help you generate, the `webserver` and the `jenkinsfile` (running the above command will prompt you as to which you want):
- `webserver` sets up the host for the static site, and should only need to be run once
- `jenkinsfile` sets up the files to be copied to the *source* for the static site, and so will need to be run each time you add a source (for documentation, this is probably only once; for workshops, it may be multiple times).

In either case, you'll also want to see the [jenkins notes](https://github.com/flatironinstitute/neurorse-internal/blob/main/docs/jenkins.md) for how to configure Jenkins to work with this setup.
