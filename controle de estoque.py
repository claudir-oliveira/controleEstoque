listProdutos = ["Computador", "Carregador", "Celular", "Controle"]
listPrecos = {"Computador": 1525.34, "Carregador": 57.00, "Celular":734.99, "Controle": 39.20}#"Computador", "Carregador", "Celular", "Controle", ]
listQtd = {"Computador": 125, "Carregador": 75, "Celular":18, "Controle": 24}
cod = 0
acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n Digite o código de sua escolha: "))

def consultaProdutos(cod):
    for item in listProdutos:
        cod = cod + 1
        print(str(cod) + " - " + item)
    continua = int(input("Você deseja continuar no sistema? (1 / 0)?"))
    if continua == 1:
        iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n Digite o código de sua escolha: ")))
    else:
        pass
def consultaPreco():
    codProduto = int(input("Qual produto deseja consultar? "))-1
    nomeProduto = listProdutos[codProduto]
    print("O preço de " + nomeProduto + " é  de R$" + str(listPrecos[listProdutos[codProduto]]))
    continua = int(input("Você deseja continuar no sistema? (1 / 0)?"))
    if continua == 1:
        iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n Digite o código de sua escolha: ")))
    else:
        pass
def consultaEstoque():
    codProduto = int(input("Qual produto deseja consultar? "))-1
    nomeProduto = listProdutos[codProduto]
    print("Temos " + str(listQtd[listProdutos[codProduto]]) + " " + nomeProduto + " em estoque.")
    continua = int(input("Você deseja continuar no sistema? (1 / 0)?"))
    if continua == 1:
        iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n Digite o código de sua escolha: ")))
    else:
        pass
def iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n Digite o código de sua escolha: "))):
    if acao == 1:
        consultaProdutos(cod)
    elif acao == 2:
        consultaPreco()
    elif acao == 3:
        consultaEstoque()

iniciaSistema(acao)