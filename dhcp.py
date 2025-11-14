# Írd ki minden IP-hez a MAC címet (dhcp.json).
import json
with open("dhcp.json", "r", encoding="utf-8") as fin:
    dhcp=json.load(fin)

print(dhcp)

volt=False

be=input("Adj meg egy ip-címet: ")

for lease in dhcp["leases"]:
    if be==lease["ip"]:
        volt=True
        break

if volt:
    print(lease["ip"], lease["mac"])
else:
    print("Nem volt.")    