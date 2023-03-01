"""A command-line tool for installing dependencies from pyproject.toml using pip.

This is intended to be used with the Dockerfile so dependencies can be cached
separately from the source code installation.
"""
import argparse
import subprocess
import sys
import tomllib
from typing import Iterable, TypedDict, cast


# NOTE: type-hinting purposes
class PyProject(TypedDict):
    project: "ProjectTable"


ProjectTable = TypedDict(
    "ProjectTable",
    {
        "dependencies": list[str],
        "optional-dependencies": dict[str, list[str]],
    },
)


def read_pyproject() -> PyProject:
    # For simplicitly, we'll use cast() and skip validating the structure
    # (Pydantic would be nice here, but that's an external dependency)
    with open("pyproject.toml", "rb") as f:
        return cast(PyProject, tomllib.load(f))


def get_required_dependencies(pyproject: PyProject) -> list[str]:
    return pyproject["project"]["dependencies"]


def get_optional_dependencies(pyproject: PyProject, extras: Iterable[str]) -> list[str]:
    extras = set(extras)

    selected_dependencies = []
    for name, dependencies in pyproject["project"]["optional-dependencies"].items():
        if name not in extras:
            continue

        selected_dependencies.extend(dependencies)
        extras.remove(name)

    if extras:
        raise ValueError(
            f"Could not match any of the following extras: {sorted(extras)}"
        )

    return selected_dependencies


def main():
    parser = argparse.ArgumentParser(
        prog="install_dependencies",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__doc__,
    )
    parser.add_argument(
        "--dry-run",
        help="If set, dependencies are listed instead of being installed.",
        action="store_true",
    )
    parser.add_argument(
        "--extras",
        help="A list of optional dependencies to install.",
        default=(),
        nargs="*",
    )
    parser.add_argument(
        "--no-required",
        help="If set, required dependencies will not be installed.",
        action="store_false",
        dest="required",
    )

    args = parser.parse_args()
    pyproject = read_pyproject()

    dependencies = []

    if args.required:
        dependencies.extend(get_required_dependencies(pyproject))

    if args.extras:
        dependencies.extend(get_optional_dependencies(pyproject, args.extras))

    if args.dry_run:
        return print(dependencies)

    subprocess.check_call(
        [sys.executable, "-m", "pip", "install"]
        + get_required_dependencies(pyproject)
        + get_optional_dependencies(pyproject, args.extras)
    )


if __name__ == "__main__":
    sys.exit(main())
