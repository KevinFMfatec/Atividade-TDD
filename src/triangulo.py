class Triangulo:
    def __init__(self):
        pass

    def verificaTriangulo(self, a, b, c) -> str:
        if not self.triangulo_valido(a, b, c):
            return "Não é um triângulo válido"
        elif self.equilateral(a, b, c):
            return "Triângulo Equilátero"
        elif self.isosceles(a, b, c):
            return "Triângulo Isósceles"
        else:
            return "Triângulo Escaleno"

    def trianguloValido(self, a: int, b: int, c: int) -> bool:
        if a <= 0 or b <= 0 or c <= 0:
            return False
        elif a + b <= c or a + c <= b or b + c <= a:
            return False
        else:
            return True

    def isosceles(self, a: int, b: int, c: int) -> bool:
        if a == b or a == c or b == c:
            return True
        else:
            return False

    def equilateral(self, a: int, b: int, c: int) -> bool:
        return a == b == c
