# Criando um dicionário para um gatinho
gatinho = {
    "nome": "Mimi",
    "idade": 2,
    "raça": "Siamês",
    "peso": 4.5,
    "vacinas": ["Antirrábica", "Tríplice Felina", "Leucemia Felina"],
    "dono": "Ana"
}

# Exibindo as informações do dicionário na tela
print("Nome:", gatinho["nome"])
print("Idade:", gatinho["idade"])
print("Raça:", gatinho["raça"])
print("Peso:", gatinho["peso"])
print("Vacinas:", ", ".join(gatinho["vacinas"]))
print("Dono:", gatinho["dono"])