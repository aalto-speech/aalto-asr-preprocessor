"""Sphinx configuration."""
from datetime import datetime


project = "Aalto ASR preprocessor"
author = "Anja Virkkunen"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
]
autodoc_typehints = "description"
html_theme = "furo"
