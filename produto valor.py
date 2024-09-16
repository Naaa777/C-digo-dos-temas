#Declarando o preço do produto e o peercentual de desconto
preco_produto = 150.0
desconto_percentual = 10
#Calculando o valor do desconto
desconto = preco_produto * (desconto_percentual /100)
#Calculando o preço do produto
preco_final = preco_produto - desconto

#Exibindo os resultados
print ("Preço do produto: R$" , preco_produto)
print ("Percentual de desconto: R$", desconto_percentual , "%")
print ("Valor de desconto : R$ ", desconto)
print ("Preço final do produto : R$ ", preco_produto)
