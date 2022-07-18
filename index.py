# leitura da entrada de dados
def readEntry(entry):
    print("Iniciando leitura de dados...")
    print("Informe os dados a seguir:")
    aux = 's'
    while aux == 's':
        id = input("Informe o ID:")
        name = input("Informe o Nome:")
        salary = float(input("Informe o Salário:"))
        entry.append({"id":id, "nome":name, "salario":salary})
        aux = input("Deseja informar mais dados?[s/n]")
# detecção de salarios errados
def createReport(entry1, entry2):
    wrongSalaries = []
    total1 = 0
    total2 = 0
    dif = 0
    average = 0
    if(len(entry1) == len(entry2)):
        for i in range(0,len(entry1)):
            # verifica quais salarios estão incorretos
            print(i)
            if(entry1[i]["salario"] != entry2[i]["salario"]):
                wrongSalaries.append({"id": entry1[i]["id"], "nome": entry1[i]["nome"], "salario": entry1[i]["salario"], "correto": entry2[i]["salario"]})
            #diferença entre a entrada e os dados  da empresa 
            total1 += entry1[i]["salario"]
            total2 += entry2[i]["salario"]
            # calculo da média
        dif = total1-total2
        average = dif/(i+1)
        print("\033[0;49;97m--"*20, "relatório", "--"*20)
        print("Funcionários com salários errados: ")
        for wrong in wrongSalaries:
            print(f"[ID]: {wrong['id']}","__"*5, f"[NOME]: {wrong['nome']}","__"*5, f"[SALARIO]: {wrong['salario']}", "__"*5, f"[SALARIO CORRETO]: {wrong['correto']}","__"*5, f"[DIFERENÇA]: {wrong['salario']-wrong['correto']}")
        print("\n\n")
        print("diferença total entre a folha de referencia e da empresa especializada:","__"*5, dif)
        print("diferença média entre a folha de referencia e da empresa especializada:","__"*5, average)
    else: 
        print("Erro, numero de dados da empresa difere do numero de dados de entrada")

# execução do programa
blue = '\033[0;49;34m'
green = '\033[0;49;32m'
entrada1= []
entrada2= []
print(f"{blue}--"*20,"Dados de entrada","--"*20)
readEntry(entrada1)
print("\n\n\n")
print(f"{green}--"*20,"Dados da empresa","--"*20)
readEntry(entrada2)
print("\n\n\n")
createReport(entrada1, entrada2)
