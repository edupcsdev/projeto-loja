import datetime, random

produtos_destaque = ["Arroz", "Feijão", "Café", "Leite", "Açúcar", "Óleo", "Macarrão", "Frango"]

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade   
class Carrinho:
    def __init__(self):
        self.itens = []
    def adicionar_item(self, produto):
        self.itens.append(produto)
    def remover_item(self, indice):
        self.itens.pop(indice)
    def calcular_total(self):
        total = 0
        for produto in self.itens:
            total += produto.preco * produto.quantidade
        return total
def aplicar_desconto(total):
    if total > 100:
        desconto = total * 0.15
    elif total > 50:
        desconto = total * 0.10
    else: 
        desconto = 0
    final = total - desconto
    return desconto, final

carrinho = Carrinho()

print("--- LOJA ---")
print("Bem-vindo à SuperMarket Python. ")
produto_aleatorio = random.sample(produtos_destaque, 3)
print(f"Produtos em destaque: {produto_aleatorio}")
nome = input("Qual é o seu nome?: ")

while True:
    print("1. Adicionar produto")
    print("2. Ver carrinho")
    print("3. Remover item do carrinho")
    print("4. Finalizar compra.")
    print("5. Sair do sistema.")

    try: 
        opcao = int(input(f"Olá cliente {nome}! Digite a opção desejada: "))
    except ValueError:
        print("Digite uma entrada válida.")
        continue

    if opcao == 1:
        try:
            nome_produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade de produtos desejados: "))
            compra = Produto(nome_produto, preco, quantidade)
            carrinho.adicionar_item(compra)
            print(f"{nome_produto} adicionado ao carrinho!")
        except ValueError:
            print("Digite uma entrada válida.")
            continue

    elif opcao == 2:
        if len(carrinho.itens) != 0:
            quantidade_produtos = len(carrinho.itens)
            print(f"Você tem {quantidade_produtos} produto (s) no carrinho.")
            for produto in carrinho.itens:
                print(f'Carrinho : Produto: {produto.nome},  Preço: R${produto.preco}, Quantidade: {produto.quantidade}')
        else:
            print("Não há nenhum item no carrinho.")

    elif opcao == 3:
        if len(carrinho.itens) != 0:
            contador = 1
            for produto in carrinho.itens:
                print(f'{contador}. Produto: {produto.nome},  Preço: R${produto.preco}, Quantidade: {produto.quantidade}')
                contador += 1
            try:
                remover_produto = int(input("Qual produto deseja remover?: "))
                carrinho.remover_item(remover_produto - 1)
                print("Item removido com sucesso!")
            except(ValueError, IndexError):
                print("Digite um valor válido e listado no seu carrinho.")
        else:
            print("Não há nenhum item no carrinho.")

    elif opcao == 4:
        hoje = datetime.datetime.now()
        formatado = hoje.strftime("%d/%m/%Y %H:%M")
        total = carrinho.calcular_total()
        desconto, final = aplicar_desconto(total)
        print(f'Subtotal: R${round(total, 2)}')
        print(f"Desconto: R${round(desconto, 2)}")
        print(f"Valor total: R${round(final, 2)}")
        print(f"Compra finalizada: {formatado} ")
        break
    elif opcao == 5:
        print("Saindo do sistema.")
        break
    else:
        print("Digite uma opção válida.")