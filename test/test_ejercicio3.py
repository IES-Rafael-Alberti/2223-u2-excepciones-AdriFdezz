import pytest
from src.ejercicio3 import cuenta_atras

def test_cuenta_atras():
    with pytest.raises(ValueError):
        cuenta_atras(-5)