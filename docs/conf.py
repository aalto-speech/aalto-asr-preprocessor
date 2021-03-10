"""Sphinx configuration."""
from datetime import datetime


project = "Aalto ASR preprocessor"
author = "Anja Virkkunen"
copyright = f"{datetime.now().year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
