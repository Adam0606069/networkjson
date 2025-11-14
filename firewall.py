# Gyűjtsd ki az összes IP-t, ahol action = "deny" (firewall.json).
import json
with open("firewall.json", "r", encoding="utf-8") as fin:
    tuzfal=json.load(fin)

print(tuzfal)

deny_ips=[]

for rule in tuzfal["rules"]:
    if rule["action"]=="deny":
        deny_ips.append(rule["ip"])

print(f"A tiltott IP-k a következők: {deny_ips}")