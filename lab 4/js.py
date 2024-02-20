# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 

import json

with open(r'C:\Users\User\Desktop\PP2\lab 4\sample-data.json')as some_file:
    data = json.load(some_file)

print("Interface Status")
print("="*78)
print("{:<50}{:<21}{:<9}{:<6}".format("DN","Description","Speed","MTU"))
print("-"*49 + " " + "-"*20 + " "*2 + "-"*6 + " "*2 + "-"*6)

for i in data['imdata']:
    attributes = i['l1PhysIf']['attributes']
    dn = attributes['dn']
    description = attributes['descr']
    speed = attributes['speed']
    mtu = attributes['mtu']
    print("{:<50}{:<21}{:<10}{:<6}".format(dn, description, speed, mtu))
