class Cliente:
	def __init__(self, nome, cpf, telefone, endereco):
		self.nome = nome
		self.cpf = cpf
		self.telefone = telefone 
		self.endereco = endereco

class Conta:
	def __init__(self, agencia, numero, saldo):
		self.agencia = agencia
		self.numero = numero
		self.saldo = saldo
		self._cliente = None
	
	def deposito(self, valor):
		if valor > 1:
			self.saldo = self.saldo + valor
			print("Deposito realizado!")
		else:
			print("Valor inválido!")
		
	def saque(self, valor):
		if self.saldo > 0:
			if valor > self.saldo:
				print(f"Não é possivel sacar essa quantia, o valor maior que o saldo na conta!")
			else:
				self.saldo = self.saldo - valor
				print(f"Saque realizado!")
		else:
			print("Você não possui saldo na conta.")
		
	def consultar_saldo(self):
		print(f"Seu saldo atual é de R$ {self.saldo}")
	
	def transferencia(self, conta1, conta2, valor):
		if conta1.saldo > 0:
			if conta1.saldo1 > valor:
				conta2.saldo += valor
				print(f"Transferência realizada! Valor: R$ {valor}")
			else:
				print("Saldo insuficiente.")
		else:
			print("Sem saldo.")
	
	def cliente(self, cliente):
			self._cliente = cliente

class Investimentos(Conta):
	def __init__(self, agencia, numero, saldo):
		Conta.__init__(self, agencia, numero, saldo)
		self.porcentagem = 0.1

	def investir(self, valor):
		rend = (valor * self.porcentagem)
		self.saldo += rend
		return rend

class Poupanca(Conta):
	def __init__(self, agencia, numero, saldo):
		Conta.__init__(self, agencia, numero, saldo)
		self.porcentagem = 0.01
	def rendimento(self):
		self.saldo += (self.saldo * self.porcentagem)
		return self.saldo


conta1 = Conta("1234-5", "56789-0", 50.0)
print("Número da conta: " + conta1.numero + "\nSaldo da conta: R$ {}" .format(conta1.saldo))
conta1.saque(60)

cliente1 = Cliente("Alex Reis", "123.456.789-00", "99999998", "Rua dos Bobos - 0")
	
conta1.cliente = cliente1
print("="*30 + "\nCONTA 1")
print("Número da conta: " + conta1.numero +  "\nNome do Cliente: " + conta1.cliente.nome + "\nSaldo da conta: R$ {}" .format(conta1.saldo))
	
conta2 = Conta("2637-5", "28378-9", 100.0)
cliente2 = Cliente("Karl Marx", "123.563.785-88", "74938383", "Rua do Limoeiro - 111")
conta2.cliente = cliente2
print("="*30 + "\nCONTA 2")
print("Número da conta: " + conta2.numero +  "\nNome do Cliente: " + conta2.cliente.nome + "\nSaldo da conta: R$ {}" .format(conta2.saldo))
	
conta3 = Conta("8337-8", "04848-0", 99999.99)
cliente3 = Cliente("Neymar dos Santos Junior", "927.102.372-58", "91362917", "Paris - França")
conta3.cliente = cliente3
print("="*30 + "\nCONTA 3")
print("Número da conta: " + conta3.numero +  "\nNome do Cliente: " + conta3.cliente.nome + "\nSaldo da conta: R$ {}" .format(conta3.saldo))

conta4 = Conta("2540-9", "14236-0", 1000.50)
cliente4 = Cliente("Xi JinPing", "111.111.111-11", "103052", "Republica Popular da China")
conta4.cliente = cliente4
print("="*30 + "\nCONTA 4")
print("Número da conta: " + conta4.numero +  "\nNome do Cliente: " + conta4.cliente.nome + "\nSaldo da conta: R$ {}" .format(conta4.saldo))

print("\n")
poupanca = Poupanca("08008", "46467", 63339)
poupanca.consultar_saldo()
print (f"Seu dinheiro rendeu: {poupanca.rendimento()}")

print("\n")
investimento = Investimentos("5889-9", "48779-0", 6500)
investimento. consultar_saldo()
investimento.investir(200)
investimento.consultar_saldo()
