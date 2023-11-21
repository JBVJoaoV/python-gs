import json

def cadastro():
    # Solicitando informações ao usuário
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    cpf = int(input("Digite seu CPF (somente numeros): "))
    altura = float(input("Digite sua altura (em metros): "))
    peso = float(input("Digite seu peso (em quilogramas): "))
    tempo_atividade = int(input("Digite o tempo de atividade física por semana (em minutos): "))
    tempo_sono = int(input("Digite o tempo de sono por dia: "))

    # Criando um dicionário com as informações
    usuario = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'altura': altura,
        'peso': peso,
        'tempo_atividade': tempo_atividade,
        'tempo_sono': tempo_sono
    }

    # Lendo o arquivo existente
    try:
        with open('dados.txt', 'r') as arquivo:
            conteudo_existente = arquivo.read()
    except FileNotFoundError:
        conteudo_existente = ""

    # Adicionando o novo cadastro ao arquivo
    with open('dados.txt', 'w') as arquivo:
        # Carregando dados existentes como uma lista de dicionários
        dados_existentes = json.loads(conteudo_existente) if conteudo_existente else []

        # Adicionando o novo usuário à lista
        dados_existentes.append(usuario)

        # Escrevendo a lista de dicionários formatada como JSON no arquivo
        arquivo.write(json.dumps(dados_existentes, indent=2))

def calcular_imc():
    altura = usuario['altura']
    peso = usuario['peso']
    imc = peso / (altura ** 2)

    if imc <= 16:
        print(f'Desnutrição, seu IMC é: {imc}')
    elif 16.1 <= imc <= 18.4:
        print(f'Magreza, seu IMC é: {imc}')
    elif 18.5 <= imc <= 24.9:
        print(f'Peso normal para a altura, seu IMC é: {imc}')
    elif 25 <= imc <= 29.9:
        print(f'Sobrepeso, seu IMC é: {imc}')
    elif 30 <= imc <= 39.9:
        print(f'Obesidade, seu IMC é: {imc}')
    else:
        print(f'Obesidade mórbida, seu IMC é: {imc}')

calcular_imc()

