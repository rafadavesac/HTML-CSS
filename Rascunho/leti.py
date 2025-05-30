print('Bem-vindo a Loja da Leticia Chaves Porto')
valor=float(input('Entre com o valor do produto: '))
quantia=float(input('Entre com a quantidade do produto: '))

total= valor*quantia
desconto=0

if total < 2500:
    desconto=total
elif 2500<= total < 6000:
    desconto=(total*4)/100 
elif 6000 <= total < 10000:
    desconto=(total*7)/100
else:
    desconto=(total*11)/100

valor_com_desconto=total-desconto

print(f'O valor SEM desconto: R${total}')
print(f'O valor COM desconto: R${valor_com_desconto}')

