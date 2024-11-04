# {{cookiecutter.project_name}} Documentation

{{cookiecutter.project_short_description}}

## Project layout

    .github/
        workflows/
            ...
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
    notebooks/
        ...
    scripts/
        ...
    src/
        {{ cookiecutter.project_slug }}/
            __init__.py
            ...
    tests/
        ...
    .editorconfig   # The configuration file.
    .pre-commit-config.yaml  # The configuration file.
    .gitignore      # The configuration file.
    mkdocs.yml      # The configuration file.
    pyproject.toml  # The configuration file.
    README.md       # The documentation homepage.

## License
{% if cookiecutter.open_source_license != "Proprietary" %}
{{ cookiecutter.open_source_license }}: [LICENSE](./LICENSE)
{% else %}
All rights reserved.
{% endif %}
