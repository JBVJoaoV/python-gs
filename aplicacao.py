import json

def cadastro():
    """Para cadastrar novos usuarios"""
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = int(input("Digite seu CPF (somente numeros): "))
    altura = float(input("Digite sua altura (em metros, exemplo: 1.8): "))
    peso = float(input("Digite seu peso (em quilogramas): "))
    tempo_atividade = int(input("Digite o tempo de atividade física por semana (em minutos): "))
    tempo_sono = int(input("Digite o tempo de sono por dia: "))

    usuario = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'altura': altura,
        'peso': peso,
        'tempo_atividade': tempo_atividade,
        'tempo_sono': tempo_sono
    }

    try:
        with open('acesso.txt', 'r') as arquivo:
            conteudo_existente = arquivo.read()
    except FileNotFoundError:
        conteudo_existente = ""

    with open('acesso.txt', 'w') as arquivo:
        dados_existentes = json.loads(conteudo_existente) if conteudo_existente else []

        dados_existentes.append(usuario)

        arquivo.write(json.dumps(dados_existentes, indent=2))

def dados ():
    """Exibe os dados do usuario"""

def IMC (altura, peso):
    """Calcula o IMC"""
    imc = peso / (altura**2)
    
    if imc <= 16 :
        print (f'Desnutrição, seu IMC é: {imc}')

    elif imc >= 16.1 and imc <= 18.4:
        print (f'Magreza, seu IMC é: {imc}')

    elif imc >= 18.5 and imc <= 24.9:
        print (f'Peso normal para a altura, seu IMC é: {imc}')

    elif imc >= 25 and imc <= 29.9:
        print (f'Sobrepeso, seu IMC é: {imc}')

    elif imc >= 30 and imc <= 39.9:
        print(f'Obesidade, seu IMC é: {imc}')
    
    else:
        print(f'Obesidade morbida, seu IMC é: {imc}')

def sedentarismo ():
    """Calcula o nivel de sedentarismo"""

def sair():
    return False

while True:
    print ("Escolha uma opção:\n 1 - Cadastro\n 2 - Exibir dados\n 3 - Calcular IMC\n 4 - Calcular nivel de sedentarismo\n 5 - Sair")
    opcao = int(input("Opção: "))

    match opcao:
        case 1: 
            cadastro()

        case 2:
            dados()

        case 3:
            IMC()

        case 4:
            sedentarismo()

        case 5:
            sair()
        
        case _:
            print("Opção inválida.")