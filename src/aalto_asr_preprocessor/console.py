"""Simple command line client for the package."""

import importlib

import click

import aalto_asr_preprocessor.preprocessor as prep

from . import __version__


@click.command()
@click.argument("input", type=click.File())
@click.argument("output", type=click.File(mode="w"))
@click.argument("recipe", type=click.Path(exists=True))
@click.option(
    "--keep-lines",
    is_flag=True,
    help="Keep each input line on its own output line, otherwise output is a single line.",
)
@click.version_option(version=__version__)
def main(input, output, recipe, keep_lines):
    """Preprocess INPUT to OUTPUT using RECIPE."""
    line_separator = ""
    if keep_lines:
        line_separator = "\n"

    spec = importlib.util.spec_from_file_location("recipe", recipe)
    recipe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(recipe)

    texts = input.readlines()
    for text in texts:
        result = prep.apply(text, recipe.REGEXPS, recipe.UNACCEPTED_CHARS, recipe.TRANSLATIONS)
        output.write(result + line_separator)
