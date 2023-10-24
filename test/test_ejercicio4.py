import pytest
from src.ejercicio4 import numero_entero

def test_numero_entero():
    with pytest.raises(ValueError):
        numero_entero(5.5)