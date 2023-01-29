
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