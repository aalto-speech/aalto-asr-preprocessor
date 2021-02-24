"""Simple command line client for the package.

The client expects three arguments: input, output, and a recipe file.
Run ``aalto-prep --help`` to see more.
"""
from importlib.abc import Loader
from importlib.util import module_from_spec
from importlib.util import spec_from_file_location
from typing import Any

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
def main(input: Any, output: Any, recipefile: Any, add_linefeed: Any) -> None:
    """Preprocess INPUT to OUTPUT using RECIPEFILE."""
    line_separator = ""
    if add_linefeed:
        line_separator = "\n"

    spec = spec_from_file_location(recipefile, recipefile)
    assert isinstance(spec.loader, Loader)  # for mypy
    recipe = module_from_spec(spec)
    spec.loader.exec_module(recipe)

    texts = input.readlines()
    for text in texts:
        try:
            result = prep.apply(
                text, recipe.REGEXPS, recipe.UNACCEPTED_CHARS, recipe.TRANSLATIONS  # type: ignore
            )
        except AttributeError:
            result = prep.apply(text, recipe.REGEXPS, recipe.UNACCEPTED_CHARS)  # type: ignore
        output.write(result + line_separator)


if __name__ == "__main__":
    main(prog_name="aalto_asr_preprocessor")  # pragma: no cover
