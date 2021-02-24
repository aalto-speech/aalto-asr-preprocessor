# type: ignore
"""Simple command line client for the package.

The client expects three arguments: input, output, and a recipe file.
Run ``aalto-prep --help`` to see more.
"""
import importlib

import click

import aalto_asr_preprocessor.preprocessor as prep


@click.command()
@click.argument("input", type=click.File())
@click.argument("output", type=click.File(mode="w"))
@click.argument("recipefile", type=click.Path(exists=True))
@click.option(
    "--add-linefeed",
    is_flag=True,
    help="Add line feeds to keep your input lines separated.",
)
@click.version_option()
def main(input, output, recipefile, add_linefeed):
    """Preprocess INPUT to OUTPUT using RECIPEFILE."""
    line_separator = ""
    if add_linefeed:
        line_separator = "\n"

    spec = importlib.util.spec_from_file_location("recipe", recipefile)
    recipe = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(recipe)

    texts = input.readlines()
    for text in texts:
        try:
            result = prep.apply(
                text, recipe.REGEXPS, recipe.UNACCEPTED_CHARS, recipe.TRANSLATIONS
            )
        except AttributeError:
            result = prep.apply(text, recipe.REGEXPS, recipe.UNACCEPTED_CHARS)
        output.write(result + line_separator)
