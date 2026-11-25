from time import sleep



# LINHA
def linha():
    print("-" * 40)




# aparece linha e texto
def painel(txt):
    linha()
    print(txt)
    linha()


# a pessoa escolhe o que ela vai fazer
def menu(lista):
    painel("ESCOLHA SUA OPÇÃO")
    cont = 1
    for item in lista:
        print(f"{cont} - {item}")
        cont += 1
    linha()
    opcao = input("Digite sua opção: ")
    return opcao


def lerArquivo(nome):
    with open(nome, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())


cont1 = 1
# cadastro
def cadastroUser(cont):
        print("-" * 15, "Cadastro do Cliente", "-" * 15)
        nomeC = input("Digite o seu nome: ")
        idade = int(input("Digite a sua idade: "))
        if idade < 18:
            print("Você é de menor, infelizmente não poderá realizar o cadastro")
            sleep(1)
            return cont

        with open("Cadastrados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nomeC.strip()} / {idade} / {cont}\n")

        print(f"nome: {nomeC}, idade: {idade}, ID: {cont}")
        sleep(1)
        print(f"Cliente Cadastrado com Sucesso!")
        sleep(1)
        cont += 1
        return cont

def buscar():
        print("-" * 15, "Buscar cliente", "-" * 15)
        idB = input("Digite o ID que voce quer procurar: ")
        
        encontrar = False

        with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
            for user in arquivo:
                dados = user.strip().split("/")

                if len(dados) < 3:
                    continue

                id = dados[2].strip()
                nome = dados[0].strip()
                idade = dados[1].strip()

                if idB == id:
                    print(f"\nO usuario com nome {nome} com o id {id} e idade {idade} foi encontrado!\n")
                    sleep(1)
                    encontrar = True
                    break

        if encontrar == False:
            print("Nenhum ID encontrado!")
            sleep(1)


def excluirC():
        print("-" * 15, "Excluir Cadastros", "-" * 15)
        idE = input("Digite o id que você quer excluir: ")

        encontrar = False

        clientesR = []

        with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
            for user in arquivo:
                dados = user.strip().split("/")

                if len(dados) < 3:
                    continue

                id = dados[2].strip()

                if idE != id:
                    clientesR.append(dados)
                else:
                    encontrar = True
                    print(f"Usuário com o id {id} excluido com sucesso!")
                    sleep(1)
                    
        with open("Cadastrados.txt", "w", encoding="utf-8") as arquivo:
            for usuario in clientesR:
                dado = usuario
                arquivo.write(f"{dado[0]}, {dado[1]}, {dado[2]}\n")


        if encontrar == False:
            print("Nenhum ID encontrado")
            sleep(1)

def atualizar():
    idDaPessoa = input("Digite o ID do usuario para atualizar o nome/idade: ")

    cadastrosAtualizados = []
    encontrar = False

    with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
        for user in arquivo:
            dados = user.strip().split("/")

            if len(dados) < 3:
                continue

            idP = dados[2].strip()

            if idDaPessoa == idP:
                atualizar1 = input("Digite o nome atualizado: ")
                atualizar = int(input("Digite a idade atualizada: "))
                if atualizar < 18:
                    print("Idades menores de 18 não são permitidas")
                    return
                dados[0] = atualizar1
                dados[1] = atualizar
                encontrar = True
            cadastrosAtualizados.append(dados)

        with open("Cadastrados.txt", "w", encoding="utf-8") as arquivo:
            for usuario in cadastrosAtualizados:
                arquivo.write(f"{usuario[0]} / {usuario[1]} / {usuario[2]}\n")

        if encontrar == True:
            print("Idade e nome atualizados com sucesso")
        else:
            print("ID não encontrado")


cont2 = 1
produtos = []
def cadastroProduto(cont):
        print("-" * 15, "Cadastro de Produto", "-" * 15)
        produtoC = input("Digite aqui o nome do produto: ")
        valor = float(input("Diigite o valor do produto: "))
        unidades = int(input("Digite a quantidade dos produtos: "))
        if unidades < 20 or unidades < 0:
            print("Não podem ser registrados produtos com quantidades menores que 20 ou menores que 0")
            return cont


        produto = {"nome": produtoC, "valor": valor, "id": cont, "quantidade": unidades}
        produtos.append(produto)
        with open("Comidas.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{produto['nome']} / {produto['valor']} / {produto['quantidade']} / {produto['id']}\n")

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

                if len(alimento) < 4:
                    continue

                idC = alimento[3].strip()
                comida = alimento[0].strip()
                valor = alimento[1].strip()
                unidade = alimento[2].strip()

                if idBP == idC:
                    print(f"Produto de nome {comida}, id {idC}, preço {valor} e qauntidade de {unidade} . Encontrado com sucesso!")
                    encontrar = True
                    

        if encontrar == False:
            print("ID de produto não encontrado")
            sleep(1)

