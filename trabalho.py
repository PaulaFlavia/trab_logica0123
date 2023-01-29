

# 1 -Enunciado: Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Para calcular o valor total que o deve-se levar em consideração o custo de embalagem conforme a tabela abaixo
# Quantidade	Custo de embalagem para frete
# 0 <= quantidade < 11	R$ 30.00
# 11 <= quantidade < 101	R$ 60.00
# 101 <= quantidade < 1001	R$ 120.00
# quantidade >= 1001	R$ 240.00
# Elabore um programa em Python que:
# Entre com o valor unitário do produto (Lembrar que número decimal é feito com PONTO e não VÍRGULA);
# Entre com a quantidade desse produto;
# O programa deve retornar o valor total sem o custo de embalagem para frete;
# O programa deve retornar o valor total após o custo de embalagem para frete;
# Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 1);
# Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 1000 und.


print('SAUDAÇÕES, Jovem Padawan Bem vindo ao ATACADISTA - Paula Flávia Pagotto Simionato (RU - 4307975)')
unit_price = float(input('Digite o valor do produto desejado(use ponto no lugar da vírgula): '))
amount_product = int(input('Digite a quantidade desejada do produto: '))
gross_price = amount_product * unit_price

portage_price = 0
if(amount_product <11):
    portage_price = 30.0
elif(amount_product >= 11 and amount_product < 101):
    portage_price = 60.0
elif(amount_product >= 101 and amount_product < 1001):
    portage_price = 120.0
else:
    portage_price = 240.0

print('O valor de sua compra sem embalagem para frete é de: {}'.format(gross_price))
print('O valor de sua embalagem para frete  é de: {}'.format(portage_price))
# print('O valor final de sua compra com a embalagem é de: {}'.format(gross_price + portage_price))


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# 2 - Enunciado: Você e sua equipe de programadores foram contratados para desenvolver um app de vendas para uma sorveteria. Você ficou com a parte de desenvolver a interface do cliente para retirada do produto.
# A Sorveteria possui seguinte tabela com o código, descrição, tamanhos e os valores de sorvete:
# Código	Descrição	Tamanho P
# (500 ml)	Tamanho M
# (1000 ml)	Tamanho G
# (2000 ml)
# TR	Sabores Tradicionais	R$ 6,00	R$ 10,00	R$ 18,00
# ES	Sabores Especiais	R$ 7,00	R$ 12,00	R$ 21,00
# PR	Sabores Premium	R$ 8,00	R$ 14,00	R$ 24,00

# Elabore um programa em Python que:
# Entre com o tamanho do pote de sorvete desejado;
# Entre com o código do sorvete desejado;
# Pergunte se o cliente quer pedir mais alguma coisa (se sim repetir a partir do item 1.  Caso contrário ir para próximo passo);
# Encerre a conta do cliente com o valor total;
# Deve-se utilizar estruturas if, elif e else (EXIGÊNCIA 1 de 3);
# Se a pessoa digitar um TAMANHO de sorvete e/ou   código diferente dos da tabela printar na tela: ‘TAMANHO ou CÓDIGO inválido(s)’ e voltar para o menu (EXIGÊNCIA 2 de 3);
# Deve-se utilizar while, break, continue (EXIGÊNCIA 3 de 3);
# (DICA: utilizar o continue dentro else que verifica a opção inválida)
# (DICA: utilizar o break dentro if que verifica a opção sair)
# Colocar um exemplo de SAIDA DE CONSOLE com 3 (três) sorvetes
# Colocar um exemplo de SAIDA DE CONSOLE com erro tamanho
# Colocar um exemplo de SAIDA DE CONSOLE com erro código


print('                JOVENS PADAWANS, BEM VINDOS A SORVETERIA da Paula Flávia Pagotto Simionato               ')
print('------------------------------------------------MENU-----------------------------------------------------')
print('|  Código  |    SABORES        |    TAMANHO-P(5OOML)     |   TAMANHO-M(10OOML)   |   TAMANHO-G(20OOML)  |')
print('|    TR    |  TRADICIONAIS     |        R$  6,00         |       R$  7,00        |       R$  8,00       |')
print('|    ES    |   ESPECIAIS       |        R$ 10,00         |       R$ 12,00        |       R$ 14,00       |')
print('|    PR    |    PREMIUN        |        R$ 18,00         |       R$ 21,00        |       R$ 24,00       |')
print('---------------------------------------------------------------------------------------------------------')

