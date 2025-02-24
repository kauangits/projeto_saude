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
    print("|5-dicas nutricionais{}|".format(" "*31))
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
        idade = int(input("Idade: "))
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
                    
                    #Opçao do calculo IMC (Indice de Massa Corporal)
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

                        #Opçao das dicas nutricionais.
        
    elif opc == "5":
        def exibir_tabela():
            print("                                 DICAS NUTRICIONAIS DO DIA À DIA SAUDÁVEL.")
            print("="*113)
            print("  >  Antes de começarmos, selecione uma categoria. Você poderá escolher se quer continuar ou não.")
            print("="*113)
            print("   >  a =  Dicas de Alimentação Saudável")
            print("   >  b =  Dicas de Bebidas e Hidratação")
            print("   >  g =  Dicas para Ganho de Peso")
            print("   >  p =  Dicas para Perda de Peso")
            print("   >  h =  Dicas de Hábitos e Rotina Nutricional")
            print("   >  e =  Para Encerrar as Dicas")
            print("="*113)

        dicas = {
            "a": [ "                      >      Dicas de Alimentação Saudável",
                "Prefira alimentos naturais – Frutas, verduras, legumes e proteínas magras devem ser a base da alimentação.",
                "Inclua fontes de fibras – Como aveia, chia, linhaça e grãos para melhorar a digestão.",
                "Evite frituras e excesso de óleos – Prefira alimentos assados, grelhados ou cozidos no vapor.",
                "Reduza o consumo de açúcar – Opte por adoçantes naturais como mel ou frutas.",
                "Beba bastante água – A hidratação é fundamental para o bom funcionamento do organismo."
            ],
            "b": ["                       >      Dicas de Bebidas e Hidratação",
                "Comece o dia com um copo de água para ativar o metabolismo.",
                "Evite refrigerantes e bebidas açucaradas – Opte por sucos naturais e chás.",
                "Beba pelo menos 2 litros de água por dia para manter o corpo hidratado.",
                "Consuma chás diuréticos, como chá-verde e hibisco, para auxiliar na digestão.",
                "Não exagere no café – O excesso de cafeína pode causar insônia e ansiedade."
            ],
            "g": ["                       >      Dicas para Ganho de Peso",
                "Aumente a ingestão calórica com alimentos saudáveis, como oleaginosas e abacate.",
                "Consuma proteínas em todas as refeições para ajudar no ganho de massa muscular.",
                "Faça refeições a cada 3 horas para manter um bom aporte calórico.",
                "Inclua shakes proteicos e vitaminas na sua dieta.",
                "Não pule o café da manhã – É uma refeição essencial para quem quer ganhar peso."
            ],
            "p": ["                       >      Dicas para Perda de Peso",
                "Pratique exercícios aeróbicos regularmente para queimar gordura.",
                "Diminua o consumo de carboidratos refinados, como pão branco e massas.",
                "Aumente a ingestão de proteínas para preservar a massa muscular.",
                "Evite beliscar entre as refeições – Planeje lanches saudáveis.",
                "Durma bem – O sono é essencial para o controle do metabolismo."
            ],
            "h": ["                       >      Dicas de Hábitos e Rotina nutricional",
                "Mantenha um horário regular para as refeições.",
                "Evite comer em frente à TV ou celular – Foque na mastigação.",
                "Planeje suas refeições da semana para evitar escolhas ruins.",
                "Diminua o consumo de ultraprocessados e fast food.",
                "Crie o hábito de ler os rótulos dos alimentos antes de comprar."
            ]
        }

        def exibir_dicas(categoria):
            for dica in dicas[categoria]:
                print("="*113)
                print(dica)
                print("="*113)
                continuar = input("Quer a próxima dica? (s/n) ->  ")
                if continuar != "s":
                    return  

        while True:
            exibir_tabela()
            opcao_dica_nutricional = input("Escolha uma categoria ->  ")
            
            if opcao_dica_nutricional in dicas:
                exibir_dicas(opcao_dica_nutricional)
            elif opcao_dica_nutricional == "e":
                print("Obrigado por utilizar nossas dicas nutricionais! Até logo!")
                break
                print("")
            else:
                print("Opção inválida! Escolha novamente.")
        
                print("")
            
            #Opção de Encerrar programa e Agradecimento
        
    elif opc == "6":
        print("{:^550}".format("OBRIGADO PELA PREFERENCIA"))
        break
    elif opc not in ['1','2','3','4','5','6']:
        print("\n")
        print("{}".format("="*52))
        print("{:^50}".format("Digito Invalido"))
        print("{}".format("="*52))
          
           
             
            


