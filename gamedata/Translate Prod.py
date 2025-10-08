import json

# Load the FurnitureData JSON file
with open('FurnitureData.json', 'r', encoding='utf-8') as f:
    furniture_data = json.load(f)

# Create a dictionary mapping classname to name and description
furniture_dicts = {}
for furnitype in furniture_data['roomitemtypes']['furnitype'] + furniture_data['wallitemtypes']['furnitype']:
    classname = furnitype['classname']
    name = furnitype.get('name')
    description = furnitype.get('description')
    
    # Store the data in the dictionary
    furniture_dicts[classname] = {
        'name': name,
        'description': description,
    }

# Load the ProductData JSON file
with open('ProductData.json', 'r', encoding='utf-8') as f:
    product_data = json.load(f)

# Replace the name and description values in ProductData with values from FurnitureData
for product in product_data['productdata']['product']:  # Acessando a lista de produtos corretamente
    classname = product['code']  # Supondo que 'code' corresponda ao 'classname' no FurnitureData
    if classname in furniture_dicts:
        product['name'] = furniture_dicts[classname]['name']
        product['description'] = furniture_dicts[classname]['description']

# Save the updated ProductData JSON file
with open('ProductData.json', 'w', encoding='utf-8') as f:
    json.dump(product_data, f, ensure_ascii=False, indent=4)
