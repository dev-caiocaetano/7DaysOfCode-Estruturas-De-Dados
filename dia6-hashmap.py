import os

class Jogo:
    def __init__(self):
        self.pontuacao = {}

    def adicionar_jogador(self):
        os.system('clear')
        nome_do_programa()
        while True:
            usuario = input('Qual o nome do jogador?: ').strip().capitalize()
            if not usuario:
                os.system('clear')
                nome_do_programa()
                print('O nome do jogador não pode ser vazio! Tente novamente.\n')
            elif usuario in self.pontuacao:
                os.system('clear')
                nome_do_programa()
                print(f'O jogador {usuario} já está na lista.\n')
                
            else:
                self.pontuacao[usuario] = 0
                os.system('clear')
                nome_do_programa()
                print(f'Jogador {usuario} adicionado com sucesso!')
                voltar_ao_menu_principal()
                break

    def atualizar_pontuacao(self):
        os.system('clear')
        nome_do_programa()
        if len(self.pontuacao) == 0:
            print('Não há jogadores nesta rodada no momento!')
            voltar_ao_menu_principal()
        else:
            while True:
                usuario = input('Qual o nome do jogador para atualizar a pontuação?: ').strip().capitalize()
                if not usuario:
                    os.system('clear')
                    nome_do_programa()
                    print('O nome do jogador não pode ser vazio! Tente novamente.\n')
                elif usuario in self.pontuacao:
                    try:
                        os.system('clear')
                        nome_do_programa()
                        pontos = input(f'Quantos pontos deseja adicionar para {usuario}?: ').strip()
                        if not pontos:
                            os.system('clear')
                            nome_do_programa()
                            print('A pontuação não pode ser vazia! Tente novamente.\n')
                        else:
                            os.system('clear')
                            nome_do_programa()
                            pontos = int(pontos)
                            self.pontuacao[usuario] += pontos
                            print(f'Pontuação de {usuario} atualizada para {self.pontuacao[usuario]} pontos.')
                            voltar_ao_menu_principal()
                            break
                    except ValueError:
                        os.system('clear')
                        nome_do_programa()
                        print('Por favor, insira um valor numérico válido para os pontos.\n')
                else:
                    os.system('clear')
                    nome_do_programa()
                    print(f'Jogador {usuario} não encontrado.\n')

    def remover_jogador(self):
        os.system('clear')
        nome_do_programa()
        if len(self.pontuacao) == 0:
            print('Não há jogadores nesta rodada no momento!')
            voltar_ao_menu_principal()
        else:    
            usuario = input('Qual o nome do jogador que deseja remover?: ').strip().capitalize()
            if not usuario:
                os.system('clear')
                nome_do_programa()
                print('O nome do jogador não pode ser vazio!')
            elif usuario in self.pontuacao:
                del self.pontuacao[usuario]
                os.system('clear')
                nome_do_programa()
                print(f'Jogador {usuario} removido com sucesso!')
            else:
                os.system('clear')
                nome_do_programa()
                print(f'O jogador {usuario} não está na lista.')

    def listar_jogadores(self):
        os.system('clear')
        nome_do_programa()
        if len(self.pontuacao) == 0:
            print('Não há jogadores nesta rodada no momento!')
            voltar_ao_menu_principal()
        else:
            ranking = sorted(self.pontuacao.items(), key=lambda x: x[1], reverse=True)
            for usuario, pontos in ranking:
                print(f'{usuario}: {pontos} pontos')
            voltar_ao_menu_principal()

    def mostrar_vencedor(self):
        os.system('clear')              
        nome_do_programa()
        print('Grande vencedor!!\n')
        if len(self.pontuacao) == 0:
            print('Não há jogadores para determinar um vencedor.')
            voltar_ao_menu_principal()
        else:
            max_pontos = max(self.pontuacao.values())
            vencedores = [usuario for usuario, pontos in self.pontuacao.items() if pontos == max_pontos]
            if len(vencedores) > 1:
                print(f'Há um empate! Os vencedores são: {', '.join(vencedores)} com {max_pontos} pontos cada.')
            else:
                print(f'O jogador {vencedores[0]} venceu o jogo com {max_pontos} pontos!')
            voltar_ao_menu_principal()

def nome_do_programa():
    print('Ｐｏｎｔｕａｄｏｒ\n')

def exibir_opcoes():
    print('1. Adicionar Jogador')
    print('2. Remover Jogador')
    print('3. Listar Jogadores')
    print('4. Atualizar Pontuação')
    print('5. Mostrar vencedor')
    print('6. Sair\n')

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

def escolher_opcao(jogo):
    while True:
        os.system('clear')
        nome_do_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                jogo.adicionar_jogador()
            elif opcao_escolhida == 2:
                jogo.remover_jogador()
            elif opcao_escolhida == 3:
                jogo.listar_jogadores()
            elif opcao_escolhida == 4:
                jogo.atualizar_pontuacao()
            elif opcao_escolhida == 5:
                jogo.mostrar_vencedor()
            elif opcao_escolhida == 6:
                finalizar_programa()
                break
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def main():
    jogo = Jogo()
    escolher_opcao(jogo)

if __name__ == '__main__':
    main()
