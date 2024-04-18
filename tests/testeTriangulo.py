import sys, os

cur_path = os.path.dirname(os.path.abspath(__file__))
head, tail = os.path.split(os.path.split(cur_path)[0])
sys.path.insert(0, os.path.join(head, 'src'))
sys.path.insert(1, os.path.join(head, 'tests'))

import pytest
from src.triangulo import Triangulo

@pytest.fixture(scope="function")
def teste():
    return Triangulo()

def testeEscaleno(teste: Triangulo):
    ret = teste.verificaTriangulo(10, 8, 4)
    assert ret == "Triângulo Escaleno"

def testeIsosceles(teste: Triangulo):
    ret = teste.verificaTriangulo(10, 10, 8)
    assert ret == "Triângulo Isósceles"

def testeEquilateral(teste: Triangulo):
    ret = teste.verificaTriangulo(10, 10, 10)
    print(ret)
    assert ret == "Triângulo Equilatero"

@pytest.mark.parametrize("a, b, c, tipo", [
    (5, 5, 3, "Triângulo Isósceles"),
    (7, 7, 2, "Triângulo Isósceles"),
    (4, 4, 6, "Triângulo Isósceles")
])
def testeIsocelesPermutacao(a: int, b: int, c: int, tipo: str, teste: Triangulo):
    ret = teste.verificaTriangulo(a, b, c)
    assert ret == tipo

@pytest.mark.parametrize("a, b, c, tipo", [
    (5, 5, 0, "Não é um triângulo válido"),
    (7, 7, -2, "Não é um triângulo válido")
])
def valorInvalido(a: int, b: int, c: int, tipo: str, teste: Triangulo):
    ret = teste.verificaTriangulo(a, b, c)
    assert ret == tipo

@pytest.mark.parametrize("a, b, c, tipo", [
    (8, 4, 4, "Não é um triângulo válido"),
    (8, 4, 4, "Não é um triângulo válido"),
    (4, 8, 4, "Não é um triângulo válido"),
    (4, 4, 8, "Não é um triângulo válido"),
])
def somaDosLados(a: int, b: int, c: int, tipo: str, teste: Triangulo):
    ret = teste.verificaTriangulo(a, b, c)
    assert ret == tipo

@pytest.mark.parametrize("a, b, c, tipo", [
    (8, 4, 4, "Não é um triângulo válido"),
    (8, 4, 4, "Não é um triângulo válido"),
    (4, 8, 4, "Não é um triângulo válido"),
    (4, 4, 8, "Não é um triângulo válido"),
])
def somaDosDoisLadosEquilatero(a: int, b: int, c: int, tipo: str, teste: Triangulo):
    ret = teste.verificaTriangulo(a, b, c)
    assert ret == tipo

@pytest.mark.parametrize("a, b, c, tipo", [
    (10, 4, 4, "Não é um triângulo válido"),
    (10, 4, 4, "Não é um triângulo válido"),
    (4, 10, 4, "Não é um triângulo válido"),
    (4, 4, 10, "Não é um triângulo válido"),
])
def somaDosDoisLadosMenor(a: int, b: int, c: int, tipo: str, teste: Triangulo):
    ret = teste.verificaTriangulo(a, b, c)
    assert ret == tipo

def TesteZero(teste: Triangulo):
    ret = teste.verificaTriangulo(0, 0, 0)
    assert ret == "Não é um triângulo válido"