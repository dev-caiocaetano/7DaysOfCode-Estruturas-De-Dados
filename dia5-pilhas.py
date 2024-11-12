import os

class Livro:
    def __init__(self, nome, numero_de_paginas):
        self.nome = nome
        self.numero_de_paginas = numero_de_paginas

class PilhaDeLivros:
    def __init__(self):
        self.pilha_de_livros = []

    def adicionar_livro(self):
        os.system('clear')
        nome_do_programa()
        while True:
            try:
                nome = input('Nome do livro: ').strip().capitalize()
                if not nome:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, digite um nome válido para o livro!\n')
                else:
                    break
            except ValueError:
                print('Por favor, digite um nome válido para o livro!\n')
        
        while True:
            try:
                numero_de_paginas = int(input('Número de páginas: '))
                if numero_de_paginas <= 0:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, digite um número de páginas válido (Maior que 0)')
                else:
                    break
            except ValueError:
                os.system('clear')
                nome_do_programa()
                print('Por favor, digite um número de páginas válido (Maior que 0)')
        novo_livro = Livro(nome, numero_de_paginas)
        self.pilha_de_livros.append(novo_livro)
        print(f'\nLivro {nome} adicionado a pilha!')
        voltar_ao_menu_principal()

    def remover_livro(self):
        if len(self.pilha_de_livros) < 1:
            os.system('clear')
            nome_do_programa()
            print('Não há livros para remover!')
            voltar_ao_menu_principal()
            return None
        livro_removido = self.pilha_de_livros.pop()
        os.system('clear')
        nome_do_programa()
        print(f'O livro {livro_removido.nome} foi removido do topo da pilha.')
        voltar_ao_menu_principal()
        return livro_removido
  
    def mostrar_livro_topo(self):
        if len(self.pilha_de_livros) < 1:
            print('A pilha está vazia!\n')
        else:
            livro_topo = self.pilha_de_livros[-1]
            print(f'O livro no topo é: {livro_topo.nome}, com {livro_topo.numero_de_paginas} páginas.\n')

    def mostrar_livros(self):
        if len(self.pilha_de_livros) < 1:
            print('Não há livros na pilha no momento!\n')
            return
        print('Livros na pilha:\n')
        for i, livro in enumerate(reversed(self.pilha_de_livros), 1):
            print(f'{i}. {livro.nome} | {livro.numero_de_paginas} páginas')
        print()

def nome_do_programa():
    print('Ｃｏｎｔｒｏｌｅ Ｂｉｂｌｉｏｔｅｃａｒｉｏ 📝\n')

def exibir_opcoes():
    print('1. Adicionar Livro')
    print('2. Remover Livro')
    print('3. Sair\n')

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

def escolher_opcao(pilha_de_livros):
    while True:
        os.system('clear')
        nome_do_programa()
        pilha_de_livros.mostrar_livro_topo()
        pilha_de_livros.mostrar_livros()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                pilha_de_livros.adicionar_livro()
            elif opcao_escolhida == 2:
                pilha_de_livros.remover_livro()
            elif opcao_escolhida == 3:
                finalizar_programa()
                break
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def main():
    pilha_de_livros = PilhaDeLivros()
    escolher_opcao(pilha_de_livros)

if __name__ == '__main__':
    main()
