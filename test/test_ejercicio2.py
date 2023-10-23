import pytest
from src.ejercicio2 import numeros_impares

def test_numeros_impares():
    with pytest.raises(ValueError):
        numeros_impares(-32)