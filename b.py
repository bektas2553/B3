import socket
import socks

server = "irc.kardelenfm.net"
port = 6667
link_part = "http://78.135.111.124:2138/"

socks.set_default_proxy(socks.SOCKS5, '162.55.87.48', 5566)
socket.socket = socks.socksocket  # Yeni bir socket oluşturulduğunda SOCKS5 proxy kullanılacak

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))

while True:
    data = irc.recv(4096).decode()
    print(data)
    if link_part in data:
        index = data.find(link_part) + len(link_part)
        link = link_part
        while index < len(data) and data[index] != ' ':
            link += data[index]
            index += 1
        print("Bağlantı ve devamı:", link)
    if data.find('PING') != -1:
        irc.send('PONG ' + data.split() [1] + '\r\n')
