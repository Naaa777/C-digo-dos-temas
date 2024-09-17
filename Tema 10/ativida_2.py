#Cria uma lista de números reais 
numeros = [3.5, 2.6, 7.8, 2.7, 8.9,1.0]

for i in numeros:
    print("Numero:", i)
    
#Inicializa variaveis para o menor valor 
menor_valor = min(numeros)
print("Menor valor: ", menor_valor)

numerosIndex = numeros.index(menor_valor)
print("Indice do menor valor", numerosIndex)
