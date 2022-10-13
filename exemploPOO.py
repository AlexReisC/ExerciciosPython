class Dog:
    def __init__(self, nome, idade):
        self.nome = nome.title()
        self.idade = idade

    def sentar(self):
        print(self.nome + " está sentado")
    
    def rolar(self):
        print(self.nome + " está rolando.")

catioro = Dog(nome = "Tobi", idade=5)
print(catioro.nome)
print(catioro.idade)
catioro.sentar
catioro.rolar