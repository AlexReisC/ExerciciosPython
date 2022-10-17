class Televisao:

  def __init__(self):
    self.ligada = False
    self.canal = 1
    self.tamanho = 20
    self.marca = "Ching-Ling"
    
  def set_canal(self, num):
    if num < 1:
    	self.canal = 60
    elif num > 60:
    	self.canal = 1
    else:
    	self.canal = num


tv1 = Televisao()
tv1.tamanho = 30
tv1.marca = "LG"

tv2 = Televisao()
tv2.tamanho = 25
tv2.marca = "Samsung"

print(f"Tv 1: marca {tv1.marca} e de tamanho {tv1.tamanho}")
print(f"Tv 2: marca {tv2.marca} e de tamanho {tv2.tamanho}")

print("A letra 'f' dentro do print e antes das aspas serve para formatar variaveis no print que estão entre chaves{}.")

tv1.set_canal(61)
print(f"Canal atual da Tv 1: {tv1.canal}")
tv2.set_canal(0)
print(f"Canal atual da Tv 2: {tv2.canal}")