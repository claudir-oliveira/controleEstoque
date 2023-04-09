listProdutos = ["Computador", "Carregador", "Celular", "Controle"]
listPrecos = {"Computador": 1525.34, "Carregador": 57.00, "Celular":734.99, "Controle": 39.20}#"Computador", "Carregador", "Celular", "Controle", ]
listQtd = {"Computador": 125, "Carregador": 75, "Celular":18, "Controle": 24}
cod = 0
#acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n Digite o código de sua escolha: "))

def consultaProdutos(cod):
    for item in listProdutos:
        cod = cod + 1
        print(str(cod) + " - " + item)
    continua = input("Você deseja continuar no sistema? (S/N)? ")
    if continua.upper() == "S":
        iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n 4 - Efetuar Venda \n 5 - Cadastrar novo Produto \n Digite o código de sua escolha: ")))
    else:
        pass
def consultaPreco():
    codProduto = int(input("Qual produto deseja consultar? "))-1
    nomeProduto = listProdutos[codProduto]
    print("O preço de " + nomeProduto + " é  de R$" + str(listPrecos[listProdutos[codProduto]]))
    continua = input("Você deseja continuar no sistema? (S/N)?")
    if continua.upper() == "S":
        iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n 4 - Efetuar Venda \n 5 - Cadastrar novo Produto \n Digite o código de sua escolha: ")))
    else:
        pass
def consultaEstoque():
    codProduto = int(input("Qual produto deseja consultar? "))-1
    nomeProduto = listProdutos[codProduto]
    print("Temos " + str(listQtd[listProdutos[codProduto]]) + " " + nomeProduto + " em estoque.")
    continua = input("Você deseja continuar no sistema? (S/N)?")
    if continua.upper() == "S":
        iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n 4 - Efetuar Venda \n 5 - Cadastrar novo Produto \n Digite o código de sua escolha: ")))
    else:
        pass
def iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n 4 - Efetuar Venda \n 5 - Cadastrar novo Produto \n Digite o código de sua escolha: "))):
    if acao == 1:
        consultaProdutos(cod)
    elif acao == 2:
        consultaPreco()
    elif acao == 3:
        consultaEstoque()
    elif acao == 4:
        efetuaVenda()
    elif acao == 5:
        cadastraProduto()
def efetuaVenda():
    codProduto = int(input("Qual o código do produto vendido? ")) -1
    nomeProduto = listProdutos[codProduto]
    precoProduto = float(listPrecos[listProdutos[codProduto]])
    estoqueProduto = listQtd[listProdutos[codProduto]]
    qtdProduto = int(input("Qual a quantidade vendida? "))
    totalVenda = float(int(qtdProduto) * float(precoProduto))
    if qtdProduto > estoqueProduto:
        print("A quantidade solicitada é maior que o estoque! \nPreencha novamente as informações.")
        efetuaVenda()
    else:
        print(f"O valor total da venda é de R${totalVenda} \n")
        finalizaVenda = input("Você deseja finalizar a venda? (S/N) ")
        if finalizaVenda.upper() == "S":
            listQtd[nomeProduto] = estoqueProduto - qtdProduto
            print("Venda finalizada com sucesso!")
            iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n 4 - Efetuar Venda \n 5 - Cadastrar novo Produto \n Digite o código de sua escolha: ")))
        else:
            print("Venda não finalizada!")
            efetuaVenda()
def cadastraProduto():
    novoProduto = input("Qual o nome do produto?")
    precoNovoproduto = float(input("Qual o preço de venda do produto?"))
    qtdNovoproduto = int(input("Qual a quantidade do produto?"))
    listProdutos.append(novoProduto)
    listPrecos[novoProduto] = precoNovoproduto
    listQtd[novoProduto] = qtdNovoproduto
    iniciaSistema(acao = int(input("Qual ação você quer executar?\n\n 1 - Consultar Catálogo de Produtos \n 2 - Consultar Preços \n 3 - Cosultar Estoque \n 4 - Efetuar Venda \n 5 - Cadastrar novo Produto \n Digite o código de sua escolha: ")))

iniciaSistema()