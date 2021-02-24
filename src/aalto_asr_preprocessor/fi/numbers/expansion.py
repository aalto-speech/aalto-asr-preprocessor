"""Number expansion for Finnish.

This package is used to convert numbers to written Finnish
form with the desired inflectional form.

Inflection mapping is defined in the module init.
"""
import re
from typing import Match

from aalto_asr_preprocessor.fi.numbers import INFLECTIONS
from aalto_asr_preprocessor.fi.numbers import UNITS


def to_nominal(match: Match[str]) -> str:
    """Regexp replacing function for expanding a string of single digits.

    Args:
        match (Match): captured digit

    Returns:
        str: word corresponding to the digit
    """
    digit = match.group(0)
    return INFLECTIONS["NOM"][digit] + " "


def inflect(match: Match[str]) -> str:
    """Regexp replacing function for inflecting a digit in correct inflectional form.

    Args:
        match (Match): captured digit and inflectional form (e.g. ('8','TRA'))

    Returns:
        str: word corresponding to the digit in correct case (e.g. 'kahdeksaksi')
    """
    digit = match.group(1)
    form = match.group(2)
    return INFLECTIONS[form][digit]


def encode_base_ten(digits: str) -> str:
    """Encode bases of ten in a number string for expansion.

    Args:
        digits (str): a number to encode (e.g. 87410)

    Returns:
        str: number encoded with bases of ten (e.g. 8k7yt 4s1k0y)
    """
    encoding = ""
    for i, d in zip(reversed(range(len(digits))), digits):
        encoding += f"{d}{UNITS[i%3]}"
        if i > 2 and i % 3 == 0:
            encoding += f"{UNITS[i]} "
    return encoding


def expand(match: Match[str]) -> str:
    """Expand a number string in Finnish text to equivalent word representation.

    Args:
        match (Match): captured number and optionally its inflectional form: 100#PAR

    Returns:
        str: the matched number(s) expanded as words
    """
    digits = match.group(1)
    form = match.group(2)
    if not form:
        form = "NOM"

    if form == "ERI" or digits.startswith("0") or len(digits) > 13:
        return str(re.sub(r"[0-9]", to_nominal, digits).strip())

    result = encode_base_ten(digits)

    # Convert teens
    result = re.sub(r"1k(\d)y", r"\1o", result)
    result = re.sub(r"0o", r"1k", result)
    # Remove redundant zeros and ones
    result = re.sub(r"0[a-z]\s*", r"", result)
    result = re.sub(r"y", r"", result)
    result = re.sub(r"\s[a-z]", r"", result)
    result = re.sub(r"1([kstmrb])", r"\1", result)
    # Add inflectional forms
    result = re.sub(r"(\S)", r"\1" + form, result)
    result = re.sub(r"(?<=NOM|PAR)([kstmrb])NOM", r"\1PAR", result)
    # Fix ordinals "ensimmäinen" and "toinen"
    result = re.sub(r"1(J[A-Z]+)$", r"!\1", result)
    result = re.sub(r"2(J[A-Z]+)$", r'"\1', result)

    # Inflect encoded string
    result = re.sub(r'([0-9a-z!"]{1})([A-Z]{3,4})', inflect, result)

    return result.replace(" ", "")
