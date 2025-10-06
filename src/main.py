# Define a função menu que gerencia a interação inicial com o usuário.
def menu():
    # Inicia um loop infinito que só será quebrado por uma escolha válida do usuário.
    while True:
        # Imprime o cabeçalho de boas-vindas do programa.
        print("\n------BEM VINDO AO PROGRAMA DE CRIPTOGRAFIA------\n")
        # Mostra a opção para criptografar uma mensagem.
        print("1 - Criptografar")
        # Mostra a opção para descriptografar uma mensagem.
        print("2 - Descriptografar")
        # Mostra a opção para encerrar o programa.
        print("3 - Sair\n")
        # Inicia um bloco try para tratar possíveis erros de digitação do usuário.
        try:
            # Solicita ao usuário que digite a opção desejada e converte para um número inteiro.
            opcao_User = int(input("SELECIONE A OPÇÃO DESEJADA: "))
            # Verifica se a escolha do usuário é 1 (Criptografar) ou 2 (Descriptografar).
            if opcao_User == 1 or opcao_User == 2:
                # Se a opção for válida (1 ou 2), retorna o número da opção escolhida.
                return opcao_User
            # Verifica se a escolha do usuário é 3 (Sair).
            elif opcao_User == 3:
                # Informa ao usuário que o programa está sendo encerrado.
                print("\nSaindo do programa...")
                # Imprime uma mensagem de finalização.
                print("\n------FIM DO PROGRAMA------\n")
                # Encerra a execução do programa.
                exit()
            # Se a opção não for 1, 2 ou 3, executa este bloco.
            else:
                # Informa ao usuário que a opção digitada é inválida.
                print("\nOpção inválida. Tente novamente.\n")
                # Fornece uma instrução clara sobre as opções disponíveis.
                print("Escolha entre 1 a 3")
        # Captura o erro que ocorre se o usuário digitar algo que não pode ser convertido para inteiro.
        except ValueError:
            # Informa ao usuário que ele deve digitar um número inteiro.
            print("\nNumero inválido, digite um numero inteiro\n")

# Define a função que pede ao usuário a mensagem e a chave de criptografia.
def mensagem_chave():
    # Solicita a mensagem ao usuário e remove espaços em branco extras do início e do fim.
    mensagem = input("\nDigite a mensagem: ").strip()
    # Verifica se a string da mensagem está vazia.
    if not mensagem:
        # Informa ao usuário que a mensagem está vazia e precisa ser digitada novamente.
        print("\nA mensagem esta vazia, Tente novamente!!\n")
        # Chama a função novamente para que o usuário possa tentar de novo.
        return mensagem_chave()
    
    # Inicia um loop infinito para garantir que uma chave numérica válida seja inserida.
    while True:
        # Inicia um bloco try para tratar o erro de digitação da chave.
        try:
            # Solicita a chave ao usuário e a converte para um número inteiro.
            chave = int(input("Digite a chave: "))
            # Retorna a mensagem e a chave validadas.
            return mensagem, chave
        # Captura o erro se a entrada não puder ser convertida para um número inteiro.
        except ValueError:
            # Informa ao usuário que a chave deve ser um número inteiro.
            print("\nNumero inválido, digite um numero inteiro\n")

# Define a função que realiza a criptografia ou descriptografia.
def criptografia_descriptografia(mensagem, chave, opcao_user): # escolha do usuario
    # Inicializa uma string vazia para armazenar o resultado final.
    mensagem_final = ""
    
    # Itera sobre cada caractere da mensagem original.
    for caractere in mensagem:
        # Verifica se o caractere é uma letra do alfabeto.
        if caractere.isalpha():
            
            # Verifica se a letra é maiúscula e armazena o resultado (True ou False).
            maiscula = caractere.isupper()
            # Converte o caractere para minúsculo para padronizar o cálculo.
            letra = caractere.lower()
            # Calcula a posição da letra no alfabeto (0 para 'a', 1 para 'b', etc.).
            posicao = ord(letra) - ord('a')
            
            # Verifica se a opção escolhida foi 1 (Criptografar).
            if opcao_user == 1:
                # Calcula a nova posição deslocando para a frente (soma a chave).
                nova_posicao = (posicao + chave) % 26
                # Converte a nova posição de volta para uma letra.
                nova_letra = chr(nova_posicao + ord('a'))
            # Verifica se a opção escolhida foi 2 (Descriptografar).
            elif opcao_user == 2:
                # Calcula a nova posição deslocando para trás (subtrai a chave).
                nova_posicao = (posicao - chave) % 26
                # Converte a nova posição de volta para uma letra.
                nova_letra = chr(nova_posicao + ord('a'))
            # Se a letra original era maiúscula.
            if maiscula:
                # Converte a nova letra para maiúscula para manter o formato original.
                nova_letra = nova_letra.upper()
                
            # Adiciona a letra processada (criptografada ou descriptografada) à mensagem final.
            mensagem_final += nova_letra
        # Se o caractere não for uma letra (ex: número, espaço, pontuação).
        else:
            # Adiciona o caractere original à mensagem final sem modificá-lo.
            mensagem_final += caractere
    # Imprime o resultado final para o usuário.
    print("\nMensagem final:", mensagem_final, "\n")

# Garante que o código dentro deste bloco só será executado quando o script for rodado diretamente.
if __name__ == "__main__":
    # Inicia o loop principal do programa, que continua até o usuário decidir sair.
    while True:
        # Chama a função menu e armazena a opção do usuário na variável 'opcao'.
        opcao = menu()
        # Verifica se a opção é 1 (Criptografar) ou 2 (Descriptografar).
        if opcao in [1, 2]:
            # Chama a função para obter a mensagem e a chave do usuário.
            mensagem, chave = mensagem_chave()
            # Chama a função principal para executar a criptografia ou descriptografia com os dados fornecidos.
            criptografia_descriptografia(mensagem, chave, opcao)
