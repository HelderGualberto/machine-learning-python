import numpy

#Array unidimensional
v = numpy.array([1,2,3,4,5,6])
print(v)

#de 0 a 99 com passo de 5
v1 = numpy.arange(0,100,5)
print(v1)

#5 valores entre 0 e 100 espaçados igualmente
v2 = numpy.linspace(0,100,5)
print(v2)

#Array bidimensional
mat = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(mat)

#Acesso indexado igual ao python padrao
print(mat[0,0])

#O : pega a coluna/linha inteira
print(mat[:,0])
print(mat[0,:])

#Acessa o ultimo elemento
print(mat[-1,-1])

m1 = numpy.array([[1,2],[3,4]])
m2 = numpy.array([[5,6],[7,8]])

#Operacoes aritimeticas

print(m1+m2)

print(m1-m2)

print(m1*m2) #Multiplicacao matricial linha x coluna

print(m1.sum()) #somatoria do vetor

print(m1.argmax()) #retorna o indice do maior valor

print(m1.T) #matrix transposta

#exemplo de somatoria
numpy.arange(0,10000000).sum()

a = numpy.array([1,2,3,4,5,6,7,8,9])

print(a[2:5]) #imprime os indices de 2 a 5

print(a[::2])#imprime todos os indices pulando de dois em dois

#a copia de array e diferente das listas em python (a = b[:])

b = a.copy()

b[0] = 100

print(a)
print(b)

#transformar vetor em matriz

print(numpy.reshape(a,(3,3)))


#Operacoes booleanas em matrizes e vetores

a = numpy.array([1,2,3,4,5,6,7,8,9])

print(a[a>4])
print(a[a < 4])

#Carregar arquivos com numpy
#O skiprows pula o numero de linhas
v1,v2,v3 = numpy.loadtxt('data.txt',skiprows=1,unpack=True)

print(v1,v2,v3)

#Preenche os dados faltantes de um arquivo
v1,v2,v3 = numpy.genfromtxt('data2.txt',skip_header=1,unpack=True, filling_values=100)
print(v1,v2,v3)

#Para fazer leitura de dados com diferentes delimitadores
v1,v2,v3 = numpy.genfromtxt('data3.csv',delimiter=',',skip_header=1,unpack=True, filling_values=100)
print(v1,v2,v3)


#embaralha o vetor
numpy.random.shuffle(a) 
print (a)

#numeros complexos com numpy
c = numpy.array([1,10 + 7j, 15 - 8j, 2 +1j], dtype=complex)
c2 = numpy.array([1,10 + 7j, 15 - 8j, 2 +1j], dtype=complex)
print(c)

print(c+c2)


