# Fundamentos de Redes de Computadores
# Professor: Daniel Fireman
# ALUNO: Marcos Messias de Souza e Silva

import socket

# Configurações do servidor 
host = '127.0.0.1'
port = 7000
origem = (host, port) #tupla de IP + Porta

# Instancia o socket à variável
# AF_INET -Família do Protocolo e SOCK_STREAM indica o TCP/IP
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# Para Zerar o TIME_WAIT
serv_socket.setsockopt (socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serv_socket.bind(origem) 
serv_socket.listen(10)

print ("""
	#####################################
	#         SERVIDOR INICIADO         #
	#                                   #
	#    Digite SAIR para finalizar     #
	#####################################\n""")

print('\n#=> Aguardando conexão do cliente!')

# Aguarda a conexão do cliente, imprime as mensagens recebidas e reenvia para o cliente.
while True:
	con, cliente = serv_socket.accept()
	print ("#=> Cliente Conectado com sucesso!")
	print ("#=> Aguardando Mensagens\n")
	while True:
		mensagem = con.recv (1024)
		mensagem_decode  = mensagem.decode()
		con.send(mensagem)
		if not mensagem:
			break
		print ('#=> Mensagem recebida =>', cliente, str(mensagem), '- Enviada de volta para o remetente')
	print ("\n\n#=> Finalizando Conexão")
	con.close()
	serv_socket.close()