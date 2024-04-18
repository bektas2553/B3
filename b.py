import socket
import socks

server = "irc.kardelenfm.net"
port = 6667
link_part = "http://78.135.111.124:2138/"

socks.set_default_proxy(socks.SOCKS5, '194.26.229.46', 20001)
socket.socket = socks.socksocket  # Yeni bir socket oluşturulduğunda SOCKS5 proxy kullanılacak

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server, port))

while True:
    data = irc.recv(4096).decode(encoding='ISO-8859-9')
    print(data)
    if data.find('PING') != -1:
        irc.send('PONG ' + data.split() [1] + '\r\n')
    if link_part in data:
        index = data.find(link_part) + len(link_part)
        link = link_part
        while index < len(data) and data[index] != ' ':
            link += data[index]
            index += 1
        print("Bağlantı ve devamı:", link)
