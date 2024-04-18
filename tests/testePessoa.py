import sys, os

cur_path = os.path.dirname(os.path.abspath(__file__))
head, tail = os.path.split(os.path.split(cur_path)[0])
sys.path.insert(0, os.path.join(head, 'src'))
sys.path.insert(1, os.path.join(head, 'tests'))

import pytest
from src.pessoa import pessoa, Email, pessoaDAO

@pytest.fixture
def pessoaValida():
    return pessoa(1, "Arthur Alves", 30)

@pytest.fixture
def pessoaInvalida():
    return pessoa(2, "Jão", 300)

@pytest.fixture
def emailValido():
    return Email(1, "arthur@example.com")

@pytest.fixture
def emailInvalido():
    return Email(2, "emailInvalido")

def testePessoaValida(pessoaValida, emailValido):
    pessoaValida.emails.append(emailValido)
    dao = pessoaDAO()
    dao.save(pessoaValida)
    assert len(dao.pessoas) == 1

def testePessoaInvalida(pessoaInvalida):
    dao = pessoaDAO()
    dao.save(pessoaInvalida)
    assert len(dao.pessoas) == 0

def testeNomeValido():
    dao = pessoaDAO()
    assert dao.nomeValido("Arthur Alves") is True
    assert dao.nomeValido("Jâo") is False
    assert dao.nomeValido("123 Arthur") is False

def testeIdadeValida():
    dao = pessoaDAO()
    assert dao.idadeValida(30) is True
    assert dao.idadeValida(300) is False