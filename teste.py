import json

def cadastro():
    """Para cadastrar novos usuarios"""

    while True:
        nome = input("Digite seu nome: ")
        if nome.strip():  
            break
        else:
            print("Nome inválido. Certifique-se de inserir um nome válido.")
    
    while True: 
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0:
                break
            else:
                print("Idade inválida. Certifique-se de inserir um valor positivo.")
        except ValueError:
            print("Idade inválida. Certifique-se de inserir um valor numérico.")

    while True:
        cpf = input("Digite seu CPF (somente números): ")
        if cpf.isdigit() and len(cpf) == 11:
            break
        else:
            print("CPF inválido. Certifique-se de inserir apenas números e ter 11 dígitos.")

    while True:
        try:
            altura = float(input("Digite sua altura (em metros, exemplo: 1.8): "))
            if altura > 0:
                break
            else:
                print("Altura inválida. Certifique-se de inserir um valor positivo.")
        except ValueError:
            print("Altura inválida. Certifique-se de inserir um valor numérico.")

    while True:
        try:
            peso = float(input("Digite seu peso (em quilogramas): "))
            if peso > 0:
                break
            else:
                print("Peso inválido. Certifique-se de inserir um valor positivo.")
        except ValueError:
            print("Peso inválido. Certifique-se de inserir um valor numérico.")
    
    tempo_atividade = int(input("Digite o tempo de atividade física por semana (em minutos): "))

    usuario = {
        'nome': nome,
        'idade': idade,
        'cpf': cpf,
        'altura': altura,
        'peso': peso,
        'tempo_atividade': tempo_atividade,
    }

    try:
        with open('dados.txt', 'r') as arquivo:
            conteudo_existente = arquivo.read()
    except FileNotFoundError:
        conteudo_existente = ""

    with open('dados.txt', 'w') as arquivo:
        dados_existentes = json.loads(conteudo_existente) if conteudo_existente else []

        dados_existentes.append(usuario)

        arquivo.write(json.dumps(dados_existentes, indent=2, ensure_ascii=False).replace("'", '"'))

def login():
    """Realiza o login para resgatar os dados dos usuarios"""

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

def dados():
    """Exibe os dados do usuario"""

    usuario = login()  # Login do usuário
    
    if usuario is not None:
        print("\nDados do Usuário:")
        print(f"Nome: {usuario['nome']}")
        print(f"Idade: {usuario['idade']}")
        print(f"CPF: {usuario['cpf']}")
        print(f"Altura: {usuario['altura']} metros")
        print(f"Peso: {usuario['peso']} kg")
        print(f"Tempo de atividade física por semana: {usuario['tempo_atividade']} minutos")

def imc():
    """Calcula o IMC"""

    usuario = login() # Login do usuário
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

def sedentarismo():
    """Calcula o nível de sedentarismo"""

    usuario = login()  # Login do usuário
    if usuario is not None:
        tempo_atividade = usuario.get('tempo_atividade', 0)

        if tempo_atividade < 150:
            print(f'Nível de sedentarismo alto. Seu tempo de atividade física por semana é inferior a 150 minutos.')
        elif 150 <= tempo_atividade < 300:
            print(f'Nível de sedentarismo moderado. Seu tempo de atividade física por semana está entre 150 e 299 minutos.')
        else:
            print(f'Nível de sedentarismo baixo. Seu tempo de atividade física por semana é igual ou superior a 300 minutos.')

def sono(tempo_dormido):
    """Calcula o tempo de sono de um individuo"""
    tempo_desejado = 480 # Tempo de sono desejado em minutos

    if tempo_dormido >= tempo_desejado:
        print(f'Você atingiu a quantidade desejada de sono. Você dormiu {tempo_dormido//60} horas.')

    else:
        tempo_necessario = tempo_desejado - tempo_dormido
        print(f'Você não dormiu horas o bastante. Faltam {tempo_necessario} minutos para atingir a meta de 8 horas.')

while True:
    print("Escolha uma opção:\n 1 - Cadastro\n 2 - Exibir dados\n 3 - Calcular IMC\n 4 - Calcular nivel de sedentarismo\n 5 - Calcular tempo de sono\n 6 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        cadastro()

    elif opcao == 2:
        dados()

    elif opcao == 3:
        imc()

    elif opcao == 4:
        sedentarismo()

    elif opcao == 5:
        x = int(input("Digite o seu tempo de sono em minutos: "))
        sono(x)

    elif opcao ==6:
        break

    else:
        print("Opção inválida.")