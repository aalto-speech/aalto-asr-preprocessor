"""Configuration file for pytest.

Load long test strings from separate files in the `data/` directory.
"""
from typing import List


pytest_plugins: List[str] = ["tests.fi.data.parl_long_test_strings"]
