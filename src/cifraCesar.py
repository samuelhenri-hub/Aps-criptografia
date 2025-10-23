def menu():
    while True:
        print("\n------BEM VINDO AO PROGRAMA DE CRIPTOGRAFIA------\n")
        print("1 - Criptografar")
        print("2 - Descriptografar")
        print("3 - Sair\n")
        try:
            opcao_User = int(input("SELECIONE A OPÇÃO DESEJADA: "))
            if opcao_User == 1 or opcao_User == 2:
                return opcao_User
            elif opcao_User == 3:
                print("\nSaindo do programa...")
                print("\n------FIM DO PROGRAMA------\n")
                exit()
            else:
                print("\nOpção inválida. Tente novamente.\n")
                print("Escolha entre 1 a 3")
        except ValueError:
            print("\nNumero inválido, digite um numero inteiro\n")

def mensagem_chave():
    mensagem = input("\nDigite a mensagem: ").strip()
    if not mensagem:
        print("\nA mensagem esta vazia, Tente novamente!!\n")
        return mensagem_chave()
    
    while True:
        try:
            chave = int(input("Digite a chave: "))
            return mensagem, chave
        except ValueError:
            print("\nNumero inválido, digite um numero inteiro\n")

def criptografia_descriptografia(mensagem, chave, opcao_user):
    mensagem_final = ""
    
    for caractere in mensagem:
        if caractere.isalpha():
            
            maiscula = caractere.isupper()
            letra = caractere.lower()
            posicao = ord(letra) - ord('a')
            
            if opcao_user == 1:
                nova_posicao = (posicao + chave) % 26
                nova_letra = chr(nova_posicao + ord('a'))
            elif opcao_user == 2:
                nova_posicao = (posicao - chave) % 26
                nova_letra = chr(nova_posicao + ord('a'))
            if maiscula:
                nova_letra = nova_letra.upper()
                
            mensagem_final += nova_letra
        else:
            mensagem_final += caractere
    print("\nMensagem final:", mensagem_final, "\n")

if __name__ == "__main__":
    while True:
        opcao = menu()
        if opcao in [1, 2]:
            mensagem, chave = mensagem_chave()
            criptografia_descriptografia(mensagem, chave, opcao)
