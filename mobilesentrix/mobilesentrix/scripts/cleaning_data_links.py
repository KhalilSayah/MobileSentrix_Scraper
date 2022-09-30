import json
from logging.handlers import BaseRotatingHandler


dump_file_path = "dump.txt"
json_file_path = "../categoriesall.json"

links = []
banned_links =["Javascript:void(0);","Javascript:void();","javascript:void();","javascript:void(0);"]
f = open(dump_file_path, "w")

with open(json_file_path, 'r') as j:
     data = json.loads(j.read())


for key in data[0]:
    for link in data[0][key]:
        if link not in banned_links:
            links.append(link)

print(len(links))
f.write(str(links))