def excluirProduto():
        print("-" * 15, "Excluir Cadastros", "-" * 15)
        idE = input("Digite o id que você quer excluir: ")
        
        encontrar = False

        produtosSobrando = []

        with open("Comidas.txt", "r", encoding="utf-8") as arquivo:
                for user in arquivo:
                    dados = user.strip().split("/")

                    if len(dados) < 4:
                        continue
        
                    id = dados[3].strip()
        
                    if idE != id:
                        produtosSobrando.append(dados)
                    else:
                        encontrar = True
                        print(f"Usuário com o id {id} excluido com sucesso!")
                        sleep(0.5)
                        
        with open("Comidas.txt", "w", encoding="utf-8") as arquivo:
            for usuario in produtosSobrando:
                dado = usuario
                arquivo.write(f"{dado[0]}, {dado[1]}, {dado[2]}\n")
        
        
        if encontrar == False:
            print("Nenhum ID encontrado")
            sleep(1)

def atualizarProduto():
    idDoProduto = input("Digite o ID do produto para atualizar a quantidade: ")
    
    produtosAtualizados = []
    encontrar = False
    
    with open("Comidas.txt", "r", encoding="utf-8") as arquivo:
        for user in arquivo:
            dados = user.strip().split("/")
    
            if len(dados) < 4:
                continue
    
            idP = dados[3].strip()
    
            if idDoProduto == idP:
                atualizar = int(input("Digite a quantidade atualizada: "))
                if atualizar < 20:
                    print("Não podem ser registrado uma quantia menor doque 20 unidades")
                    return
                dados[2] = atualizar
                encontrar = True
            produtosAtualizados.append(dados)
    
    with open("Comidas.txt", "w", encoding="utf-8") as arquivo:
        for produto in produtosAtualizados:
            arquivo.write(f"{produto[0]} / {produto[1]} / {produto[2]} / {produto[3]}\n")
    
    if encontrar == True:
        print("Produto atualizada com sucesso")
    else:
        print("ID não encontrado")

cont3 = 1
def vendaProduto(cont):
    while True:
        print("-" * 15, "Cadastro de venda", "-" * 15)

        encontraPessoa = False

        idDaPessoa = input("Digite o seu ID para compra: ")
        with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
            for pessoa in arquivo:
                people = pessoa.strip().split("/")

                if len(people) < 3:
                    continue

                idP = people[2].strip()

                if idDaPessoa == idP:
                    encontraPessoa = True
                    nomeDaPessoa = people[0].strip()

        if encontraPessoa == False:
            print("Esse ID não existe")
            return cont
  
        while True:
            produtosSobrando = []
            encontraNome = False
            vendaFeita = False          
            compra = input("Digite o nome do produto que você deseja comprar: ")
            with open("Comidas.txt", "r", encoding="utf-8") as arquivo:
                    for nomes in arquivo:
                        nome1 = nomes.strip().split("/")

                        if len(nome1) < 4:
                             continue

                        nomeP = nome1[0].strip()
                        id = nome1[3].strip()
                        valor = float(nome1[1].strip())
                        qtd = int(nome1[2].strip())

                        if compra == nomeP:
                            encontraNome = True
                            quantosQuer = int(input("Digite a quantidade que deseja comprar: "))
                            nomeCompra = nomeP
                            idCompra = id
                            valorCompra = valor
                            if quantosQuer <= qtd:
                                quantidade = qtd - quantosQuer
                                total = quantosQuer * valor
                                vendaFeita = True
                            else:
                                print("Não existe estoque suficiente")
                                quantidade = qtd

                        else:
                            quantidade = qtd
                            
                        produto = [nomeP, valor, quantidade, id]
                        produtosSobrando.append(produto)
                            
                            
                    if encontraNome == False:
                            print("Esse produto não existe")
                            continue
                    elif vendaFeita == False:
                            print("A venda não foi feita")
                            continue
                    else:
                        print(f"\nVoce comprou {quantosQuer} e o valor total foi {total}\n")
                        print(f"A sua venda foi {nomeCompra}, e o ID da compra é {cont}")
                        with open("Vendas.txt", "a", encoding="utf-8") as arquivo:
                            arquivo.write(f"{nomeDaPessoa} / {nomeCompra} / {quantosQuer} / {valorCompra} / {total} / {idCompra} / {cont} / {idDaPessoa}\n")
                            
                                            
                    if vendaFeita == True:
                        with open("Comidas.txt", "w", encoding="utf-8") as arquivo:
                            for comida in produtosSobrando:
                                sobras = comida
                                arquivo.write(f"{sobras[0]} / {sobras[1]} / {sobras[2]} / {sobras[3]}\n")
                        break
            return cont
        break

