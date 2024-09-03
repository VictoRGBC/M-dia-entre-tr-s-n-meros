# Desafio 04
numero_01 = 0.0
numero_02 = 0.0
numero_03 = 0.0

def ler_numeros():
    global numero_01
    global numero_02
    global numero_03
    
    numero_01 = float(input("Digite o 1° numero: "))
    numero_02 = float(input("Digite o 2° numero: "))
    numero_03 = float(input("Digite o 3° numero: "))
    
    print(f"Os números lidos são: {numero_01}, {numero_02} e {numero_03}")

def calcular_soma():
    global numero_01
    global numero_02
    global numero_03
    
    soma = numero_01 + numero_02 + numero_03
    print(f"A soma é: {round(soma, 2)}")
    return soma

def calcular_media():
    soma = calcular_soma()  # Usando a função calcular_soma para obter o valor da soma
    media = soma / 3
    print(f"A média é: {round(media, 2)}")
    return media

# Chamada das funções
ler_numeros()
calcular_soma()
calcular_media()
