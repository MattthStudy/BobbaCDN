import os
import requests
from datetime import datetime
import json

def download_swf_and_icons(furnitures):
    swf_dir = "furniture"
    icons_dir = os.path.join(swf_dir, "icons")

    if not os.path.exists(swf_dir):
        os.makedirs(swf_dir)
        print(f"Diretório '{swf_dir}' criado.")
    
    if not os.path.exists(icons_dir):
        os.makedirs(icons_dir)
        print(f"Diretório '{icons_dir}' criado.")

    for furni in furnitures:
        item_name = furni['classname'].replace("*", "_")
        
        # Download SWF
        swf_url = (f"https://images.habblet.city/leet-asset-bundles/libraries/furniture/{item_name}.nitro")

        swf_path = os.path.join(swf_dir, f"{item_name}.nitro")

        if not os.path.exists(swf_path):
            try:
                response = requests.get(swf_url)
                response.raise_for_status()
                with open(swf_path, 'wb') as f:
                    f.write(response.content)
                print(f"Arquivo SWF baixado e salvo em '{swf_path}'.")
            except requests.RequestException as e:
                print(f"Erro ao baixar arquivo SWF para {item_name}: {e}")

        # Download Icon
        icon_url = (f"https://images.habblet.city/library/hof_furni/icons/{item_name}_icon.png")

        icon_path = os.path.join(icons_dir, f"{item_name}_icon.png")

        if not os.path.exists(icon_path):
            try:
                response = requests.get(icon_url)
                response.raise_for_status()
                with open(icon_path, 'wb') as f:
                    f.write(response.content)
                print(f"Ícone baixado e salvo em '{icon_path}'.")
            except requests.RequestException as e:
                print(f"Erro ao baixar ícone para {item_name}: {e}")

json_data = None
with open(file="./habblet_furni.json", mode="r", encoding="utf-8") as file:
    json_str = file.read()
    try:
        json_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        json_data = []

# Inserir todas as páginas e itens
for itemx, item_list in json_data.items():
    download_swf_and_icons(item_list["furnitype"])
