import pytest
from app.models.usuario import Usuario


@pytest.fixture
def cria_usuario():
    usuario01= Usuario("Pedro","Pedro@gmail","123")
    return usuario01

def test_varificar_valor_vazio():
    with pytest.raises(ValueError,match= "A mensagem não pode esta vazia."):
        Usuario("Pedro","","456")
        
        


    