from enum import Enum

class Cargo(Enum):
    DESENVOLVEDOR = 1
    DBA = 2
    TESTADOR = 3
    GERENTE = 4

class Funcionario:
    def __init__(self, nome, email, salarioBase, cargo):
        self.nome = nome
        self.email = email
        self.salarioBase = salarioBase
        self.cargo = cargo

    def calcularSalarioLiquido(self):
        if self.cargo == Cargo.DESENVOLVEDOR:
            if self.salarioBase >= 3000:
                return self.salarioBase * 0.8
            else:
                return self.salarioBase * 0.9
        elif self.cargo == Cargo.DBA or self.cargo == Cargo.TESTADOR:
            if self.salarioBase >= 2000:
                return self.salarioBase * 0.75
            else:
                return self.salarioBase * 0.85
        elif self.cargo == Cargo.GERENTE:
            if self.salarioBase >= 5000:
                return self.salarioBase * 0.7
            else:
                return self.salarioBase * 0.8
