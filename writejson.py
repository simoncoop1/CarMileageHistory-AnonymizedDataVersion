import json
import generator


##make a dictionary of makes and models for 2019
make_mdl = {}

#goes to alist of models

for c in generator.dGenerateCars():
    if c[8] == "make":
        continue
    if len(c) != 14:
        continue
    if c[2][0:4] != "2019":
        continue
    if c[8] in make_mdl.keys():
        if c[9] not in make_mdl[c[8]]:
            make_mdl[c[8]].append(c[9])
    else:
        make_mdl[c[8]] = [c[9],]
    

#data = ["Land Rover","Skoda","Volswagen","Rolls Royce"]
data = make_mdl

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

sorteed = sorted(data.keys(), key=lambda p: p)
with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(sorteed, f, ensure_ascii=False, indent=4)
