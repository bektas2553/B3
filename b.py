import socket
import socks

server = "irc.kardelenfm.net"
port = 6667
nickname = "Bott"

socks.set_default_proxy(socks.SOCKS5, "162.55.87.48", 5566)

socket.socket = socks.socksocket

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"USER {nickname} {nickname} {nickname} :{nickname}\n".encode())
irc.send(f"NICK {nickname}\n".encode())

while True:
    data = irc.recv(4096).decode(encoding="ISO-8859-9")
    print(data)
    if data.find('PING') != -1:
        irc.send(f"PONG {data.split()[1]}\n".encode())
