#escolha do usuario
opcao_user = int(input("1 - Criptografar\n2 - Descriptografar\n"))

#pedir mensagem e chave
mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave: "))

#inicializar variavel da mensagem final
mensagem_final = ""

#percorrer cada caractere da mensagem
for caractere in mensagem:
    letra = caractere #letra original
    chave = 0 #quantidade de posicoes que a letra vai andar

    posicao = ord(letra) - ord('a') #achar a posicao da letra no alfabeto (0-25)
    nova_posicao = (posicao + chave) % 26 #aplica o deslocamento(para criptografar)
    nova_letra = chr(nova_posicao + ord('a')) #converte a nova posicao de volta para letra

    if opcao_user == 1:
        nova_posicao = (posicao + chave) %26 #aplica o deslocamento(para criptografar)
    elif opcao_user == 2:
        nova_posicao = (posicao - chave) %26 #aplica o deslocamento(para descriptografar)

    nova_posicao = nova_posicao + mensagem_final #adiciona a nova letra na mensagem final

else:
    letra += mensagem_final #adiciona a letra original na mensagem final

print("Mensagem final:", mensagem_final)