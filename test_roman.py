import pytest

from roman import convert_to_roman_symbol

def test_convert_X():
    assert convert_to_roman_symbol('X') == 10

def test_convert_IX():
    assert convert_to_roman_symbol('IX') == 9

def test_convert_XI():
    assert convert_to_roman_symbol('XI') == 11

def test_convert_IXX():
    assert convert_to_roman_symbol('IXX') == 19

def test_convert_XXI():
    assert convert_to_roman_symbol('XXI') == 21

def test_unknown_symbol():
    with pytest.raises(ValueError):
        convert_to_roman_symbol('unknown')

def test_empty_parameter():
    with pytest.raises(TypeError):
        convert_to_roman_symbol()