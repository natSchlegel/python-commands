import socket

HOST = 'localhost'
PORT = 45678
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# cria o arquivo arquivo.json e repassa para o objeto
arq = open('arquivo.json', 'wb+')
# objeto escreve o que recebe da conexão
arq.write(s.recv(6000))
arq.close()
s.close()
