#MENU PARA ESCOLHA DO USARIO
print("------CRIPTOGRAFIA------\n")
opcaoUser = int(input(" 1 - Criptografar\n 2 - Descriptografar\n 3 - Sair"))

#CRIPTOGRAFIA
if opcaoUser == 1:
    criptografia = string(input("Digite a mensagem que deseja ser criptografada: "))
    chave = int(input("Digite a chave de criptografia: "))
    mensagemCriptografada = ""
    #FALTA COMPLETAR A CRIPTOGRAFIA

#DESCRIPTOGRAFIA
elif opcaoUser == 2:
    chave = int(input("Digite a chave para descriptografar: "))
    print(f"A mensagem é: {mensagemDescriptografada}")
    #FALTA COMPLETAR A DESCRIPTOGRAFIA

#SAIR
elif opcaoUser == 3:
    print("------SAINDO DO PROGRAMA-----")
    exit()

#OPCAO INVALIDA
else: 
    print("OPÇÃO INVALIDA")
    retorno = int(input("Deseja voltar ao menu?\n 1 - sim 2 - não"))
    if retorno == 1:
        # Voltar ao menu
        opcaoUser = int(input(" 1 - Criptografar\n 2 - Descriptografar\n 3 - Sair"))
    else:
        exit()

