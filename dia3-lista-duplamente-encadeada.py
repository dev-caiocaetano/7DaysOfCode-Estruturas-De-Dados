import os

class Produto:
    def __init__(self, codigo_de_barras, nome, preco, quantidade):
        self.codigo_de_barras = codigo_de_barras
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.proximo_produto = None
        self.produto_anterior = None

class ListaDeProdutos:
    def __init__(self):
        self.head = None
        self.tail = None

    def adicionar_produto(self):
        os.system('clear')
        nome_do_programa()

        while True:
            try:
                codigo_de_barras = int(input('Digite o Código de Barras: '))
                produto_atual = self.head
                codigo_existente = False
                while produto_atual is not None:
                    if produto_atual.codigo_de_barras == codigo_de_barras:
                        codigo_existente = True
                        break
                    produto_atual = produto_atual.proximo_produto
                if codigo_existente:
                    os.system('clear')
                    nome_do_programa()
                    print(f'O Código de Barras já existe! Por favor, digite outro.\n')    
                else:
                    break
            except ValueError:
                os.system('clear')
                nome_do_programa()
                print('Por favor, digite um número válido para o Código de Barras.\n')
        
        while True:
            try:
                nome = input('Qual o nome do produto?: ').strip().title()
                if not nome:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, digite um nome válido para o produto!\n')
                else:
                    break
            except ValueError:
                print('Por favor, digite um nome válido para o paciente!\n')

        while True:
            try:
                preco = float(input('Qual o preço do produto?: R$ '))
                if preco <= 0:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, digite um preço válido (Maior que zero).\n')
                else:
                    break
            except ValueError:
                os.system('clear')
                nome_do_programa()
                print('Por favor, digite um número válido para o preço.\n')

        while True:
            try:
                quantidade = int(input('Qual a quantidade que deseja adicionar?: '))
                if quantidade < 0:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, digite uma quantidade válida (zero ou maior).\n')
                else:
                    break
            except ValueError:
                os.system('clear')
                nome_do_programa()
                print('Por favor, digite um número válido para a quantidade.\n')

        novo_produto = Produto(codigo_de_barras, nome, preco, quantidade)
        if self.head is None:
            self.head = novo_produto
            self.tail = novo_produto
        else:
            self.tail.proximo_produto = novo_produto
            novo_produto.produto_anterior = self.tail
            self.tail = novo_produto
        os.system('clear')
        nome_do_programa()
        print(f'Produto {nome} adicionado com sucesso!!')
        voltar_ao_menu_principal()

    def remover_produto(self):
        os.system('clear')
        nome_do_programa()        
        if not self.head:
            print('Não há produtos no estoque!')
            voltar_ao_menu_principal()
        else:
            try:
                codigo_de_barras = int(input('Digite o Código de Barras que deseja remover: '))
            except ValueError:
                print('\nPor favor, digite um código válido.')
                voltar_ao_menu_principal()
                return

            if self.head.codigo_de_barras == codigo_de_barras:
                os.system('clear')
                nome_do_programa()
                print('Produto removido com sucesso!')
                self.head = self.head.proximo_produto
                if self.head:
                    self.head.produto_anterior = None
            else:  
                produto_atual = self.head
                produto_encontrado = False

                while produto_atual is not None:
                    proximo_produto = produto_atual.proximo_produto
                    if proximo_produto and proximo_produto.codigo_de_barras == codigo_de_barras:
                        os.system('clear')
                        nome_do_programa()
                        print('Produto removido com sucesso!')
                        produto_atual.proximo_produto = proximo_produto.proximo_produto
                        if proximo_produto.proximo_produto:
                            proximo_produto.proximo_produto.produto_anterior = produto_atual
                        produto_encontrado = True
                        break
                    produto_atual = produto_atual.proximo_produto
                if not produto_encontrado:
                    os.system('clear')
                    nome_do_programa()
                    print('Produto não encontrado!')  
            voltar_ao_menu_principal()  

    def atualizar_estoque(self):
        os.system('clear')
        nome_do_programa()
        if not self.head:
            print('Não há produtos no estoque.')
            voltar_ao_menu_principal()
            return
        try:
            codigo_de_barras = int(input('Digite o Código de Barras do produto que deseja atualizar: '))
            os.system('clear')
            nome_do_programa()
        except ValueError:
            print('Código de barras inválido.')
            voltar_ao_menu_principal()
            return

        produto_atual = self.head
        while produto_atual is not None:
            if produto_atual.codigo_de_barras == codigo_de_barras:
                print(f'Produto encontrado: {produto_atual.nome}')

                while True:
                    try:
                        novo_preco = float(input(f'Preço atual: R${produto_atual.preco} | Novo preço (Digite o mesmo caso não queira alterar!): R$ '))
                        if novo_preco <= 0:
                            os.system('clear')
                            nome_do_programa()
                            print('Por favor, digite um preço válido (Maior que zero).')
                        else:
                            break
                    except ValueError:
                        os.system('clear')
                        nome_do_programa()
                        print('Por favor, digite um número válido para o preço.')

                while True:
                    try:
                        nova_quantidade = int(input(f'Quantidade atual: {produto_atual.quantidade} | Nova quantidade: '))
                        if nova_quantidade < 0:
                            os.system('clear')
                            nome_do_programa()
                            print('Por favor, digite uma quantidade válida (Zero ou maior).')
                        else:
                            break
                    except ValueError:
                        os.system('clear')
                        nome_do_programa()
                        print('Por favor, digite um número válido para a quantidade.')

                produto_atual.preco = novo_preco if novo_preco else produto_atual.preco
                produto_atual.quantidade = nova_quantidade if nova_quantidade >= 0 else produto_atual.quantidade
                
                os.system('clear')
                nome_do_programa()
                print('Produto atualizado com sucesso!')
                voltar_ao_menu_principal()
                return
            produto_atual = produto_atual.proximo_produto

        print('Produto não encontrado.')
        voltar_ao_menu_principal()

    def listar_estoque(self):
        os.system('clear')
        nome_do_programa()
        if not self.head:
            print('Não há produtos no estoque.')
        else:
            produto_atual = self.head
            while produto_atual is not None:
                print(f'Código de barras: {produto_atual.codigo_de_barras} | Nome: {produto_atual.nome} | Preço: R${produto_atual.preco:.2f} | Quantidade: {produto_atual.quantidade}')
                produto_atual = produto_atual.proximo_produto
        voltar_ao_menu_principal()

def nome_do_programa():
    print('Ｃｏｎｔｒｏｌｅ ｄｅ Ｅｓｔｏｑｕｅ 📝\n')

def exibir_opcoes():
    print('1. Listar Estoque')
    print('2. Adicionar Produto')
    print('3. Remover Produto')
    print('4. Atualizar Produto')
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

def escolher_opcao(lista_de_produtos):
    while True:
        os.system('clear')
        nome_do_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                lista_de_produtos.listar_estoque()
            elif opcao_escolhida == 2:
                lista_de_produtos.adicionar_produto()
            elif opcao_escolhida == 3:
                lista_de_produtos.remover_produto()
            elif opcao_escolhida == 4:
                lista_de_produtos.atualizar_estoque()
            elif opcao_escolhida == 5:
                finalizar_programa()
                break
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def main():
    lista_de_produtos = ListaDeProdutos()
    escolher_opcao(lista_de_produtos)

if __name__ == '__main__':
    main()
