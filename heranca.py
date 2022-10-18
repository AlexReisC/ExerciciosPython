class Pessoa:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def info(self):
        return "{} {}, {} anos" .format(self.nome, self.sobrenome, self.idade)


class Aluno(Pessoa):
    def __init__(self, nome, sobrenome, idade, instituicao, materias=None):
        Pessoa.__init__(self, nome, sobrenome, idade)
        self.instituicao = instituicao
        if materias is None:
            self.materias = []
            #self.materias = self.materias.append(materia)
        else:
            self.materias = materias

    def exibir_materias(self):
        for x in self.materias:
            print(x)


"""class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, idade, cargo, salario):
        Pessoa.__init__(self, nome, sobrenome, idade)
        self.cargo = cargo
        self.salario = salario
    def aumentar_salario(self, porcentagem):
        self.salario += 


class Desenvolvedor(Funcionario):
    def __init__(self, nome, sobrenome, idade, salario, setor):
        super.__init__(self, nome, sobrenome, idade, "Engenheiro de Software", salario, setor)
"""

if __name__ == "__main__":
    p1 = Pessoa("Maria", "Teresa", 12)
    print(p1.info())

    p2 = Aluno("José", "da Silva", 33, "UFCA", ["Laboratório de Programação", "Circuitos Digitais", "Algoritmos e Estruturas de dados"])
    print(p2.info())

