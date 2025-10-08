import os
import json

# Caminho para a pasta que contém as imagens
directory = r'C:\Habbo\Assets\c_images\album1584'

# Lista para armazenar os nomes das imagens
image_names = []

# Percorre todos os arquivos no diretório
for filename in os.listdir(directory):
    # Verifica se é um arquivo (e não um diretório)
    if os.path.isfile(os.path.join(directory, filename)):
        image_names.append(filename)

# Cria o arquivo JSON e escreve os nomes das imagens
with open('Badges.json', 'w') as json_file:
    json.dump(image_names, json_file)

print(f'Arquivo JSON criado com {len(image_names)} imagens.')
