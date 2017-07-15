#Este script mostra algumas operações para entrada de dados em python

#Para funções com a mesma funcionalidade do 'scanf' tem-se o 'input'
#Por padrao a funcao input recebe um valor string
#para utilizar como outros tipos de dados é necessário fazer cast

string = input('String: ') #Neste caso a função escreve o tento "String: "
							#Mas retorna apenas o dado entrado
print(type(string))
print(string)

inteiro = int(input('Inteiro: '))
print(type(inteiro))
print(inteiro)

flutuante = float(input('Flutuante: '))
print(type(flutuante))
print(flutuante)