"""A helper script for installing dependencies from pyproject.toml.

This is intended to be used with the Dockerfile so dependencies can be cached
separately from the source code installation.
"""
import subprocess
import sys
import tomllib

with open("pyproject.toml", "rb") as f:
    pyproject = tomllib.load(f)

dependencies = pyproject["project"]["dependencies"]
subprocess.check_call([sys.executable, "-m", "pip", "install"] + dependencies)
