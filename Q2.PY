def obter_dados_pessoas():
    return [
        {"altura": 1.91, "genero": "Masculino"},
        {"altura": 1.87, "genero": "Masculino"},
        {"altura": 1.75, "genero": "Feminino"},
        {"altura": 1.58, "genero": "Feminino"},
        {"altura": 1.82, "genero": "Masculino"},
        {"altura": 1.67, "genero": "Feminino"},
       
    ]

def calcular_maior_menor_altura(pessoas):

    alturas = [pessoa['altura'] for pessoa in pessoas]
    maior = max(alturas)
    menor = min(alturas)
    return maior, menor

def calcular_media_altura_masculino(pessoas):
 
    masculino = [pessoa['altura'] for pessoa in pessoas if pessoa['genero'] == 'Masculino']
    return sum(masculino) / len(masculino) if masculino else 0

def contar_feminino(pessoas):

    feminino = [pessoa for pessoa in pessoas if pessoa['genero'] == 'Feminino']
    return len(feminino)

pessoas = obter_dados_pessoas()

maior_altura, menor_altura = calcular_maior_menor_altura(pessoas)
media_masculino = calcular_media_altura_masculino(pessoas)
num_feminino = contar_feminino(pessoas)

print(f"A maior altura do grupo é: {maior_altura} metros.")
print(f"A menor altura do grupo é: {menor_altura} metros.")
print(f"A média de altura do gênero Masculino é: {media_masculino} metros.")
print(f"O número de pessoas do gênero Feminino é: {num_feminino}.")