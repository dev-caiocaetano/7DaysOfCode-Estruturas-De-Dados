import os

class ListaDeCompras:
    def __init__(self):
        self.itens = []
        self.quantidades = []

    def adicionar_item(self):
        os.system('clear')
        nome_do_programa()
        while True:
            try:
                item = input('Qual item que deseja adicionar à lista?: ').strip().title()
                if not item:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, digite um nome válido para o item!\n')
                else:
                    break
            except ValueError:
                print('Por favor, digite um nome válido para o item!')
        while True:
            try:
                quantidade = int(input(f'Quanto de {item} deseja adicionar?: '))
                if quantidade <= 0:
                    print('Por favor, digite um quantidade válida.')
                else:
                    break
            except ValueError:
                print('Por favor, digite um número inteiro para a quantidade.')
        self.itens.append(item)
        self.quantidades.append(quantidade)
        print(f'\nO item {item} foi adicionado à lista com sucesso!')
        voltar_ao_menu_principal()

    def remover_item(self):
        os.system('clear')
        nome_do_programa()
        if not self.itens:
            print('A lista está vazia.')
            voltar_ao_menu_principal()
        else:
            item = input('Qual o nome do item que deseja remover?: ').strip().lower()
            for i, item_lista in enumerate(self.itens):
                if item_lista.lower() == item:
                    del self.itens[i]
                    del self.quantidades[i]
                    print(f'\nO item {item.title()} foi removido com sucesso!')
                    voltar_ao_menu_principal()
                    return
            print('Esse item não está na lista.')
            voltar_ao_menu_principal()

    def listar_itens(self):
        os.system('clear')
        nome_do_programa()
        if not self.itens:
            print('A lista está vazia.')
            voltar_ao_menu_principal()
        else:
            for i in range(len(self.itens)):
                item = self.itens[i].title()
                quantidade = self.quantidades[i]
                print(f'Item {i+1}: {item.ljust(20)} | Quantidade: {quantidade}')
            voltar_ao_menu_principal()

    def atualizar_quantidade(self):
        os.system('clear')
        nome_do_programa()
        if not self.itens:
            print("A lista está vazia.")
            voltar_ao_menu_principal()
        else:
            item = input('Qual item deseja atualizar?: ').strip().lower()
            if item.title() in self.itens:
                indice = self.itens.index(item.title())
                print(f'A quantidade de {item.title()} atual é {self.quantidades[indice]}!\n')
                while True:
                    try:
                        quantidade = int(input(f'Quanto de {item.title()} deseja adicionar?: '))
                        if quantidade <= 0:
                            print('Por favor, digite uma quantidade válida.')
                        else:
                            break
                    except ValueError:
                        os.system('clear')
                        nome_do_programa()
                        print('Por favor, digite um número inteiro para a quantidade.')
                self.quantidades[indice] = quantidade
                os.system('clear')
                nome_do_programa()
                print(f'A quantidade de {item.title()} foi atualizada com sucesso!')
            else:
                print(f'\nO item "{item.title()}" não está na lista.')
            voltar_ao_menu_principal()

def nome_do_programa():
    print('Ｌｉｓｔａ ｄｅ Ｃｏｍｐｒａｓ\n')

def exibir_opcoes():
    print('1. Mostrar Lista')
    print('2. Adicionar Item')
    print('3. Remover Item')
    print('4. Atualizar quantidade')
    print('5. Sair\n')

def opcao_invalida():
    os.system('clear')
    nome_do_programa()
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def finalizar_programa():
    os.system('clear')
    print('Finalizando o programa! Até logo ... 😊 \n')

def voltar_ao_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu: ')

def escolher_opcao(lista):
    while True:
        os.system('clear')
        nome_do_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                lista.listar_itens()
            elif opcao_escolhida == 2:
                lista.adicionar_item()
            elif opcao_escolhida == 3:
                lista.remover_item()
            elif opcao_escolhida == 4:
                lista.atualizar_quantidade()
            elif opcao_escolhida == 5:
                finalizar_programa()
                break            
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def main():
    lista = ListaDeCompras()
    escolher_opcao(lista)

if __name__ == '__main__':
    main()
