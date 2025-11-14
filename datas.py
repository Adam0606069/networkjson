import json

with open ("datas.txt", "r", encoding="utf-8") as fin:
    adatok=json.load(fin)

print(adatok)

for pont in adatok:
    pont["pont"]+=1

print(adatok)

with open ("datas1.txt", "w", encoding="utf-8") as fout:
    adatok=json.dump(adatok, fout, ensure_ascii=False, indent=4)