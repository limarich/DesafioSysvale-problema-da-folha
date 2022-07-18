entrada = [{"id": 1, "nome": "richard", "salario": 1200}, {
    "id": 2, "nome": "david", "salario": 1800}, {"id": 3, "nome": "bianca", "salario": 2500}]
dadosEmpresa = [{"id": 1, "nome": "richard", "salario": 2000}, {
    "id": 2, "nome": "david", "salario": 1500}, {"id": 3, "nome": "bianca", "salario": 2500}]
lenEntrada = len(entrada)
colaboradoresErrados = []
totalEntrada = 0
totalEmpresa = 0
difMedia = 0
# leitura da entrada de dados
def readEntry():
    print("Iniciando leitura de dados...")
    print("Informe os dados a seguir:")
    aux = 's'
    while aux == 's':
        id = input("Informe o ID:")
        name = input("Informe o Nome:")
        salary = float(input("Informe o Salário:"))
        aux = input("Deseja informar mais dados?[s/n]")

if(lenEntrada == len(dadosEmpresa)):
    for i in range(0, len(entrada)):
        if(entrada[i]["salario"] != dadosEmpresa[i]["salario"]):
            colaboradoresErrados.append(entrada[i])
        totalEntrada += entrada[i]["salario"]
        totalEmpresa += dadosEmpresa[i]["salario"]
        difMedia += (entrada[i]["salario"] - dadosEmpresa[i]["salario"])
# print(colaboradoresErrados)
# print(totalEntrada-totalEmpresa)
# print(difMedia/lenEntrada)
readEntry()
