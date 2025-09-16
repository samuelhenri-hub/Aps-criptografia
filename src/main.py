#importando biblioteca string
import string

#MENU PARA ESCOLHA DO USARIO
print("------CRIPTOGRAFIA------\n")
opcaoUser = int(input(" 1 - Criptografar\n 2 - Descriptografar\n 3 - Sair \n"))
#lista de caracteres valídos
letra = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
#variavel para a mensagem descriptografado
mensagemDescriptografada = ""