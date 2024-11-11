
import pytest

from app.models.usuario import Usuario

@pytest.fixture
def usuario_valido():
    return Usuario("pedro","pedro@gmail.com","123")

def test_nome_valido(usuario_valido):
    assert usuario_valido.nome == "pedro"

def test_email_valido(usuario_valido):
    assert usuario_valido.email == "pedro@gmail.com"

def test_senha_valida(usuario_valido):
    assert usuario_valido.senha == "123"

def test_nome_vazio():
    with pytest.raises(ValueError,match = "Insira um valor."):
        Usuario("","Pedro@gmail.com","123")

def test_nome_invalido():
    with pytest.raises(TypeError, match= "Tipo inválido."):
        Usuario(256,"Pedro@gmail.com","123")

def test_email_vazio():
    with pytest.raises(ValueError,match = "Insira um valor."):
        Usuario("Pedro","","123")

def test_email_invalido():
    with pytest.raises(TypeError, match= "Tipo inválido."):
        Usuario(256,789,"123")

def test_senha_invalida():
    with pytest.raises(TypeError, match= "Tipo inválido."):
        Usuario(256,"Pedro@gmail.com",123)       
        
def test_senha_vazia():
    with pytest.raises(ValueError,match = "Insira um valor."):
        Usuario("Pedro","Pedro@gmail.com","")


        


    