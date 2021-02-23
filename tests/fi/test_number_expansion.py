#!/usr/bin/env python3
# coding=utf-8
"""Test number expansion for Finnish."""
import re

import pytest

import aalto_asr_preprocessor.fi.numbers.expansion as num_fi


@pytest.mark.parametrize(
    "str_to_expand, true_result",
    [
        ("0433789#ERI", "nolla neljä kolme kolme seitsemän kahdeksan yhdeksän"),
        ("200#PAR", "kahtasataa"),
        ("13#JNOM", "kolmastoista"),
        ("1300002#NOM", "miljoonakolmesataatuhattakaksi"),
        (
            "50666#TRA",
            "viideksikymmeneksituhanneksikuudeksisadaksikuudeksikymmeneksikuudeksi",
        ),
        ("3002000000011#INE", "kolmessabiljoonassakahdessamiljardissayhdessätoista"),
        ("87410#GEN", "kahdeksankymmenenseitsemäntuhannenneljänsadankymmenen"),
    ],
)
def test_number_expansion(str_to_expand: str, true_result: str) -> None:
    """Test that numbers are correctly expanded into Finnish words."""
    result = re.sub(r"(\d+)#?([A-Z]+)?", num_fi.expand, str_to_expand)
    assert result == true_result
