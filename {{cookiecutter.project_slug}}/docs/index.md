# {{cookiecutter.project_name}} Documentation

{{cookiecutter.project_short_description}}

## Project layout

    src/
        {{ cookiecutter.project_slug }}/
            __init__.py
            ...
    tests/
        ...
    scripts/
        ...
    notebooks/
        ...
    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Mkdocs Commands

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## License
{% if cookiecutter.open_source_license != "Proprietary" %}
{{ cookiecutter.open_source_license }}: [LICENSE](../LICENSE)
{% else %}
All rights reserved.
{% endif %}
