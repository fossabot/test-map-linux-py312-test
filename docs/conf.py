# SPDX-FileCopyrightText: © 2024 Romain Brault <mail@romainbrault.com>
#
# SPDX-License-Identifier: MIT OR Apache-2.0

"""Sphinx configuration."""

# pylint: disable=invalid-name,redefined-builtin

from importlib import metadata


project = "test map linux py312-test"
author = "Romain Brault"
copyright = "2024, Romain Brault. "
language = "en"
myst_heading_anchors = 3
extensions = [
    "autoapi.extension",
    "myst_parser",
    "sphinx_click",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]
autoapi_type = "python"
autoapi_dirs = ["../src"]
autodoc_typehints = "description"
html_theme = "furo"
html_favicon = "images/logo.svg"
html_logo = "images/logo.svg"
html_extra_path = ["images/"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "pip": ("https://pip.pypa.io/en/stable", None),
    "tox": ("https://tox.wiki/en/stable/", None),
}
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

release = metadata.version("test_map_linux_py312_test")
version = ".".join(release.split(".")[:3])
