# importando módulo socket
import socket

HOST = 'localhost'
PORT = 45678
# criando socket passando como parâmetro o IPV4 e TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# vinculando o host 'localhost' a porta '45678'
s.bind((HOST, PORT))
# escutando pedidos do cliente
s.listen()
# aceita a conexão e repassa conn para conexão e ender para endereço do cliente
conn, ender = s.accept()
# imprime na tela a mensagem seguido do endereço do cliente
print('[Conexão com', ender, "]")
# abre arquivo e repassa pro objeto
arq = open('arquivo.json', 'rb')
# lê o arquivo e repassa em binário para o objeto
upload = arq.read(6000)
# envia o objeto
conn.send(upload)
# fecha arquivo
arq.close()
# fecha conexão
conn.close()
