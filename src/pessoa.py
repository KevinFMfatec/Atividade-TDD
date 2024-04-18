from typing import List, Tuple
import re

class pessoa:
    def __init__(self, id: int, nome: str, idade):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.emails: List[Email] = list()

class Email:
    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome

class pessoaDAO:
    def __init__(self):
        self.pessoas: List[pessoa] = list()

    def save(self, pessoa:pessoa):
        errors = self.valido(pessoa)
        if len(errors) == 0:
            self.pessoas.append(pessoa)

    def valido(self, pessoa:pessoa) -> List[str]:
        erros = list()
        if not self.nomeValido(pessoa.nome):
            erros.append("Nome é válido")
        if not self.idadeValida(pessoa.idade):
            erros.append("Idade é válido")
        if not self.pessoaTemEmail(pessoa.emails):
            erros.append("Pessoa precisa ter email")
        for email in pessoa.emails:
            if not self.emailValido(email.nome):
                erros.append("Email é invalido, deve esta no formato _____@____._____")
        print(erros)
        return erros

    def nomeValido(self, nome:str) -> bool:
        nomes = nome.split(" ")
        has_digit = bool(re.search(r'\d', nome))
        if len(nomes) >= 2 and not has_digit:
            return True
        else:
            return False

    def idadeValida(self, idade:int) -> bool:
        if idade in range(1, 201):
            return True
        else:
            return False

    def pessoaTemEmail(self, emails: List[Email]):
        if len(emails) >= 1:
            return True
        else:
            return False

    def emailValido(self, email: str) -> Tuple[bool, None]:
        padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(padrao, email) is not None