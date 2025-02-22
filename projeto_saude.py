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
    print("|3-calcular imc do usuario{}|".format(" "*25))
    print("|4-dica do dia{}|".format(" "*37))
    print("|5-registrar treinos{}|".format(" "*31))
    print("|6-saida{} |".format("  "*21))
    print("+{}+".format("-"*50))
 
def calcularIMC():
    ...



print("{:^550}".format("SEJA BEM-VINDO"))
infoUser = {}

while True:
    verMenu()
    print("\n")
    opc = (input(f"{' ':^35}Digite a opção desejada: "))
    if opc =="1":
        print("\n")
        print("{}".format("="*50))
        print("{:^50}".format("Cadastro Usuario"))
        print("{}".format("="*50))

        nome = input("Nome: ")   
        dataNascimento = input("Data de Nascimento (DD/MM/AAAA): ")
        peso = float(input("Peso (kg): "))
        altura = float(input("Altura (m): "))
        infoUser = {'nome':nome,"data":dataNascimento,'peso':peso,'altura':altura}        
    elif opc == "2":
        print("{}".format("="*50))
        print("{:^50}".format("informacoes do Usurario"))
        print("{}".format("="*50))


        print(f"Nome: {nome}")
        print(f"Data de Nascimento: {dataNascimento}")
        print(f"Peso (kg): {peso:.2f}")
        print(f"Altura (m): {altura:.2f}")
    elif opc == "3":
        ...
    elif opc == "4":
        ...

    elif opc == "5":
        ...
    elif opc == "5":
        ...

   