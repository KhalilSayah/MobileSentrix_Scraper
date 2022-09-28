import json 

json_file_path = "product.json"

links = []


with open(json_file_path, 'r') as j:
     data = json.loads(j.read())

for i in range(len(data)):
    links.append(data[i]["link"])

print(len(links))




