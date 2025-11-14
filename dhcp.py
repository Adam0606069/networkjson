# Írd ki minden IP-hez a MAC címet (dhcp.json).
import json
with open("dhcp.json", "r", encoding="utf-8") as fin:
    dhcp=json.load(fin)

print(dhcp)

for lease in dhcp["leases"]:
    print(lease["ip"], lease["mac"])