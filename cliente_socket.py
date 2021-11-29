# Fundamentos de Redes de Computadores
# Professor: Daniel Fireman
# ALUNO: Marcos Messias de Souza e Silva

import socket

# Configurações de servidor
host ='127.0.0.1'
port = 7000
destino = (host, port) #tupla de IP + Porta

# Variável booleana que identifica a conexão estabelecida
conectado = False

# Instancia o socket à variável
# AF_INET - Família do Protocolo e SOCK_STREAM indica o TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tenta realizar a conexão com o servidor
try:
	server_socket.connect(destino)
	print('Conexão estabeleciada com o servidor!')
	conectado = True
except:
 	print('Erro de conexão com o servidor!')

# Verifica se está conectado ao servidor
if conectado:

	# Imprime a mensagem inicial
	print ("""
	#####################################
	# Ecoador Tabajara - Marcos Messias #
	#                                   #
	#    Digite SAIR para finalizar     #
	#####################################\n""")

	# inicializa a variável de controle do loop
	mensagem = ''

	# Verifica se a variável de controle do loop possui o valor necessário para finalização do software
	while (mensagem != 'SAIR'):

		# Colhe a mensagem que deseja enviar para o servidor e envia como bytes
		print('#=> Envie a mensagem desejada para o servidor <=#')
		mensagem = input('Enviar => ')
		mensagem_byte = str.encode(mensagem)
		server_socket.send(mensagem_byte)

		# Recebe a resposta do servidor e imprime
		response = server_socket.recv(1024).decode()
		print('Resposta => ', response, '\n')

	# Finaliza a conexão
	server_socket.close()