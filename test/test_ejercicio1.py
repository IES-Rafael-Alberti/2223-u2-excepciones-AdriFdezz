import pytest
from src.ejercicio1 import edad_cumplida

def test_edad_cumplida():
    with pytest.raises(ValueError):
        edad_cumplida(-20)