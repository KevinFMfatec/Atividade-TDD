import sys, os

cur_path = os.path.dirname(os.path.abspath(__file__))
head, tail = os.path.split(os.path.split(cur_path)[0])
sys.path.insert(0, os.path.join(head, 'src'))
sys.path.insert(1, os.path.join(head, 'tests'))

import pytest
from src.funcionarios import Funcionario, Cargo

@pytest.fixture
def desenvolvedor():
    return Funcionario("João", "joao@example.com", 3500, Cargo.DESENVOLVEDOR)

@pytest.fixture
def dba():
    return Funcionario("Pedro", "pedro@example.com", 2500, Cargo.DBA)

@pytest.fixture
def testador():
    return Funcionario("Carlos", "carlos@example.com", 2500, Cargo.TESTADOR)

@pytest.fixture
def gerente():
    return Funcionario("José", "jose@example.com", 6000, Cargo.GERENTE)

def testeDesenvolvedorSalarioMaiorOuIgual3000(desenvolvedor):
    assert desenvolvedor.calcularSalarioLiquido() == 2800.0

def testeSalarioDesenvolvedorMenor3000():
    desenvolvedor = Funcionario("Maria", "maria@example.com", 2500, Cargo.DESENVOLVEDOR)
    assert desenvolvedor.calcularSalarioLiquido() == 2250.0

def testeSalarioDBAMaiorIgual2000(dba):
    assert dba.calcularSalarioLiquido() == 1875.0

def testeSalarioDBAMenor2000():
    dba = Funcionario("Ana", "ana@example.com", 1500, Cargo.DBA)
    assert dba.calcularSalarioLiquido() == 1275.0

def testeSalarioTestadorMaiorOuIgual2000(testador):
    assert testador.calcularSalarioLiquido() == 1875.0

def testeSalarioTestadorMenor2000():
    testador = Funcionario("Amanda", "amanda@example.com", 1500, Cargo.TESTADOR)
    assert testador.calcularSalarioLiquido() == 1275.0

def testeSalarioGerenteMaiorOuIgual5000(gerente):
    assert gerente.calcularSalarioLiquido() == 4200.0

def testeSalarioGerenteMenor5000():
    gerente = Funcionario("Patrícia", "patricia@example.com", 4000, Cargo.GERENTE)
    assert gerente.calcularSalarioLiquido() == 3200.0