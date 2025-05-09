import nmap
import ipaddress

#!/usr/bin/python3

#192.168.0.30
print("")
print("   _____    _____           _____ ")
print("  / ____|  / ____|  ______ /  __ |")
print(" | |      | (___   |___  / \ \_| |")
print(" | |       \ __ \    |_  \  \__  |")
print(" | |____   ____) |  ___) |     | |")
print("  \_____| |_____/  |_____/     |_|")
print("")

try:
    ip = input("Dirección IP a escanear: ")
    ipaddress.ip_address(ip)  # Valida IP
except ValueError:
    print("[-] Dirección IP inválida")
    exit()
try:	
	#Creación de instancia de la clase PortScanner
	p_scan = nmap.PortScanner()
	puertos_abiertos="-p "
	results = p_scan.scan(hosts=ip,arguments="-n -Pn -T4")
	#results = nm.scan(hosts=ip,arguments="-Pn -sV")
	count=0

	#Se muestra host y estado de este
	print("\nHost : %s" % ip)
	print("Estado : %s" % p_scan[ip].state())

	#Iteración sobre los protocolos detectados (TCP, UDP...)
	for proto in p_scan[ip].all_protocols():
		print("Protocol : %s" % proto)
		print()
		#Se obtienen los puertos de cada protocolo
		lport = p_scan[ip][proto].keys()
		sorted(lport)
		for port in lport:
			#Se muestran puertos y estado (abierto, cerrado, filtrado...)
			print ("Puerto : %s\tEstado : %s" % (port, p_scan[ip][proto][port]["state"]))
			#String con '-p' y los puertos abiertos
			if count==0:
				puertos_abiertos=puertos_abiertos+str(port)
				count=1
			else:
				puertos_abiertos=puertos_abiertos+","+str(port)

	print("\nPuertos abiertos: "+ puertos_abiertos)
	print("\nnmap "+ puertos_abiertos +" -Pn -sV "+ ip + " -O -sC")

#Se permite terminar el script en caso de necesidad (Ctrl+C)
except KeyboardInterrupt:
	print("\nEscaneo cancelado!" )
	exit()