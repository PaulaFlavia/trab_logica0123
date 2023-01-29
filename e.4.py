lista_funcionarios = []
id_funcionario = 0

# funções auxiliares:
def cadastrar_funcionario(id_funcionario):
  print('Cadastro de Funcionários')
  print('Id do funcionário {}'.format(consultar_funcionario))
  nome = input('Digite o nome completo do funcionário: ')
  setor = input('Digite o setor de atuação do funcionário: ')
  salario = input('Digite o salário do funcionário: ')
  descricao_funcionario = {
    'Id' : id_funcionario,
    'nome' : nome,
    'setor' : setor,
    'salário': salario,
  }
  lista_funcionarios.append(descricao_funcionario.copy())

def consultar_funcionario():
  print('Menu listagem de Funcionários')
  while True:
    opcao_consultar = input('1- Consultar Todos Funcionários \n' +
                          '2- Consultar Funcionário por Id\n' +
                          '3- Consultar Funcionário por Setor\n' +
                          '4- Retornar\n' +
                          '>> ')
    if opcao_consultar == '1':
      print('Opção consultar todos os Funcionários')
      for funcionario in lista_funcionarios: # funcionario itera toda a lista_funcionarios
        print('................................')
        for key, value in funcionario.items():
          print('{}: {}'.format(key, value))
        print('................................')
    elif opcao_consultar == '2':
      print('opcao consultar funcionario por id')
      id_buscado = int(input('Digite o Id do funcionário desejado: '))
      for funcionario in lista_funcionarios:
        if funcionario['Id'] == id_buscado:
          print('................................')
          for key, value in funcionario.items():
            print('{}: {}'.format(key, value))
          print('................................')
    elif opcao_consultar == '3':
      print('opção consultar funcionário por setor')
      setor_buscado = input('Digite o setor de atuação do funcionário: ')
      for funcionario in lista_funcionarios:
        if funcionario['setor'] == setor_buscado:
          print('................................')
          for key, value in funcionario.items():
            print('{}: {}'.format(key, value))
          print('................................')
    elif opcao_consultar == '4':
      return
    else:
      print('Opção inválida, por favor, tente novamente')
    
def remover_funcionario():
  print('Menu de remoção de Funcionário')
  id_desejado = int(input('Digite o Id do funcionário que deseja remover: '))
  for funcionario in lista_funcionarios:
    if funcionario['Id'] == id_desejado:
      lista_funcionarios .remove(funcionario)
      print('................................')
    for key, value in funcionario.items():
        print('Funcionário removido {}: {}'.format(key, value))
    print('................................')

# programa principal:
print('Bem vindo Tech Head Hunter de Paula F. P. Simionato RU 4307975')
print('Cadastro de Funcionários')
while True:
  opcao_principal = input('1- Cadastrar Funcionário\n' +
                          '2- Consultar Funcionário(s)\n' +
                          '3- Remover Funcionário\n' +
                          '4- Sair\n' +
                          '>> ')
  if opcao_principal == '1':
    id_funcionario = id_funcionario  + 1
    cadastrar_funcionario(id_funcionario)
  elif opcao_principal == '2':
    consultar_funcionario()
  elif opcao_principal == '3':
    remover_funcionario()
  elif opcao_principal == '4':
    break
  else:
    print('Opção inválida, por favor, tente novamente')
    continue