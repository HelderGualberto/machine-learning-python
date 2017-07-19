#As variáveis em python são rótulos para seus resultados
#No caso de strings elas são imutáveis, por isso quando atribuído um novo valor
#ele cria um novo objeto, pois ele não altera o rótulo

#Um exemplo simples é:

nome = "Helder"
nome2 = nome
print(id(nome))
print(id(nome2))
print('\n')

#isso resultara em ids iguais, pois o rótulo criado foi o nome "Helder"
#E as variáveis apontam para este rótulo
#Outra forma de comprovar isso é:

nome = "Helder"
nome2 = "Helder"
print(id(nome))
print(id(nome2))

#Os ids continuam iguais, mesmo que as variáveis sejam diferentes

#Quando atribuimos um novo valor para nome ou nome2, ele apenas irá
#mudar o apontamento do rótulo, e o rótulo original será mantido enquanto
#houver alguma referência para si


nome = "Helder"
nome2 = nome
print(id(nome))
print(id(nome2))

nome = "Rodrigues"

print(id(nome))
print(id(nome2))

#Neste caso, no primeiro print os ids serão iguais, no entanto, no
#segundo print eles serão diferentes, pois apontam agora para rótulos 
#diferentes.
#Não se pode confundir os rótulos de python com os ponteiros em C para strings
#pois neste caso estes objetos são imutáveis

nome = "Helder"
nome2 = "Rodrigues"
print(id(nome))
print(id(nome2))
print('\n')

nome = nome2

print(id(nome))
print(id(nome2))
print('\n')

nome = "Helder"
print(id(nome))
print(id(nome2))
