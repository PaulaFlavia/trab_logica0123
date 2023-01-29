# Funções auxiliares

def metragem_limpeza():
  print('================================== MENU 1 de 3 =====================================')
  while True:
    try:
      metragem = int(input('Qual o tamanho da área que deseja limpar? (Trabalhamos apenas com áreas apartir de 30 m2 até no máximo de 700m2): '))
      if(30 <= metragem < 300):
        return (metragem * 0.3) + 60 
      elif(300 <= metragem < 700):
        return (metragem * 0.5) + 120
      else:
        print('Só trabalhamos com áreas entre 30 e 700 m2')
        continue # continue retorna ao inicio do laço
    except ValueError:# caso usuário digite um número não inteiro
      print('Por favor não, use vírgulas ou pontos, digite um numero inteiro entre 30 e 700')
           
def tipo_limpeza():
  print('================================== MENU 2 de 3 =====================================')
  while True:
    opcao = input('Qual a tipo de limpeza desejada?\n'+
                  'B- Básica: indicada para sujeiras semanais ou quinzenais\n'+
                  'C- Completa: indicada para sujeiras antigas e/ou não rotineiras\n'+
                  '>> ')
    opcao = opcao.lower()
    opcao = opcao.strip()
    if opcao == 'b':
      return 1.00
    elif opcao == 'c':
      return 1.30
    else:
      print('Oooops as opções existenten são apenas: b = básica/ e c = Completa')
      continue # continue retorna ao inicio do laço
    
def adcionar_servicos():
  print('================================== MENU 3 de 3 =====================================')
  acumulador = 0
  while True:
    adcionar_servicos = input('Temos vários serviços adicionais, deseja escolher algum?/n'+
                            '0- Não desejo serviços extras (encerrar pedido)\n'             
                            '1- Passar 10 peças de roupas - R$ 10,00\n' +                                           
                            '2- Limpeza de 1 forno/micro-ondas - R$ 12,00\n' +                               
                            '3- Limpeza de 1 geladeira/freezer - R$ 20,00\n' +                                
                            '  ' )
    if adcionar_servicos == '0':
      return acumulador
      continue
    elif adcionar_servicos == '1':
       acumulador += 10
       continue
    elif adcionar_servicos == '2':
      acumulador += 10
      continue
    elif adcionar_servicos == '3':
      acumulador += 12
      continue
    else:
      print('Por favor, digite apenas opções entre 0 e 3')                                    
      print(acumulador)
# main programmam
print('==================== LIMPA TUDO - Paula F. P. Simionato - RU 4307975 ====================')

metragem = metragem_limpeza()
tipo = tipo_limpeza()
adcionais = adcionar_servicos()
total = (metragem * tipo) + adcionais
# print('O total de seu serviço é de: R$ {:.2f} (Seu pedido: R$ {:.2f} pelo serviço, multiplicado por {} pelo tipo escolhido e R$ {:.2f} pelos serviços adicionais'.format(total, metragem, tipo, adcionais))