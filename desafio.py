#Escreva um programa em Python que solicita ao usuário para digitar seu nome
# o valor do seu salário mensal
# valor do bônus que recebeu. 
# O programa deve, 
#O cálculo do KPI do bônus de 2024 é de 1000 + salario * bônus
#Finalmente, o programa deve imprimir uma mensagem no seguinte formato: "Olá [nome], o seu valor bônus foi de 5000".
# então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.

nome_usuario =input("Digite seu nome :")
salario_mensal = float(input("Digite o valor do seu salário mensal :"))
bonus = float(input("Digite o valor do bonus recebido :"))
constante_bonus = 1000
valor_do_bonus = constante_bonus+salario_mensal *bonus

print(f"O usuario: {nome_usuario}, possui o bonus de:{valor_do_bonus} ")