acumulador = 0
while True:
    tamanho = input('Digite o tamanho do sorvete que deseja(P/M/G): ')
    tamanho = tamanho.upper()
    if (tamanho != 'P' and tamanho != 'M' and tamanho != 'G'):
        print('Opção inválida. Os tamanhos existentes são apenas pequeno - P, médio - M, e grande - G.')
        continue
    codigo = input('Por favor, digite o código do sorvete escolhido(TR, ES, PR): ')
    codigo = codigo.upper()
    if (codigo != 'TR' and codigo != 'ES' and codigo != 'PR'):
        print('Opção inválida, por favor escolha ente TR, ES e PR')
        continue
    if codigo == 'TR' and tamanho == 'P':
        print('Você escolheu um sorvete TRADICIONAL de tamanho Pequeno')
        acumulador = acumulador + 6.0
    elif codigo == 'TR' and tamanho == 'M':
        print('Você escolheu um sorvete TRADICIONAL de tamanho Médio')
        acumulador = acumulador + 7.0
    elif codigo == 'TR' and tamanho == 'G':
        print('Você escolheu um sorvete TRADICIONAL de tamanho Grande')
        acumulador = acumulador + 8.0

    if codigo == 'ES' and tamanho == 'P':
        print('Você escolheu um sorvete ESPECIAL de tamanho Pequeno')
        acumulador = acumulador + 10.0
    elif codigo == 'ES' and tamanho == 'M':
        print('Você escolheu um sorvete ESPECIAL de tamanho Médio')
        acumulador = acumulador + 12.0
    elif codigo == 'ES' and tamanho == 'G':
        print('Você escolheu um sorvete ESPECIAL de tamanho Grande')
        acumulador = acumulador + 14.0

    if codigo == 'PR' and tamanho == 'P':
        print('Você escolheu um sorvete PREMIUM de tamanho Pequeno')
        acumulador = acumulador + 18.0
    elif codigo == 'PR' and tamanho == 'M':
        print('Você escolheu um sorvete PREMIUM de tamanho Médio')
        acumulador = acumulador + 21.0
    elif codigo == 'PR' and tamanho == 'G':
        print('Você escolheu um sorvete PREMIUM de tamanho Grande')
        acumulador = acumulador + 24.0

    continuar_pedindo = input(
        'Deseja continuar comprando sorvetes?(S/ ou digite qualquer outra tecla): ')
    continuar_pedindo = continuar_pedindo.upper()
    if continuar_pedindo == 'S':
        continue # continue retorna ao inicio do laço
    else:
        print('Valor total de sua compra: R${:.2f}'.format(acumulador))
        break


# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

# 3 -Enunciado: Imagina-se que você e sua equipe foram contratados por uma empresa preste serviços de limpeza para desenvolver a solução de software. Você ficou encarregado da parte de interação com o usuário.
# O valor que a empresa cobra por limpeza é dado pela seguinte equação:

# Em que cada uma das variáveis que compõe o preço total é quantizada da seguinte maneira:
# Quadro 1: Metragem versus valor
# Metragem (m²)	Valor (R$)
# 30 <= metragem < 300	60 + 0.3 *  metragem
# 300 <= metragem < 700	120 + 0.5 *  metragem
# Outros valores	Não são aceitos
# 	Quadro 2: Tipo versus multiplicador
# Tipo	Multiplicador
# B – Básica - Indicada para sujeiras semanais ou quinzenais	1.00
# C – Completa - Indicada para sujeiras antigas e/ou não rotineiras	1.30


# Quadro 3: Adicionais versus valor
# Adicionais	Valor (R$)
# 0- Não desejo mais nada (encerrar)	0,00
# 1- Passar 10 peças de roupas - R$ 10.00	10,00
# 2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00	12,00
# 3- Limpeza de 1 Geladeira/Freezer - R$ 20,00	20,00

# Elabore um programa em Python que:
# Pergunte a metragem (em m²);
# Se o valor for 30 e 299,deve-se printar: “É necessário contratar 1 pessoa”
# Se o valor for 300 e 699, deve-se printar “É necessário contratar 2 pessoas”
# Se o valor passar 699, for menor que 30 ou for diferente de número; deve-se repetir a pergunta;
# Pergunte a tipo de limpeza. Se digitar uma opção não válida deve repetir a pergunta
# Pergunte o adicional. Deve-se perguntar ao usuário se desejada mais algum adicional até digitar ele 0
# Encerre o total a ser pago com base na equação desse enunciado;
# Deve-se codificar uma função metragem_limpeza() (EXIGÊNCIA 1 de 3);
# Deve-se perguntar dentro da função a metragem da porção (em m²);
# Deve-se ter um if/else ou if/elif ou if/else/elif para verificar se o usuário não digitou uma metragem fora da faixa com que o empresa trabalha;
# Deve-se ter try/except para o caso do usuário digitar um valor não numérico;
# Deve-se retornar o valor em (RS) conforme a Quadro 1
# Deve-se codificar uma função tipo_limpeza() (EXIGÊNCIA 2 de 3);
# Deve-se perguntar dentro da função a opção desejada;
# Deve-se ter um if/elif/else para verificar as opções possíveis ou não;
# Deve-se retornar o multiplicador conforme o Quadro 2
# Deve-se codificar uma função adicional_limpeza()  (EXIGÊNCIA 3 de 3);
# Deve-se perguntar dentro se deseja ou não mais algum adicional



# Funções auxiliares

