from time import sleep
from funçoes import *


cont1 = 1
# cadastro
def cadastroUser(cont):
        print("-" * 15, "Cadastro do Cliente", "-" * 15)
        nomeC = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        if idade < 18:
            print("Você é de menor, infelizmente não poderá realizar o cadastro")
            sleep(1.5)
            return 

        usuarios = []
        
        usuario = [nomeC, idade, cont]

        usuarios.append(usuario)

        with open("Cadastrados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nomeC.strip()} / {idade} / {cont}\n")

        print(f"nome: {nomeC}, idade: {idade}, ID: {cont}")
        sleep(1)
        print(f"Cliente Cadastrado com Sucesso!")
        sleep(1.5)
        return cont

def buscar():
        print("-" * 15, "Buscar cliente", "-" * 15)
        idB = input("Digite o ID que voce quer procurar: ")
        
        encontrar = False

        with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
            for user in arquivo:
                dados = user.strip().split("/")

                id = dados[2].strip()
                nome = dados[0].strip()
                idade = dados[1].strip()

                if idB == id:
                    print(f"\nO usuario com nome {nome} com o id {id} e idade {idade} foi encontrado!\n")
                    sleep(2)
                    encontrar = True
                    break

        if encontrar == False:
            print("Nenhum ID encontrado!")
            sleep(1.5)


def excluirC():
        print("-" * 15, "Excluir Cadastros", "-" * 15)
        idE = input("Digite o id que você quer excluir: ")

        encontrar = False

        clientesR = []

        with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
            for user in arquivo:
                dados = user.strip().split("/")

                id = dados[2].strip()

                if idE != id:
                    clientesR.append(dados)
                else:
                    encontrar = True
                    print(f"Usuário com o id {id} excluido com sucesso!")
                    sleep(2)
                    
        with open("Cadastrados.txt", "w", encoding="utf-8") as arquivo:
            for usuario in clientesR:
                dado = usuario
                arquivo.write(f"{dado[0]}, {dado[1]}, {dado[2]}\n")


        if encontrar == False:
            print("Nenhum ID encontrado")
            sleep(1.5)
    

cont2 = 1
def cadastroProduto(cont):
        print("-" * 15, "Cadastro de Produto", "-" * 15)
        produtoC = input("Digite aqui o nome do produto: ")
        valor = float(input("Diigite o valor do produto: "))
        unidades = int(input("Digite a quantidade dos produtos: "))
        if unidades < 20 or unidades < 0:
            print("Não podem ser registrados produtos com quantidades menores que 20 ou menores que 0")
            return

        produtos = []

        produto = {"nome": produtoC, "valor": valor, "id": cont, "quantidade": unidades}
        produtos.append(produto)
        with open("Comidas.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{produtoC} / {valor} / {unidades} / {cont}\n")

        print("Produto Cadastrado com Sucesso!")
        print(f"O seu produto é: {produtoC}, id: {cont}, quantidade adicionada: {unidades} e valor: {valor}")
        cont += 1
        return cont

def buscarProduto():
        print("-" * 15, "Busca de Produto", "-" * 15)

        idBP = input("Digite o id do produto que você quer procurar: ")

        encontrar = False

        with open("Comidas.txt", "r", encoding="utf-8") as arquivo:
            for p in arquivo:
                alimento = p.strip().split("/")

                idC = alimento[3].strip()
                comida = alimento[0].strip()
                valor = alimento[1].strip()
                unidade = alimento[2].strip()

                if idBP == idC:
                    print(f"Produto de nome {comida}, id {idC}, preço {valor} e qauntidade de {unidade} . Encontrado com sucesso!")
                    encontrar = True
                    

        if encontrar == False:
            print("ID de produto não encontrado")
            sleep(1.5)

def excluirProduto():
        print("-" * 15, "Excluir Cadastros", "-" * 15)
        idE = input("Digite o id que você quer excluir: ")
        
        encontrar = False

        produtosSobrando = []

        with open("Comidas.txt", "r", encoding="utf-8") as arquivo:
                for user in arquivo:
                    dados = user.strip().split("/")
        
                    id = dados[3].strip()
        
                    if idE != id:
                        produtosSobrando.append(dados)
                    else:
                        encontrar = True
                        print(f"Usuário com o id {id} excluido com sucesso!")
                        sleep(2)
                        
        with open("Comidas.txt", "w", encoding="utf-8") as arquivo:
            for usuario in produtosSobrando:
                dado = usuario
                arquivo.write(f"{dado[0]}, {dado[1]}, {dado[2]}\n")
        
        
        if encontrar == False:
            print("Nenhum ID encontrado")
            sleep(1.5)

