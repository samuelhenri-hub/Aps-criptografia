# escolha do usuario
def menu():
    while True:
        print("\n------BEM VINDO AO PROGRAMA DE CRIPTOGRAFIA------\n")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair\n")
        try:
            opcao_User = int(input("SELECIONE A OPÇÃO DESEJADA"))
            if opcao_User == 1 or opcao_User == 2:
                return opcao_User
            elif opcao_User == 3:
                print("\nSaindo do programa...\n")
                print("\n------FIM DO PROGRAMA------\n")
                exit()
            else:
                print("\nOpção inválida. Tente novamente.\n")
                print("Escolha entre 1 a 3")
        except ValueError:
            print("\nEntrada inválida, digite um numero inteiro\n")

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