# def metragem_limpeza():
#   print('================================== MENU 1 de 3 =====================================')
#   while True:
#     try:
#       metragem = int(input('Qual o tamanho da área que deseja limpar? (Trabalhamos apenas com áreas apartir de 30 m2 até no máximo de 700m2): '))
#       if(30 <= metragem < 300):
#         return (metragem * 0.3) + 60 
#       elif(300 <= metragem < 700):
#         return (metragem * 0.5) + 120
#       else:
#         print('Só trabalhamos com áreas entre 30 e 700 m2')
#         continue # continue retorna ao inicio do laço
#     except ValueError:# caso usuário digite um número não inteiro
#       print('Por favor não, use vírgulas ou pontos, digite um numero inteiro entre 30 e 700')
           
# def tipo_limpeza():
#   print('================================== MENU 2 de 3 =====================================')
#   while True:
#     opcao = input('Qual a tipo de limpeza desejada?\n'+
#                   'B- Básica: indicada para sujeiras semanais ou quinzenais\n'+
#                   'C- Completa: indicada para sujeiras antigas e/ou não rotineiras\n'+
#                   '>> ')
#     opcao = opcao.lower()
#     opcao = opcao.strip()
#     if opcao == 'b':
#       return 1.00
#     elif opcao == 'c':
#       return 1.30
#     else:
#       print('Oooops as opções existenten são apenas: b = básica/ e c = Completa')
#       continue # continue retorna ao inicio do laço
    
# def adcionar_servicos():
#   print('================================== MENU 3 de 3 =====================================')
#   acumulador = 0
#   while True:
#     adcionar_servicos = input('Temos vários serviços adicionais, deseja escolher algum?/n'+
#                             '0- Não desejo serviços extras (encerrar pedido)\n'             
#                             '1- Passar 10 peças de roupas - R$ 10,00\n' +                                           
#                             '2- Limpeza de 1 forno/micro-ondas - R$ 12,00\n' +                               
#                             '3- Limpeza de 1 geladeira/freezer - R$ 20,00\n' +                                
#                             '  ' )
#     if adcionar_servicos == '0':
#       return acumulador
#       continue
#     elif adcionar_servicos == '1':
#        acumulador += 10
#        continue
#     elif adcionar_servicos == '2':
#       acumulador += 10
#       continue
#     elif adcionar_servicos == '3':
#       acumulador += 12
#       continue
#     else:
#       print('Por favor, digite apenas opções entre 0 e 3')                                    
#       print(acumulador)
# # main programmam
# print('==================== LIMPA TUDO - Paula F. P. Simionato - RU 4307975 ====================')

# metragem = metragem_limpeza()
# tipo = tipo_limpeza()
# adcionais = adcionar_servicos()
# total = (metragem * tipo) + adcionais
# print('O total de seu serviço é de: R$ {:.2f} (Seu pedido: R$ {:.2f} pelo serviço, multiplicado por {} pelo tipo escolhido e R$ {:.2f} pelos serviços adicionais'.format(total, metragem, tipo, adcionais))



# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


# 4-Enunciado: Imagina-se que você está desenvolvendo um software de controle de funcionários para uma empresa de RH. Este software deve ter o seguinte menu e opções:
# Cadastrar Funcionário
# Consultar Funcionários(s)
# Consultar Todas as Funcionários
# Consultar Funcionário por Id
# Consultar Funcionário(s) por Setor
# Retornar
# Remover Funcionário
# Sair
# Elabore um programa em Python que:
# Deve-se codificar uma função cadastrar_funcionario(id) (EXIGÊNCIA 1);
# Essa função recebe como parâmetro um id exclusivo para cada funcionário cadastrado (DICA: utilize um contador como parâmetro)
# Dentro da função perguntar o nome do funcionário;
# Dentro da função perguntar o setor do funcionário;
# Dentro da função perguntar o salário do funcionário
# Cada funcionário cadastrado deve ter os seus dados armazenados num DICIONÁRIO (DICA: Conferir material escrito da p. 22 até p24  da AULA 06)
# Deve-se codificar uma função consultar_funcionários()(EXIGÊNCIA 2);
# Dentro da função ter um menu com as seguintes opções:
# Consultar Todos os Funcionários
# Consultar Funcionário por Id
# Consultar Funcionário(s) por Setor
# Retornar
# Deve-se codificar uma função remover_funcionario() (EXIGÊNCIA 3);
# Dentro da função perguntar qual o código do funcionário que se deseja remover do cadastro (da lista de dicionário)
# Colocar um exemplo de SAIDA DO CONSOLE com o cadastro de 3 (ou mais) funcionários . Sendo que 2 delas do mesmo setor – ver figura 1
# Colocar um exemplo de SAIDA DO CONSOLE com a consulta a todos os funcionários cadastrados – ver figura 2
# Colocar um exemplo de SAIDA DO CONSOLE com uma consulta por id – ver figura 3
# Colocar um exemplo de SAIDA DO CONSOLE com uma consulta por setor – ver figura 4
# Colocar um exemplo de SAIDA DO CONSOLE ao remover um funcionário cadastrado e mostrando depois todos os funcionários – ver figura 5



# variáves globais:

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
    
# funcionario itera toda a lista_produtos