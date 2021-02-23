"""Test the command line client."""
import pytest
from click.testing import CliRunner

from aalto_asr_preprocessor import console


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


def test_fail_without_arguments(runner: CliRunner) -> None:
    result = runner.invoke(console.main)  # type: ignore  # main is not recognized
    assert result.exit_code == 2


def test_help_option(runner: CliRunner) -> None:
    result = runner.invoke(console.main, ["--help"])  # type: ignore  # main is not recognized
    assert result.exit_code == 0


def test_preprocessing_to_stdout(runner: CliRunner) -> None:
    result = runner.invoke(
        console.main,  # type: ignore  # main is not recognized
        ["tests/console_test_input.txt", "-", "tests/minimal_test_recipe.py"],
    )
    assert result.exit_code == 0
    assert result.output == "barbar\nthis test was a success"


def test_add_linefeed_handle(runner: CliRunner) -> None:
    result = runner.invoke(
        console.main,  # type: ignore  # main is not recognized
        [
            "tests/console_test_input.txt",
            "-",
            "tests/minimal_test_recipe.py",
            "--add-linefeed",
        ],
    )
    assert result.exit_code == 0
    assert result.output == "barbar\n\nthis test was a success\n"
