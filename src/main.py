# escolha do usuario
print("\n------BEM VINDO AO PROGRAMA DE CRIPTOGRAFIA------\n")
print("SELECIONE A OPÇÃO DESEJADA")
opcao_user = int(input("1 - Criptografar\n2 - Descriptografar\n"))

# pedir mensagem e chave
mensagem = input("\nDigite a mensagem: ")
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

        elif opcao_user == 2:  # descriptografia
            nova_posicao = (posicao - chave) % 26

        nova_letra = chr(nova_posicao + ord('a'))
        mensagem_final += nova_letra
    else:
        mensagem_final += caractere  # mantém o caractere original

print("\nMensagem final:", mensagem_final, "\n")
print("------FIM DO PROGRAMA------\n")
