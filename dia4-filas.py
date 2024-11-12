import os

class Pedido:
  def __init__(self, pedido, nome, prato, mesa):
    self.pedido = pedido
    self.nome = nome
    self.prato = prato
    self.mesa = mesa

class FilaDePedidos:
  def __init__(self):
    self.fila_de_pedidos = []
    self.proximo_pedido = 1

  def adicionar_pedido(self):
    os.system('clear')
    nome_do_programa()
    pedido = self.proximo_pedido
    while True:
      try:
        nome = input('Nome do cliente: ').strip().capitalize()
        if not nome:
          os.system('clear')
          nome_do_programa()
          print('Por favor, digite um nome válido para o cliente!\n')
        else:
          break
      except ValueError:
        print('Por favor, digite um nome válido para o cliente!\n')

    while True:
      try:
        prato = input('Prato desejado: ').strip().capitalize()
        if not prato:
          os.system('clear')
          nome_do_programa()
          print('Por favor, digite um prato válido!\n')
        else:
          break
      except ValueError:
        print('Por favor, digite um prato válido!\n')  
    
    while True:
      try:
        mesa = int(input('Número da mesa: '))
        if not mesa:
          os.system('clear')
          nome_do_programa()
          print('Por favor, digite uma mesa válida!\n')
        else:
          break
      except ValueError:
        os.system('clear')
        nome_do_programa()
        print('Por favor, digite uma mesa válida!\n')

    novo_pedido = Pedido(pedido, nome, prato, mesa)
    self.fila_de_pedidos.append(novo_pedido)
    self.proximo_pedido += 1
    print(f'\nPedido de {nome} adicionado a fila!')
    voltar_ao_menu_principal()

  def remover_pedido(self):
    if len(self.fila_de_pedidos) < 1:
      return None
    return self.fila_de_pedidos.pop(0)

  def mostrar_pedidos(self):
    if len(self.fila_de_pedidos) < 1:
      print('Não há pedidos no momento!')
      return
    for pedido in self.fila_de_pedidos:
      print(f'Número: {pedido.pedido} | Nome: {pedido.nome} | Prato: {pedido.prato} | Mesa: {pedido.mesa}')

def nome_do_programa():
    print('Ｃｏｎｔｒｏｌｅ ｄｅ Ｐｅｄｉｄｏｓ 📝\n')

def exibir_opcoes():
    print('\n1. Adicionar Pedido')
    print('2. Remover pedido')
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

def escolher_opcao(fila_de_pedidos):
    while True:
        os.system('clear')
        nome_do_programa()
        fila_de_pedidos.mostrar_pedidos()
        exibir_opcoes()
        try:
            opcao_escolhida = int(input('Escolha uma opção: '))
            if opcao_escolhida == 1:
                fila_de_pedidos.adicionar_pedido()
            elif opcao_escolhida == 2:
                fila_de_pedidos.remover_pedido()
            elif opcao_escolhida == 3:
                finalizar_programa()
                break
            else:
                opcao_invalida()
        except ValueError:
            opcao_invalida()

def main():
    fila_de_pedidos = FilaDePedidos()
    escolher_opcao(fila_de_pedidos)

if __name__ == '__main__':
    main()
