import json
with open("C:/Users/baqzh/OneDrive/Рабочий стол/labaratory works/LAB4/json", "r") as f:
    data = json.load(f)
print("Inherit status")
print("="*50)
print("DN")
print("-"*50)
for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn")
    descr = attr.get("descr")
    speed = attr.get("speed")
    mtu = attr.get("mtu")
    print(f"{dn:50} {descr:11} {speed:7} {mtu}")