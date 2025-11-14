# Írd ki az összes VLAN nevét és ID-ját (vlans.py).

import json
with open("vlans.json", "r", encoding="utf-8") as fin:
    vlanok=json.load(fin)

for vlan in vlanok["vlans"]:
    print(vlan["name"], vlan["id"])