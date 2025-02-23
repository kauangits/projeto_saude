# criar conta de usuario
# mostrar conta do usuario
# calcular imc do usuario
# dica do dia 
# registrar treinos
# saida



def verMenu():
        
    print("+{}+".format("-"*50))
    print("|{:^50}|".format("Menu Principal"))
    print("+{}+".format("-"*50))
    print("|1-criar conta de usuario{}|".format(" "*26))
    print("|2-mostrar conta do usuario{}|".format(" "*24))
    print("|3-calcular macromutrientes{}|".format(" "*25))
    print("|4-calculo imc do usuario{}|".format(" "*25))
    print("|5-registrar treinos{}|".format(" "*31))
    print("|6-saida{} |".format("  "*21))
    print("+{}+".format("-"*50))
 

def calcularIMC(peso,altura):
    return peso/(altura**2)
    



print("{:^550}".format("SEJA BEM-VINDO"))
infoUser = {}


while True:
    verMenu()
    print("\n")
    opc = ((input(f"{' ':^13}Digite a opção desejada: ")))
    if opc =="1":
        print("\n")
        print("{}".format("="*50))
        print("{:^50}".format("Cadastro Usuario"))
        print("{}".format("="*50))

        nome = input("Nome: ")   
        idade = input("Idade: ")
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        sexo = input("Digite o seu sexo('h'= Homem/'m'= Mulher)  ->     ").lower()
        infoUser = {'nome':nome,"data":idade,'peso':peso,'altura':altura,'sexo':sexo}        
    elif opc == "2":
        print("{}".format("="*50))
        print("{:^50}".format("informacoes do Usurario"))
        print("{}".format("="*50))


        print(f"Nome: {nome}")
        print(f"Data de Nascimento: {idade}")
        print(f"Peso (kg): {peso:.2f}")
        print(f"Altura (m): {altura:.2f}")
    elif opc == "3":
        if not infoUser:  # Se infoUser estiver vazio, o usuário ainda não cadastrou nada
            print("Cadastre-se antes desse passo")
        else:

            altura = float(input("Digite sua altura   ->     "))

            print("")

            print("|=================================================================================|")
            print("|   Nivel       |   classificação   |     Tempo de exercicio (Semanais)           |")
            print("|_________________________________________________________________________________|")
            print("|  -> Nivel 1   |   Sedentario      |        <150 minutos semanais                |")
            print("|_________________________________________________________________________________|")
            print("|  -> Nivel 2   |   Pouco Ativo     |        Entre 150 e 300 minutos semanais     |")
            print("|_________________________________________________________________________________|")
            print("|  -> Nivel 3   |   Muito ativo     |        >300 minutos semanais                |")
            print("|=================================================================================|")

            print("")

            print("Digite o numero 1, 2 ou 3")
            nivel_Sedentarismo = input("Diga Qual seu nivel de sedentarismo  ->     ")

            print("")

            print("1 => Manter")
            print("2 => Perder Peso")
            print("3 => Ganhar Peso")

            print("Digite o numero 1, 2 ou 3")
            objetivo = float(input("Qual seu objetivo   ->    "))

        # Calculo de metabolismo basal
            #calculo para homem 
            if sexo == "h":
                bmr = (10 * (peso) + 6.25 * (altura) - 5 * (idade) + 5)
            #Calculo para mulher
            elif sexo == "m":
                bmr = (10 * (peso) + 6.25 * (altura) - 5 * idade - 161)

        # Calculo do gasto calorico total diario (TDEE)
            if nivel_Sedentarismo == "1":
                tdee = (bmr * 1.2)
            elif nivel_Sedentarismo == "2":
                tdee = (bmr * 1.375)
            elif nivel_Sedentarismo == "3":
                tdee = (bmr * 1.55)


        #Calculo para distribuiçao de macronutrientes de acordo com o objetivo

            percentual_proteina = 0
            percentual_carboidrato = 0
            percentual_gordura = 0

            if objetivo ==1:
                percentual_proteina = 0.25
                percentual_carboidrato = 0.50
                percentual_gordura = 0.25
            elif objetivo ==2:
                percentual_proteina = 0.30
                percentual_carboidrato = 0.40
                percentual_gordura = 0.30
            elif objetivo ==3:
                percentual_proteina =0.30
                percentual_carboidrato =0.50
                percentual_gordura = 0.20
            else:
                print("Objetivo invalido ERROr:")
            
        #Calculadora de de calorias para cada macronutrientes
            calorias_proteinas = ( tdee * percentual_proteina )
            calorias_carboidratos = ( tdee * percentual_carboidrato)
            calorias_gorduras = ( tdee * percentual_gordura)

        #Converter calorias para gramas.

            gramas_proteina = (calorias_proteinas /4)
            gramas_carboidratos = (calorias_carboidratos /4)
            gramas_gordura = (calorias_gorduras /9)

            if objetivo ==1:
                print("A distribuição de macronutrientes diario para o seu objetivo de manter o peso é:")
                print("")
                print("Proteinas:    gramas {:.2f}, calorias {:.0f}".format(gramas_proteina,calorias_proteinas))
                print("Carboidratos: gramas {:.2f}, calorias {:.0f}".format(gramas_carboidratos,calorias_carboidratos))
                print("Gordura:      gramas {:.2f}, calorias {:.0f}".format(gramas_gordura,calorias_gorduras))
                print("")
            elif objetivo ==2:
                print("A distribuição de macronutrientes diario para o seu objetivo de perder peso é:")
                print("")
                print("Proteinas:    gramas {:.2f}, calorias {:.0f}".format(gramas_proteina,calorias_proteinas))
                print("Carboidratos: gramas {:.2f}, calorias {:.0f}".format(gramas_carboidratos,calorias_carboidratos))
                print("Gordura:      gramas {:.2f}, calorias {:.0f}".format(gramas_gordura,calorias_gorduras))
                print("")
            elif objetivo ==3:
                print("A distribuição de macronutrientes diario para o seu objetivo de ganhar peso é:")
                print("")
                print("Proteinas:    gramas {:.2f}, calorias {:.0f}".format(gramas_proteina,calorias_proteinas))
                print("Carboidratos: gramas {:.2f}, calorias {:.0f}".format(gramas_carboidratos,calorias_carboidratos))
                print("Gordura:      gramas {:.2f}, calorias {:.0f}".format(gramas_gordura,calorias_gorduras))
                print("")
    elif opc == "4":
        imc = calcularIMC(peso,(altura))

        print(" ")

        print("    ->  {}, Seu Indice de Massa Corporal é   | {:.2f} |" .format(nome, imc))

        print("")

        if imc <16:
            print(f"    -> Atenção {nome}! Você está com magreza grave")
        elif  16<= imc < 17:
            print(f"    -> {nome} Você está com magreza moderada")
        elif  17<= imc <18.5:
            print(f"    ->  {nome} Você está com magreza leve")
        elif 18.5<= imc <25:
            print(f"    -> {nome} Que bom! Você está saudável")
        elif 25<= imc <30:
            print(f"    -> {nome} Você está com sobrepeso")
        elif 30<= imc <35:
            print(f"    -> ATENÇÃO {nome}! Você está com obesidade grau 1")
        elif 35<= imc <40:
            print(f"    -> ATENÇÃO {nome}! Você está com obesidade grau 2")
        elif imc >40:
            print(f"    -> ATENÇÃO {nome}! Você está com obesidade grau 3")

    elif opc == "5":
        ...
    elif opc == "6":
        print("{:^550}".format("OBRIGADO PELA PREFERENCIA"))
        break
    elif opc not in ['1','2','3','4','5','6']:
        print("\n")
        print("{}".format("="*52))
        print("{:^50}".format("Digito Invalido"))
        print("{}".format("="*52))
          
           
             
            


