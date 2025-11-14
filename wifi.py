# Írasd ki az aktív SSID-ket (wifi.json).
import json
with open("wifi.json", "r", encoding="utf-8") as fin:
    wireless=json.load(fin)

for ssid in wireless["access_points"]:
    if ssid["status"]=="active":
        print(f"A(z) {ssid["ssid"]} SSID-val rendelkező Access-pont aktív.")