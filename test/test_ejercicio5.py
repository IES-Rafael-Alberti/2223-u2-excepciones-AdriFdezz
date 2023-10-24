import pytest
from src.ejercicio5 import verificar_contrasenia

def test_verificar_contrasenia():
    with pytest.raises(NameError):
        verificar_contrasenia("contraseña123")