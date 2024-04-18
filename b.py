import socket
import socks

server = "irc.kardelenfm.net"
port = 6667
nickname = "Bott"

socks.set_default_proxy(socks.SOCKS5, "162.55.87.48", 5566)  # SOCKS5 proxy bilgilerini ayarlayın
socket.socket = socks.socksocket  # Yeni bir socket oluşturulduğunda SOCKS5 proxy kullanılacak

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))
irc.send(f"USER {nickname} {nickname} {nickname} :{nickname}\n".encode())
irc.send(f"NICK {nickname}\n".encode())

while True:
    data = irc.recv(4096).decode()
    print(data)
    if data.find('PING') != -1:
        irc.send('PONG ' + data.split() [1] + '\r\n')
