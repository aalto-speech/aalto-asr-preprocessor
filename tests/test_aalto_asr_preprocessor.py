"""Tests for the Aalto ASR preprocessor package."""
from aalto_asr_preprocessor import __version__


def test_version() -> None:
    """Check version is correct."""
    assert __version__ == "0.1.0"
