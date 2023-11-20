#def cadastro ():

#def login ():

#def dados ():

def IMC (altura, peso):
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

#def sedentarismo ():


x = 1 # Variavel para loop do menu

while x == 1:
    print ("Escolha uma opção:")
    print ("1 - Cadastro")
    print ("2 - Login")
    print ("3 - Exibir dados")
    print ("4 - Calcular IMC")
    print ("5 - Calcular nivel de sedentarismo")


"""
    match 6:
        case 1:
            cadastro()

        case 2:
            login() 

        case 3:
            dados()

        case 4:
            IMC()

        case 5:
            sedentarismo()

        case 6:
            
"""