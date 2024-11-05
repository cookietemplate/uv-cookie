import os
import shutil
import subprocess
import json
import requests
from typing import Literal

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

LICENSES_DICT = {
    "Proprietary": None,
    "Apache-2.0": "Apache-2.0",
    "MIT": "MIT",
    "BSD-4-Clause": "BSD-4-Clause",
    "BSD-3-Clause": "BSD-3-Clause",
    "BSD-2-Clause": "BSD-2-Clause",
    "GPL-2.0-only": "GPL-2.0",
    "GPL-2.0-or-later": "GPL-2.0",
    "GPL-3.0-only": "GPL-3.0",
    "GPL-3.0-or-later": "GPL-3.0",
    "LGPL-2.1-only": "LGPL-2.1",
    "LGPL-2.1-or-later": "LGPL-2.1",
    "LGPL-3.0-only": "LGPL-3.0",
    "LGPL-3.0-or-later": "LGPL-3.0",
    "ISC": "ISC",
}


def download_license_from_github(license_name):
    """Download the license file from GitHub"""
    license_name = LICENSES_DICT[license_name]
    if license_name:
        url = "https://api.github.com/licenses/{}".format(license_name)
        response = requests.get(url)
        if response.status_code == 200:
            license_content = json.loads(response.content.decode("utf-8"))["body"]
            return license_content
    return None


def init_uv(
    kind: Literal["app", "lib", "script"] = "lib",
    no_package: bool = False,
    backend: Literal["hatch", "flit", "pdm", "setuptools", "maturin", "scikit"] | None = "hatch",
    author_from: Literal["auto", "git", "none"] = "auto",
    vcs: Literal["git", "none"] = "git",
    name: str | None = None,
    python: str | None = None,
):
    """Initialize the uv project"""
    command = ["uv", "init", PROJECT_DIRECTORY]
    if kind:
        command.append(f"--{kind}")
    if no_package:
        command.append("--no-package")
    if backend:
        command.extend(["--build-backend", backend])
    if author_from:
        command.extend(["--author-from", author_from])
    if vcs:
        command.extend(["--vcs", vcs])
    if name:
        command.extend(["--name", name])
    if python:
        command.extend(["--python", python])

    subprocess.run(command)


def write_license_file(license_name):
    """Write the license file to the project directory"""
    license_content = download_license_from_github(license_name)
    if license_content:
        with open(os.path.join(PROJECT_DIRECTORY, "LICENSE"), "w") as f:
            f.write(license_content)


def init_git_repo():
    """Initialize the git repository"""
    os.system("git init")
    os.system("git add .")
    os.system("git commit -m 'Initial commit'")


def method_pyproject_toml():
    """Method to create pyproject.toml file"""
    tmpl_path = os.path.join(PROJECT_DIRECTORY, "pyproject.tmpl.toml")
    pyproject_path = os.path.join(PROJECT_DIRECTORY, "pyproject.toml")

    # Copy tmpl file to the bottom of pyproject.toml
    with open(tmpl_path, "r") as f:
        tmpl = f.read()

    with open(pyproject_path, "a") as f:
        f.write("\n")
        f.write(tmpl)

    # Remove tmpl file
    os.remove(tmpl_path)


def add_dev_dependencies():
    """Add development dependencies"""
    packages = [
        "pytest",
        "pre-commit",
        "pytest-mock",
        "pytest-cov",
        "commitizen",
        "pyright",
        "isort",
        "mkdocs-material",
        "ruff",
        "nox",
    ]

    command = ["uv", "add", "--dev", *packages]
    subprocess.run(command)


if __name__ == "__main__":
    if "{{ cookiecutter.open_source_license }}" != "Proprietary":
        write_license_file("{{ cookiecutter.open_source_license }}")
    init_uv(
        kind="{{ cookiecutter.kind }}",
        no_package={{ cookiecutter.no_package }},
        backend="{{ cookiecutter.backend }}",
        author_from="{{ cookiecutter.author_from }}",
        vcs="{{ cookiecutter.vcs }}",
        python="{{ cookiecutter.python }}",
    )
    add_dev_dependencies()
    method_pyproject_toml()
    if "{{ cookiecutter.vcs }}" == "git":
        init_git_repo()
