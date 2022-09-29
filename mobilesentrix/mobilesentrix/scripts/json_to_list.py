import json


dump_file_path = "Apple_start_urls.txt"
json_file_path = "result.json"

links = []
f = open(dump_file_path, "w")

with open(json_file_path, 'r') as j:
     data = json.loads(j.read())


for key in data[0]:
    for link in data[0][key]:
        links.append(link)
        
        


f.write(str(links))
print(len(links))