def buscarCompra():
        print("-" * 15, "Procurar compra", "-" * 15)

        idCompra = input("Digite o id da sua compra: ")

        encontrar = False

        with open("Vendas.txt", "r", encoding="utf-8") as arquivo:
            for comida in arquivo:
                alimento = comida.strip().split("/")

                if len(alimento) < 8:
                    continue

                id = alimento[7].strip()
                nome = alimento[0].strip()
                total = alimento[4].strip()
                quantidade = alimento[2].strip()
                idDaCompra = alimento[6].strip()
                nomeDoProduto = alimento[1].strip()

                if idCompra == idDaCompra:
                    print(f"A compra de {nome}, ID: {id} foi {nomeDoProduto} valor total de {total}, quantidade comprada foi de {quantidade} e com o ID de venda {idDaCompra} foi encontrado com sucesso")
                    encontrar = True


        if encontrar == False:
            print("Não foi encontrado nenhum produto com esse id")
            sleep(1.5)

def excluirCompra():
        print("-" * 15, "Excluir compra", "-" * 15)
        excluid = input("Digite o id da compra para exclui-la: ")

        encontrar = False
        comprasR = []

        with open("Vendas.txt", "r", encoding="utf-8") as arquivo:
          for compra in arquivo:
               compras = compra.strip().split("/")

               if len(compras) < 8:
                   continue

               id = compras[6].strip()

               if excluid != id:
                comprasR.append(compras)
               else:
                    encontrar = True
                    print(f"A venda com o ID: {id} foi exluida com sucesso")
        

        with open("Vendas.txt", "w", encoding="utf-8") as arquivo:
             for buy in comprasR:
                  comprar = buy
                  arquivo.write(f"{comprar[0]} / {comprar[1]} / {comprar[2]} / {comprar[3]} / {comprar[4]} / {comprar[5]} / {comprar[6]} / {comprar[7]}\n")

        if encontrar == False:
             print("ID de venda não encontrado")
             sleep(1)


def relatorioDeVendas():
    print("-" * 15, "Relatorio de vendas", "-" * 15)

    totalDoEstoque = 0

    with open("Vendas.txt", "r", encoding="utf-8") as arquivo:
        for venda in arquivo:
            vendas = venda.strip().split("/")
            id = vendas[7].strip()
            nome = vendas[0].strip()
            total = float(vendas[4].strip())
            quantidade = vendas[2].strip()
            idDaCompra = vendas[6].strip()
            nomeDoProduto = vendas[1].strip()

            totalDoEstoque += total

            print(f"""
            Usuario: {nome} 
            ID: {id}
            Comprou: {nomeDoProduto} e {quantidade} unidades e o ID da compra foi {idDaCompra}
            e o valor total foi: {total}""")

    print(f"     O total arrecadado foi {totalDoEstoque:.2f}")

def relatorioDeProdutos():

     with open("Comidas.txt", "r", encoding="utf-8") as arquivo:
          for comida in arquivo:
            comidas = comida.strip().split("/")

            nomeDoProduto = comidas[0].strip()
            preco = comidas[1].strip()
            qtd = comidas[2].strip()
            id = comidas[3].strip()

            print(f"""
            Produto: {nomeDoProduto}
            Valor: {preco}
            quantidade: {qtd}
            ID: {id}""")
            



# titulo do ngc
painel("LANXONETE".center(40))

# oque ta rodando
while True:
    digito = menu(["Gerenciar Clientes", "Gerenciar Produtos", "Gerenciar Vendas", "Relátorios", "Sair"])
    if digito == "1":
        while True:
            escolha = menu(["CADASTRAR", "BUSCAR", "Excluir", "Atualizar", "SAIR"])
            if escolha == "1":
                cont1 = cadastroUser(cont1)
            elif escolha == "2":
                buscar()
            elif escolha == "3":
                excluirC()
            elif escolha == "4":
                atualizar()
            elif escolha == "5":
                print("Voltando...")
                sleep(1)
                break
            else:
                print("Digite uma opção valida")
                sleep(1)

    elif digito == "2":
        while True:
            opc = menu(["Cadastrar", "Buscar", "Excluir", "Atualizar", "Sair"])
            if opc == "1":
                cont2 = cadastroProduto(cont2)
            elif opc == "2":
                buscarProduto()
            elif opc == "3":
                excluirProduto()
            elif opc == "4":
                atualizarProduto()
            elif opc == "5":
                print("Voltando...")
                sleep(1.3)
                break
            else:
                print("Digite uma opção valida")
                sleep(1.3)

    elif digito == "3":
        while True:
            opc = menu(["Cadastrar", "Buscar", "Excluir", "Sair"])
            if opc == "1":
                cont3 = vendaProduto(cont3)
            elif opc == "2":
                buscarCompra()
            elif opc == "3":
                excluirCompra()
            elif opc == "4":
                print("Voltando...")
                sleep(1)
                break
            else:
                print("Digite uma opção valida")
                sleep(1)

    elif digito == "4":
        while True:
            opc = menu(["Relatorios de vendas", "Relatorios de produtos", "Sair"])
            if opc == "1":
                relatorioDeVendas()
            elif opc == "2":
                relatorioDeProdutos()
            elif opc == "3":
                print("Voltando...")
                sleep(1)
                break
            else:
                print("Digite uma opção valida")
                sleep(1)

    elif digito == "5":
        print("Programa Encerrado")
        break

    else:
        print("\nDigite uma opção valida\n")
    sleep(1)
