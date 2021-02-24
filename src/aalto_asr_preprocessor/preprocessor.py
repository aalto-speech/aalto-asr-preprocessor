"""General text preprocessor that uses a regexp recipe to clean a text."""
import re
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple


class UnacceptedCharsError(Exception):
    """A custom error type for preprocessing."""

    pass


def apply(
    text: str,
    regexps: List[Tuple[str, object]],
    unaccepted_chars: str,
    translations: Optional[Dict[str, str]] = None,
) -> str:
    r"""Apply preprocessing recipe to given text.

    Result is validated by checking it for any unaccepted characters. Easiest way to define
    unaccepted characters using regexps is to use a negation of accepted chars. For example:

    ``r"[^a-zåäö \n]"``

    In addition to regexp substitutions, translation mapping is applied to input if defined.

    Args:
        text (str): input string to preprocess
        regexps (list): a preprocessing recipe in the form of regexp-substition pairs
        unaccepted_chars (str): a regexp used to search unaccepted characters
        translations (dict, optional): a translation mapping

    Raises:
        UnacceptedCharsError: raised if preprocessing fails to remove unwanted characters

    Returns:
        str: preprocessed text
    """
    result = text

    for regexp, substitution in regexps:
        result = re.sub(regexp, substitution, result)  # type: ignore  # overload not found

    if translations:
        translation = str.maketrans(translations)
        result = result.translate(translation)

    if match := re.search(unaccepted_chars, result):
        raise UnacceptedCharsError(
            f"Found unaccepted character '{match.group(0)}' in result at index {match.start()}. "
            f"Result:\n{result}"
        )
    return result
