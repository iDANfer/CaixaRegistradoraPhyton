def totalapagar(codigoProduto, qtdComprada):
    if codigoProduto == 0:
        return 0
    elif codigoProduto == 1:
        return qtdComprada * 0.5
    elif codigoProduto == 2:
        return qtdComprada * 1.00
    elif codigoProduto == 3:
        return qtdComprada * 4.00
    elif codigoProduto == 5:
        return qtdComprada * 7.00
    elif codigoProduto == 9:
        return qtdComprada * 8.00
    else:
        return -1

while True:

    print("Tabela de Produtos:")
    print("Código 1 - Produto A - R$0.50")
    print("Código 2 - Produto B - R$1.00")
    print("Código 3 - Produto C - R$4.00")
    print("Código 5 - Produto D - R$7.00")
    print("Código 9 - Produto E - R$8.00")
    print("Código 0 - Finalizar")

    codigoProduto = int(input("Informe o código do produto (ou 0 para sair): "))

    if codigoProduto == 0:
        print("Finalizando programa")
        break

    qtdComprada = int(input("Informe a quantidade desejada: "))
    precoTotal = totalapagar(codigoProduto, qtdComprada)

    if precoTotal >= 0:
        print("O preço do produto é R$:", precoTotal)
    else:
        print("Código inválido")
