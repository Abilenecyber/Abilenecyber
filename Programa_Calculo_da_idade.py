import datetime
# 1. Solicita o nome completo
nome = input("digite o seu nome completo:")
#2. Solicita o ano de nascimento
ano_nascimento = int(input("digite o seu ano de nascimento: "))
# 3. Obtém o ano atual dinamicamente e calcula a idade
ano_atual = datetime.date.today().year
idade = ano_atual - ano_nascimento
#4. Exibe a mensagem personalizada
print(f"\nOlá, {nome}! Você nasceu em {ano_nascimento} e atualmente tem {idade}")