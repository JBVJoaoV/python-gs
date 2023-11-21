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
        with open('dados.txt', 'r') as arquivo:
            conteudo_existente = arquivo.read()
    except FileNotFoundError:
        conteudo_existente = ""

    with open('dados.txt', 'w') as arquivo:
        dados_existentes = json.loads(conteudo_existente) if conteudo_existente else []

        dados_existentes.append(usuario)

        arquivo.write(json.dumps(dados_existentes, indent=2))

def login():
    nome_usuario = input("Digite o nome do usuário: ")

    try:
        with open('dados.txt', 'r') as arquivo:
            conteudo = arquivo.read()
    except FileNotFoundError:
        print("Arquivo 'dados.txt' não encontrado.")
        return None

    dados_usuarios = json.loads(conteudo) if conteudo else []
    usuario_encontrado = None

    for usuario in dados_usuarios:
        if usuario['nome'] == nome_usuario:
            usuario_encontrado = usuario
            break

    if usuario_encontrado:
        print(f"Bem-vindo, {nome_usuario}!")
        return usuario_encontrado
    else:
        print(f"Usuário {nome_usuario} não encontrado.")
        return None

def dados ():
    """Exibe os dados do usuario"""

def IMC ():
    """Calcula o IMC"""
    # Login do usuário
    usuario = login()
    if usuario is None:
        return

    altura = float(usuario.get('altura', 0))
    peso = float(usuario.get('peso', 0))

    imc = peso / (altura ** 2)

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
    print("Escolha uma opção:\n 1 - Cadastro\n 2 - Exibir dados\n 3 - Calcular IMC\n 4 - Calcular nivel de sedentarismo\n 5 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastro()
    elif opcao == 2:
        dados()
    elif opcao == 3:
        IMC()
    elif opcao == 4:
        sedentarismo()
    elif opcao == 5:
        if not sair():
            break  # Interrompe o loop se sair() retornar False
    else:
        print("Opção inválida.")