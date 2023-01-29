print('        JOVENS PADAWANS, BEM VINDOS A SORVETERIA da Paula Flávia Pagotto Simionato (RU-4307975)          ')
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
        print('TAMANHO INVÁLIDO. Os tamanhos existentes são apenas pequeno - P, médio - M, e grande - G.')
        continue
    codigo = input('Por favor, digite o código do sorvete escolhido(TR, ES, PR): ')
    codigo = codigo.upper()
    if (codigo != 'TR' and codigo != 'ES' and codigo != 'PR'):
        print('CÓDIGO INVALIDO, por favor escolha ente TR, ES e PR')
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