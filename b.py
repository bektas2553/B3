import socket
import socks

server = "irc.kardelenfm.net"
port = 6667
nickname = "Bott"
link_part = "http://78.135.111.124:2138/"

socks.set_default_proxy(socks.SOCKS5, "45.138.87.238", 1080)

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
      
    if link_part in data:
        index = data.find(link_part) + len(link_part)
        remaining_text = data[index:]
        link = remaining_text.split(':')[0]
        print("Bağlantı ve devamı:", link)
