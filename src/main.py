# escolha do usuario
opcao_user = int(input("1 - Criptografar\n2 - Descriptografar\n"))

# pedir mensagem e chave
mensagem = input("Digite a mensagem: ")
chave = int(input("Digite a chave: ")) #numero de posicoes para deslocar

# inicializar variavel da mensagem final
mensagem_final = ""

# percorrer cada caractere da mensagem
for caractere in mensagem:
    if caractere.isalpha():  # verifica se o caractere é uma letra
        letra = caractere.lower()
        posicao = ord(letra) - ord('a')

        if opcao_user == 1:  # criptografar
            nova_posicao = (posicao + chave) % 26
        elif opcao_user == 2:  # descriptografar
            nova_posicao = (posicao - chave) % 26

        nova_letra = chr(nova_posicao + ord('a'))
        mensagem_final += nova_letra
    else:
        mensagem_final += caractere  # mantém o caractere original

print("Mensagem final:", mensagem_final)
