#Classes em python

#No python 3 e necessario colocar a heranca da classe padrao Object
class Pessoa(object):

	#Contrutor da classe
	#Utiliza-se o self como referencia ao proprio objeto
	def __init__(self, nome, idade):

		#Sempre que formas adicionar atributos ao objeto, deve-se
		#utilizar o self
		#Isso e equivalente a declarar a variavel no escopo global da
		#classe, como em Java e CPP

		#Por padrao esses atributos sao publicos
		self.nome = nome
		self.idade = idade

	#Todas as funcoes devem receber a referencia ao proprio objeto
	def imprime_nome(self):
		print(self.nome)


#A heranca em python e dada atraves da passagem de um parametro
#que indica a classe Pai

#Classe cidadao herda de pessoa
class Cidadao(Pessoa):

	def __init__(self,nome,idade,cpf,rg):
		#E necessario chamar o init da superclasse
		super(Cidadao,self).__init__(nome,idade)
		self.rg = rg
		self.cpf = cpf

	#funcao padrao chamada pelo print
	#Devemos fazer a sobreascrita para imprimir o que desejamos
	#A funcao print sempre faz a chada da funcao str do objeto passado por parametro
	def __str__(self):
		return self.nome

p = Pessoa("Helder",22)

print(p.nome)
p.imprime_nome()

c = Cidadao("Helder",22,1234,4321)
c.imprime_nome()

print(c.cpf)
print(c.rg)
print(c)