cont3 = 1      
def vendaProduto(cont):
    print("-" * 15, "Cadastro de venda", "-" * 15)

    produtosSobrando = []

    compra = input("Digite o nome do produto que você deseja comprar: ")
    quantosQ = int(input("Digite a quantidade que deseja comprar: "))

    encontrar = False
    vendaFeita = False

    with open("Comidas.txt", "r", encoding="utf-8") as arquivo:
        for produto in arquivo:
            produtos = produto.strip().split("/")

            nome = produtos[0].strip()
            id = produtos[3].strip()
            valor = float(produtos[1].strip())
            qtd = int(produtos[2].strip())

            if compra == nome:
                encontrar = True
                if quantosQ <= qtd:
                        qtd = qtd - quantosQ
                        total = quantosQ * valor
                        vendaFeita = True
                else:
                    print("Não existe estoque suficiente")

            produto = [nome, valor, qtd, id]
            produtosSobrando.append(produto)


        if encontrar == False:
            print("Esse produto não existe")
        elif vendaFeita == False:
            print("A venda não foi feita")
        else:
            print(f"\nVoce comprou {quantosQ} e o valor total foi {total}\n")
            print(f"A sua venda foi {nome}, e o ID da compra é {cont}")
            with open("Vendas.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{nome} / {quantosQ} / {total} / {id} / {cont}\n")
            cont += 1

        if vendaFeita == True:
            with open("Comidas.txt", "w", encoding="utf-8") as arquivo:
                for comida in produtosSobrando:
                    sobras = comida
                    arquivo.write(f"{sobras[0]} / {sobras[1]} / {sobras[2]} / {sobras[3]}\n")
    return cont

def buscarCompra():
        print("-" * 15, "Procurar compra", "-" * 15)

        idCompra = input("Digite o id da sua compra: ")

        encontrar = False

        with open("Vendas.txt", "r", encoding="utf-8") as arquivo:
            for comida in arquivo:
                alimento = comida.strip().split("/")

                id = alimento[4].strip()
                nome = alimento[0].strip()
                total = alimento[2].strip()
                quantidade = alimento[1].strip()
                idDaComida = alimento[3].strip()

                if idCompra == id:
                    print(f"A compra de {nome}, com o id {idDaComida}, valor total de {total} e quantidade comprada foi de {quantidade} foi encontrada com sucesso")
                    encontrar = True


        if encontrar == False:
            print("Não foi encontrado nenhum produto com esse id")
            sleep(1.5)



# titulo do ngc
painel("LANCHONETE".center(40))

# oque ta rodando
while True:
    digito = menu(["Gerenciar Clientes", "Gerenciar Produtos", "Gerenciar Vendas", "Relátorios", "Sair"])
    if digito == "1":
        while True:
            escolha = menu(["CADASTRAR", "BUSCAR", "Excluir", "Atualizar", "SAIR"])
            if escolha == "1":
                cadastroUser(cont1)
                cont1 += 1
            elif escolha == "2":
                buscar()
            elif escolha == "3":
                excluirC()
            elif escolha == "5":
                print("Voltando...")
                sleep(1.3)
                break
            else:
                print("Digite uma opção valida")
                sleep(1.3)

    elif digito == "2":
        while True:
            opc = menu(["Cadastrar", "Buscar", "Excluir", "Atualizar", "Sair"])
            if opc == "1":
                cadastroProduto(cont2)
                cont2 += 1
            elif opc == "2":
                buscarProduto()
            elif opc == "3":
                excluirProduto()
            elif opc == "5":
                print("Voltando...")
                sleep(1.3)
                break
            else:
                print("Digite uma opção valida")
                sleep(1.3)

    elif digito == "3":
        while True:
            opc = menu(["Cadastrar", "Buscar", "Sair"])
            if opc == "1":
                vendaProduto(cont3)
                cont3 += 1
            elif opc == "2":
                buscarCompra()
            elif opc == "3":
                break
            

    elif digito == "5":
        print("Programa Encerrado")
        break

    else:
        print("\nDigite uma opção valida\n")
    sleep(1)
