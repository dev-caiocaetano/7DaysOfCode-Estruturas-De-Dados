import os

class Produto:
    def __init__(self, codigo, nome, quantidade, preco):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

class Node:
    def __init__(self, produto):
        self.esquerda = None
        self.direita = None
        self.produto = produto

class ArvoreProduto:
    def __init__(self):
        self.raiz = None

    def adicionar_produto(self):
        os.system('clear')
        nome_do_programa()
        try:
            codigo = int(input('Código do Produto: '))
            if self.buscar_produto(codigo):
                os.system('clear')
                nome_do_programa()
                print('Erro: Código existente!')
                voltar_ao_menu_principal()
                return
        except ValueError:
            os.system('clear')
            nome_do_programa()
            print('Erro: ID inválido!')
            voltar_ao_menu_principal()
            return

        while True:
            try:
                nome = input('Nome do Produto: ').strip().title()
                if not nome:
                    os.system('clear')
                    nome_do_programa()
                    print('O nome do produto não pode ser vazio!\n')
                else:
                    break
            except ValueError:
                print('O nome do produto não pode ser vazio!\n')

        while True:
            try:
                quantidade = int(input('Quantidade: '))
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

        while True:
            try:
                preco = float(input('Preço (Use ponto para separar centavos): R$ '))
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

        self.inserir_produto(codigo, nome, quantidade, preco)
        os.system('clear')
        nome_do_programa()
        print(f'Produto {nome} adicionado com sucesso!')
        voltar_ao_menu_principal()

    def inserir_produto(self, codigo, nome, quantidade, preco):
        novo_produto = Produto(codigo, nome, quantidade, preco)
        if self.raiz is None:
            self.raiz = Node(novo_produto)
        else:
            self._inserir_produto(novo_produto, self.raiz)

    def _inserir_produto(self, produto, node):
        if produto.codigo < node.produto.codigo:
            if node.esquerda is None:
                node.esquerda = Node(produto)
            else:
                self._inserir_produto(produto, node.esquerda)
        elif produto.codigo > node.produto.codigo:
            if node.direita is None:
                node.direita = Node(produto)
            else:
                self._inserir_produto(produto, node.direita)

    def remover_produto(self):
        os.system('clear')
        nome_do_programa()
        if not self.raiz:
            print('Não há produtos no estoque!')
            voltar_ao_menu_principal()
        else:
            try:
                codigo = int(input('Código do Produto a ser removido: '))
                produto_removido = self.buscar_produto(codigo) 
                if produto_removido: 
                    self.raiz = self._remover_produto(self.raiz, codigo)
                    os.system('clear')
                    nome_do_programa()
                    print('Produto removido com sucesso!')
                else:
                    os.system('clear')
                    nome_do_programa()
                    print('Produto não encontrado!')
                voltar_ao_menu_principal()
            except ValueError:
                os.system('clear')
                nome_do_programa()
                print('Código inválido!')
                voltar_ao_menu_principal()

    def _remover_produto(self, node, codigo):
        if node is None:
            return node
        if codigo < node.produto.codigo:
            node.esquerda = self._remover_produto(node.esquerda, codigo)
        elif codigo > node.produto.codigo:
            node.direita = self._remover_produto(node.direita, codigo)
        else:
            if node.esquerda is None:
                return node.direita
            if node.direita is None:
                return node.esquerda
            temp = self._min_value_node(node.direita)
            node.produto = temp.produto
            node.direita = self._remover_produto(node.direita, temp.produto.codigo)
        return node

    def _min_value_node(self, node):
        while node.esquerda is not None:
            node = node.esquerda
        return node

    def atualizar_produto(self):
        os.system('clear')
        nome_do_programa()

        if not self.raiz:
            print('Não há produtos no estoque.')
            voltar_ao_menu_principal()
            return

        try:
            codigo = int(input('Digite o código do produto que deseja atualizar: '))
            os.system('clear')
            nome_do_programa()
        except ValueError:
            print('Código inválido.')
            voltar_ao_menu_principal()
            return

        node = self.buscar_produto(codigo)
        if node:
            print(f'Produto encontrado: {node.produto.nome}')

            while True:
                try:
                    novo_preco = float(input(f'Preço atual: R${node.produto.preco} | Novo preço (Digite o mesmo valor se não quiser alterar): R$ '))
                    if novo_preco <= 0:
                        os.system('clear')
                        nome_do_programa()
                        print('Por favor, insira um preço válido (Maior que zero).')
                    else:
                        break
                except ValueError:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, insira um número válido para o preço.')

            while True:
                try:
                    nova_quantidade = int(input(f'Quantidade atual: {node.produto.quantidade} | Nova quantidade: '))
                    if nova_quantidade < 0:
                        os.system('clear')
                        nome_do_programa()
                        print('Por favor, insira uma quantidade válida (Zero ou maior).')
                    else:
                        break
                except ValueError:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, insira um número válido para a quantidade.')

            node.produto.preco = novo_preco if novo_preco else node.produto.preco
            node.produto.quantidade = nova_quantidade if nova_quantidade >= 0 else node.produto.quantidade
            
            os.system('clear')
            nome_do_programa()
            print(f'Produto atualizado com sucesso! Novo preço: R${node.produto.preco:.2f} | Nova quantidade: {node.produto.quantidade}')
        else:
            os.system('clear')
            nome_do_programa()
            print('Produto não encontrado.')
        voltar_ao_menu_principal()

    def buscar_produto(self, codigo):
        return self._buscar_produto(codigo, self.raiz)

    def _buscar_produto(self, codigo, node):
        if node is None or node.produto.codigo == codigo:
            return node
        elif codigo < node.produto.codigo:
            return self._buscar_produto(codigo, node.esquerda)
        else:
            return self._buscar_produto(codigo, node.direita)

    def listar_produtos(self):
        os.system('clear')
        nome_do_programa()
        if self.raiz is None:
            print('Não há produtos no estoque!')
        else:
            self._listar_produtos(self.raiz)
        voltar_ao_menu_principal()

    def _listar_produtos(self, node):
        if node is not None:
            self._listar_produtos(node.esquerda)
            print(f'Código: {node.produto.codigo} | Nome: {node.produto.nome} | Quantidade: {node.produto.quantidade} | Preço: R${node.produto.preco:.2f}')
            self._listar_produtos(node.direita)

def nome_do_programa():
    print('Ｓｋａｔｅ ｏｒ Ｄｉｅ 🔥\n')

def exibir_opcoes():
    print('1. Adicionar Produto')
    print('2. Remover Produto')
    print('3. Atualizar Estoque')
    print('4. Lista de Estoque')
    print('5. Sair\n')

def opcao_invalida():
    os.system('clear')
    nome_do_programa()
    print('Opção inválida!')
    voltar_ao_menu_principal()

def finalizar_programa():
    os.system('clear')
    print('Finalizando o programa! Até logo ... 😊 \n')

def voltar_ao_menu_principal():
    input('\nPressione qualquer tecla para voltar ao menu: ')

def escolher_opcao(arvore):
    while True:
        os.system('clear')
        nome_do_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                arvore.adicionar_produto()
            elif opcao_escolhida == 2:
                arvore.remover_produto()
            elif opcao_escolhida == 3:
                arvore.atualizar_produto()
            elif opcao_escolhida == 4:
                arvore.listar_produtos()
            elif opcao_escolhida == 5:
                finalizar_programa()
                break
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def main():
    arvore = ArvoreProduto()
    escolher_opcao(arvore)

if __name__ == '__main__':
    main()
