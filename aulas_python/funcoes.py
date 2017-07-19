#Funcoes
#Valores default para funcoes


#Passar vetores para funcoes
#O asterisco desempacota os dados dentro do vetor.
#Os dados podem ser passados sem estar em um vetor 
#Pois utilizando o asterisco havera o empacotamento dos dados
def sum_all(*vect):
	print(vect) 



def nome(nome="desconhecido"):
	print(nome)
	return

nome()
nome("Helder")

print(sum_all([1,2,3,45,6,7]))

print(sum_all(1,2,3,45,6,7))

#funcoes lambda

a = lambda x: x*2
print(a(2))
