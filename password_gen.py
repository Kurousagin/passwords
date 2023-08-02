import random
import string
#função para gerar senha
def password_gen(len_pass = 8):
    ascii_options = string.ascii_letters
    number_options = string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ""
#cria um array que começa de 0 até o valor de len_pass
    for i in range(0, len_pass):
        digit = random.choice(options)
        password_user = password_user + digit

    return password_user

choice_user = input("quantos digitos na senha?\n")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:
    print("Entrada Invalida!")
    quit()

response = password_gen(len_pass = choice_user)
print(f"senha gerada:\n{response}")