import os

class Paciente:
    def __init__(self, id_paciente, nome, estado_de_saude):
        self.id_paciente = id_paciente
        self.nome = nome
        self.estado_de_saude = estado_de_saude
        self.proximo_paciente = None

class ListaDePacientes:
    def __init__(self):
        self.head = None

    def adicionar_paciente(self):
        os.system('clear')
        nome_do_programa()
        while True:
            try:
                id_paciente = int(input('Digite o ID do paciente: '))
                paciente_atual = self.head
                id_existente = False
                while paciente_atual is not None:
                    if paciente_atual.id_paciente == id_paciente:
                        id_existente = True
                        break
                    paciente_atual = paciente_atual.proximo_paciente
                
                if id_existente:
                    os.system('clear')
                    nome_do_programa()
                    print(f'O ID {id_paciente} já existe! Por favor, escolha outro.\n')
                else:
                    break
            except ValueError:
                os.system('clear')
                nome_do_programa()
                print('Por favor, digite um número válido para o ID.\n')
        
        while True:
            try:
                nome = input('Digite o nome do paciente: ').strip().title()
                if not nome:
                    os.system('clear')
                    nome_do_programa()
                    print('Por favor, digite um nome válido para o paciente!\n')
                else:
                    break
            except ValueError:
                print('Por favor, digite um nome válido para o paciente!\n')
        estados_validos = ['Estável', 'UTI', 'Grave']
        while True:
            estado_de_saude = input('Digite o estado de saúde do paciente (Estável, UTI ou Grave): ').strip().title()
            if estado_de_saude.lower() in [estado.lower() for estado in estados_validos]:
                break
            else:
                os.system('clear')
                nome_do_programa()
                print(f'Estado de saúde inválido! Escolha entre: Estável, UTI ou Grave.\n')
        
        novo_paciente = Paciente(id_paciente, nome, estado_de_saude)
        
        if self.head is None:
            self.head = novo_paciente
        else:
            paciente_atual = self.head
            while paciente_atual.proximo_paciente is not None:
                paciente_atual = paciente_atual.proximo_paciente
            paciente_atual.proximo_paciente = novo_paciente

        print(f'\nO paciente {nome} foi adicionado com sucesso!')
        voltar_ao_menu_principal()

    def remover_paciente(self):
        os.system('clear')
        nome_do_programa()
        if not self.head:
            print('Não há pacientes na lista.')
            voltar_ao_menu_principal()
        else:
            try:
                id_paciente = int(input('Digite o ID do paciente que deseja remover: '))
            except ValueError:
                print('Por favor, digite um número válido.')
                voltar_ao_menu_principal()
                return
            
            if self.head.id_paciente == id_paciente:
                print(f'Paciente {self.head.nome} removido com sucesso.')
                self.head = self.head.proximo_paciente
            else:
                paciente_atual = self.head
                while paciente_atual.proximo_paciente is not None:
                    if paciente_atual.proximo_paciente.id_paciente == id_paciente:
                        print(f'Paciente {paciente_atual.proximo_paciente.nome} removido com sucesso.')
                        paciente_atual.proximo_paciente = paciente_atual.proximo_paciente.proximo_paciente
                        break
                    paciente_atual = paciente_atual.proximo_paciente
                else:
                    print('Paciente não encontrado.')
            voltar_ao_menu_principal()

    def listar_pacientes(self):
        os.system('clear')
        nome_do_programa()
        if not self.head:
            print('Não há pacientes nesta lista.')
        else:
            paciente_atual = self.head
            while paciente_atual is not None:
                print(f'ID: {paciente_atual.id_paciente}, Nome: {paciente_atual.nome}, Estado de saúde: {paciente_atual.estado_de_saude}')
                paciente_atual = paciente_atual.proximo_paciente

        voltar_ao_menu_principal()

def nome_do_programa():
    print('Ｈｏｓｐｉｔａｌ Ｍｕｎｉｃｉｐａｌ 🏥\n')

def exibir_opcoes():
    print('1. Lista de Pacientes')
    print('2. Adicionar Paciente')
    print('3. Remover Paciente')
    print('4. Sair\n')

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

def escolher_opcao(lista_de_pacientes):
    while True:
        os.system('clear')
        nome_do_programa()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                lista_de_pacientes.listar_pacientes()
            elif opcao_escolhida == 2:
                lista_de_pacientes.adicionar_paciente()
            elif opcao_escolhida == 3:
                lista_de_pacientes.remover_paciente()
            elif opcao_escolhida == 4:
                finalizar_programa()
                break
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def main():
    lista_de_pacientes = ListaDePacientes()
    escolher_opcao(lista_de_pacientes)

if __name__ == '__main__':
    main()
