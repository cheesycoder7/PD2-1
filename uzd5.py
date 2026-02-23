# Hostname; IP; Latency(ms); Status
nodes = [
"Srv-Web-01;192.168.1.10;15;UP",
"Srv-DB-01;192.168.1.20;450;UP",
"Srv-Backup;10.0.0.5;0;DOWN",
"Workstation-A;192.168.1.105;5;UP",
"Srv-Proxy-01;172.16.0.1;10;up",
"Srv-Mail;10.0.0.10;120;UP",
"Router-Core;192.168.1.1;2;UP",
"Srv-Dev-01;192.168.2.50;500;UP",
"Printer-Main;192.168.1.200;0;down",
"Srv-Log;10.0.0.15;105;UP"
]
y = 0
new_nodes = []
for i in range(len(nodes)):
    split_node = nodes[i].split(";")
    name_lower = split_node[0].lower()
    name_under = name_lower.replace("-","_")
    split_node[0] = f"{name_under}.local"
    new_nodes.append(split_node)
    print(new_nodes[i][0])
    