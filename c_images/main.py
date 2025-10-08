import os
import requests
import json

def download_swf_and_icons(furnitures):
    swf_dir = "catalogue"

    if not os.path.exists(swf_dir):
        os.makedirs(swf_dir)
        print(f"Diretório '{swf_dir}' criado.")
    
    item_name = furnitures.get('_icon', 0)

    if item_name:
        # Download SWF
        swf_url = f"https://images.habblet.city/c_images/catalogue/icon_{item_name}.png"
        swf_path = os.path.join(swf_dir, f"icon_{item_name}.png")

        if not os.path.exists(swf_path):
            try:
                response = requests.get(swf_url)
                response.raise_for_status()
                with open(swf_path, 'wb') as f:
                    f.write(response.content)
                print(f"Arquivo SWF baixado e salvo em '{swf_path}'.")
            except requests.RequestException as e:
                print(f"Erro ao baixar arquivo SWF para {item_name}: {e}")
    
    # Check for children and recursively call the function
    if "_children" in furnitures:
        for child in furnitures["_children"]:
            download_swf_and_icons(child)

# Load JSON data
json_data = None
with open(file="./habblet-catalog.json", mode="r", encoding="utf-8") as file:
    json_str = file.read()
    try:
        json_data = json.loads(json_str)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        json_data = []

# Process each page and item
for key, page in json_data["pages"].items():
    download_swf_and_icons(page)