# putting first 3 characcters of an ip address into a list and print
# addresses are just for example purposes.
ip_addresses1 = ["198.576.342.245" , "424.242.245.145", "342.545.242.536" , "245.142.534.157", "234.634.625.252" ]
networks = []
for address in ip_addresses1:
    networks.append(address[0:3])
print(networks)
