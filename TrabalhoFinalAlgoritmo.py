# FUNÇÕES
# Mostrar as opções do cardápio
def exibir_cardapio():
    print(" CARDÁPIO ")
    print("1 - Cachorro-Quente : R$ 12.00")
    print("2 - X-Burguer       : R$ 18.00")
    print("3 - X-Salada        : R$ 20.00")
    print("4 - Batata Frita    : R$ 15.00")
    print("5 - Refrigerante    : R$ 6.00")

# Calcular o desconto
def calcular_desconto(total_compra):
    if total_compra < 50.00:
        percentual = 0
        valor_desconto = 0.0
    elif total_compra <= 99.99:
        percentual = 5
        valor_desconto = total_compra * 0.05
    else:  # Para R$ 100.00 ou mais
        percentual = 10
        valor_desconto = total_compra * 0.10

    valor_final = total_compra - valor_desconto
    return percentual, valor_desconto, valor_final


# Forma de Pagamento
def obter_forma_pagamento():
    opcao_valida = False
    forma = ""


    while not opcao_valida:
        print(" FORMA DE PAGAMENTO ")
        print("1 - Dinheiro")
        print("2 - PIX")
        print("3 - Cartão")
        opcao = int(input("Escolha a forma de pagamento (1 a 3): "))

        if opcao == 1:
            forma = "Dinheiro"
            opcao_valida = True
        elif opcao == 2:
            forma = "PIX"
            opcao_valida = True
        elif opcao == 3:
            forma = "Cartão"
            opcao_valida = True
        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

    return forma


# Exibir o resumo da compra
def exibir_resumo(nome, total_compra, percentual, valor_desconto, valor_final, forma_pagamento):
    print("       RESUMO DO PEDIDO       ")
    print("Cliente:", nome)
    print("Valor Original da Compra: R$", total_compra)
    print("Desconto Aplicado:", percentual, "%")
    print("Valor do Desconto: R$", valor_desconto)
    print("Valor Final a Pagar: R$", valor_final)
    print("Forma de Pagamento:", forma_pagamento)
    print("Atendimento finalizado com sucesso!")


# PROGRAMA PRINCIPAL
# Perguntar o nome do cliente
nome = input("Digite o nome do cliente: ")

# O subtotal e o total da compra começa zerado
subtotal = 0.0
total_compra = 0.0
continuar = "s"

# Para escolher os produtos, o cliente deve informar o código e a quantidade
while continuar.lower() == "s":
    exibir_cardapio()
    codigo = int(input("Digite o número do produto (1 a 5): "))
    quantidade = int(input("Digite a quantidade: "))

    # Identifica o produto, calcula o subtotal e soma no total
    if codigo == 1:
        subtotal = 12.00 * quantidade
        total_compra = total_compra + subtotal
        print("Adicionado: Cachorro-Quente | Subtotal: R$", subtotal)
    elif codigo == 2:
        subtotal = 18.00 * quantidade
        total_compra = total_compra + subtotal
        print("Adicionado: X-Burguer | Subtotal: R$", subtotal)
    elif codigo == 3:
        subtotal = 20.00 * quantidade
        total_compra = total_compra + subtotal
        print("Adicionado: X-Salada | Subtotal: R$", subtotal)
    elif codigo == 4:
        subtotal = 15.00 * quantidade
        total_compra = total_compra + subtotal
        print("Adicionado: Batata Frita | Subtotal: R$", subtotal)
    elif codigo == 5:
        subtotal = 6.00 * quantidade
        total_compra = total_compra + subtotal
        print("Adicionado: Refrigerante | Subtotal: R$", subtotal)
    else:
        print("Opção inválida! Nenhum valor foi adicionado.")

    # Perguntar se deseja continuar comprando após cada produto adicionado
    continuar = input("Deseja adicionar mais algum produto? (s/n): ")

# Após encerrar o laço com 'n':

# Calcular o desconto
percentual, valor_desconto, valor_final = calcular_desconto(total_compra)

# Solicitar a forma de pagamento
forma_pagamento = obter_forma_pagamento()

# Apresentar o resumo final
exibir_resumo(nome, total_compra, percentual, valor_desconto, valor_final, forma_pagamento)