from menu import design_m
import os, json


def ler_json():
    if not os.path.exists('produtos.json'):
        with open('produtos.json', 'w', encoding='utf-8') as file:
            return json.dump([], file)
    with open('produtos.json', 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def escrever_json(lista):
    with open('produtos.json', 'w', encoding='utf-8') as file:
        json.dump(lista, file, indent=4)

def info_lista():
    return []


def adicionar_produto():
    lista_produto = ler_json()
    while True:
        print('=' * 30)
        print("Adicionar Produto".center(30))
        print('=' * 30 +'\n')
        try:
            produto = {'nome': input("Nome: "),
                    'preco': float(input("Preço R$: ")),
                    'tipo':  input("Tipo: ")}

            lista_produto.append(produto)
            print(f"O Produto {produto['nome']} Foi Adicionado com Sucesso")
            os.system('cls')
            print(design_m)
            escrever_json(lista_produto)
            return
        except (ValueError, TypeError):
            print("ERROR: Valor Invalido")

def atualizar_produto():
    lista_produto = ler_json()
    while True:
        os.system('cls')
        print("Atualizar Produto\n")
        for i,  p in enumerate(lista_produto, start=1):
            print(f"[{i}] | {p['nome']}")
        try:
            print("[0] - Retornar ao Menu")
            editar = int(input("Qual produto deseja Atualizar: "))
            if 1 <= editar <= len(lista_produto):
                lista_produto[editar - 1] = {'nome': input("Nome: "),
                                            'preco': float(input("Preço: R$: ")),
                                            'tipo': input("Tipo: ")}
                escrever_json(lista_produto)
                enter = input("[Enter] para retornar ao menu: ")

                if enter is True or enter == '':
                    os.system('cls')
                    print(design_m)
                    return
            elif editar == 0:
                os.system('cls')
                print(design_m)
                return
            else:
                print(f"ERROR: {editar} Não é um valor válido")
                input("Tentar Novamente: [Enter]")
        except (ValueError, TypeError):
            print(f"ERROR: Digite um valor válido")
            input("Tentar Novamente: [Enter]")

def remover_produto():
        lista_produto = ler_json()
        while True:
            os.system('cls')
            print('Removedor De Produto\n')
            for i, p in enumerate(lista_produto, start=1):
                print(f"{i} | {p['nome']}")

            try:
                print("0 | Retornar Menu")
                print("Qual produto deseja remover:", end=' ' )
                n = int(input(""))

                if 1 <= n <= len(lista_produto):
                        print(f"O Produto {lista_produto[n - 1]['nome']} Foi Removido Com Sucesso")
                        lista_produto.pop(n - 1)
                        escrever_json(lista_produto)
                        enter = input("Aperte Qualquer Tecla para Retornar ao Menu: ")
                        if enter is True or enter == '':
                            os.system('cls')
                            print(design_m)
                        return
                elif n == 0:
                    os.system('cls')
                    print(design_m)
                    return
                    
                else:
                    print(f"ERROR: {n} Não é um valor válido")
                    input("Tentar Novamente: [Enter]")
            except (ValueError, TypeError):
                print("Digite um valor válido")
                input("Tentar Novamente: [Enter]")
                
def ver_produtos():
    lista_produto = ler_json()
    os.system('cls')
    try:
        if not lista_produto:
            print("Lista de Produtos está Vázia")
            input("[Enter] -> Retornar ao Menu: ")
            os.system('cls')
            print(design_m) 
            return
        for i, p in enumerate(lista_produto, start=1):
            print('=' * 30)
            print(f"ID: {i}\n"
                f"Nome: {p['nome']}\n"
                f"Preço: R${float(p['preco']):.2f}\n"
                f"Tipo: {p['tipo']}")
        print('=' * 30)
        
        enter = input("[Enter] -> Retornar ao menu: ")
        enter = ''
        if enter is True or enter == '':
            os.system('cls')
            print(design_m)

    except (ValueError, TypeError):
        print("ERRO: Valor Invalido")
    

def desconto():
    lista_produto = ler_json()
    while True:
        os.system('cls')
        print("Aplicando Desconto")
        for i, p in enumerate(lista_produto, start=1):
            print(f"{i} | {p['nome']}")
        try:
            print("0 | Para Retornar ao Menu")
            n = int(input("Qual Produto deseja aplicar desconto: "))
            while n > len(lista_produto):
                print("ERROR: Digite Apenas um dos Valores correspondentes")
                n = int(input(""))
                os.system('cls')
            porcentagem = int(input("Porcentagem a ser reduzida: "))
            if 1 <= n <= len(lista_produto):
                res  = (lista_produto[n - 1]['preco'] * porcentagem) / 100
                lista_produto[n - 1]['preco'] -= res
                print(f"O Preço do Produto {lista_produto[n -1]['nome']} Foi Reduzido em {porcentagem:.0f}%")
                enter = input("Pressione Qualquer Tecla para Retornar ao Menu: ")

                if enter is True or enter == '':
                    os.system('cls')
                    print(design_m)
                return
            elif n == 0:
                os.system('cls')
                print(design_m)
                return
            
            else:
                print(f"ERROR: {n} Não é um Valor Válido")
        except (ValueError, TypeError):
            print("ERROR: Digite um valor válido")

def menu():
    os.system('cls')
    print(design_m)
    while True:
        try:
    
            opcao = int(input("Selecione uma opção: "))
            if opcao == 1:
                os.system('cls')
                adicionar_produto()
                continue
            elif opcao == 2:
                remover_produto()
            elif opcao == 3:
                atualizar_produto() 
            elif opcao == 4:
                ver_produtos()
            elif opcao == 5:
                desconto()
            elif opcao == 6:
                print("Volte Sempre!")
                break
            else:
                print("ERROR: Digite Apenas números entre 1 e 5")
            
        except (ValueError, TypeError) or opcao > 5:
            print("ERROR: Digite Apenas números entre 1 e 5")
            
menu()