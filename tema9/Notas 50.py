Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Declarando o valor da conta
... valor_conta = 137  # Exemplo de valor
... 
... # Calculando a quantidade de notas de 50
... notas_50 = valor_conta // 50
... resto = valor_conta % 50
... 
... # Calculando a quantidade de notas de 10
... notas_10 = resto // 10
... resto = resto % 10
... 
... # Calculando a quantidade de notas de 1
... notas_1 = resto
... 
... # Exibindo os resultados
... print("Notas de 50:", notas_50)
... print("Notas de 10:", notas_10)
