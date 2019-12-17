"""
Script para intentar encender una maquina | deben de tener la opción habilitada en el BIOS
uso: encender_maquina.py nombre_host ej: encender_maquina host1
Por: ]3/\|)´|+|>< versión 0.0.1 | 12 noviembre 2019
"""
import socket
import sys
import msvcrt

def check_up(hostname, mode):
	result = ''
	try:
		result = socket.getaddrinfo(hostname, None, socket.AF_INET,\
			socket.SOCK_DGRAM, socket.IPPROTO_IP, socket.AI_CANONNAME)
		ip_list = [x[4][0] for x in result]
		if mode:
			return True

		return ip_list
	except Exception:
		return False

def encender(hostname):
	print("Haciendo intento de encender maquina: %s" % hostname)
	
	while not check_up(hostname, True):
		print("El host aun no enciende ...")
	ips = check_up(hostname, False)
	print("-- Host inicio funciones de red --\nIps del host: ")
	
	for ip in ips:
		print("\t"+ip)

print("\
\
   _____ _____ _____ __  __ \n\
  / ____|_   _|_   _|  \\/  | Script: encender_maquina\n\
 | (___   | |   | | | \\  / | ver: 0.0.1\n\
  \\___ \\  | |   | | | |\\/| | Fecha: 12-11-19\n\
  ____) |_| |_ _| |_| |  | | Por: ]3/\\|)´|+|><.\n\
 |_____/|_____|_____|_|  |_|\n\
")
if len(sys.argv) > 1:
	host_name = sys.argv[1]
	
else:
	host_name = str(input("Nombre del host: "))

encender(host_name)
msvcrt.getch()
