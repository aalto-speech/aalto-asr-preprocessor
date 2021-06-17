"""Test the command line client."""
import pytest
from click.testing import CliRunner

from aalto_asr_preprocessor import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Initialize a command line client."""
    return CliRunner()


def test_fail_without_arguments(runner: CliRunner) -> None:
    """It exits if no arguments or options are given."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 2


def test_fail_with_bad_recipe_file(runner: CliRunner) -> None:
    """It exits if recipe file is not a python file."""
    result = runner.invoke(
        __main__.main, ["tests/console_test_input.txt", "-", "tests/console_test_input.txt"]
    )
    assert result.exit_code == 1


def test_help_option(runner: CliRunner) -> None:
    """It exits with status code 0 if help option is passed."""
    result = runner.invoke(__main__.main, ["--help"])
    assert result.exit_code == 0


def test_preprocessing_to_stdout(runner: CliRunner) -> None:
    """It exits with status code 0 and processes the given input to stdout."""
    result = runner.invoke(
        __main__.main,
        ["tests/console_test_input.txt", "-", "tests/minimal_test_recipe.py"],
    )
    assert result.exit_code == 0
    assert result.output == "barbar\nthis test was a success\n"


def test_add_linefeed_handle(runner: CliRunner) -> None:
    """It outputs additional linefeeds with --add-linefeed handle."""
    result = runner.invoke(
        __main__.main,
        [
            "tests/console_test_input.txt",
            "-",
            "tests/minimal_test_recipe.py",
            "--add-linefeed",
        ],
    )
    assert result.exit_code == 0
    assert result.output == "barbar\n\nthis test was a success\n\n"
