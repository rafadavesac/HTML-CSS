print('Leticia Chaves Porto')
sabor=input('Entre com sabor desejado (CP/AC): ')


if sabor == 'cp' or sabor == 'ac' or sabor == 'CP' or sabor == 'AC':
    tam=input('Entre com o tamanho desejado: ')
    if sabor =='cp' or sabor=='CP':
        s='Cupuaçu'

    elif sabor =='ac' or sabor=='AC':
        s='Açaí'
else:
    print('Sabor inválido. Tente novamente')
    
if tam=='P' or tam=='M' or tam=='G' or tam=='p' or tam=='m' or tam=='g':
    if tam=='P' or tam=='p':
        t='P'
        if s=='Cupuaçu':
            valor=9
        elif s=='Açaí':
            valor=11
        print(f'Você pediu um {s} no tamanho {t}: R$ {valor}.00')
    elif tam=='m' or tam=='M':
        t='M'
        if s=='Cupuaçu':
            valor=14
        elif s=='Açaí':
            valor=16
        print(f'Você pediu um {s} no tamanho {t}: R$ {valor}.00')
    elif tam=='g' or tam=='G':
        t='G'
        if s=='Cupuaçu':
            valor=18
        elif s=='Açaí':
            valor=20
        print(f'Você pediu um {s} no tamanho {t}: R$ {valor}.00')
    else:
        print('Tamanho inválido. Tente novamente')

d=input('Deseja mais alguma coisa? (S/N):')
if d != 's' and d!='S':
    print(f'O valor total a ser pago: {valor}')

while d=='s' or d=='S':
    if sabor == 'cp' or sabor == 'ac' or sabor == 'CP' or sabor == 'AC':
        tam=input('Entre com o tamanho desejado: ')
        if sabor =='cp' or sabor=='CP':
            s='Cupuaçu'
        elif sabor =='ac' or sabor=='AC':
            s='Açaí'
        else:
            print('Sabor inválido. Tente novamente')
    if tam=='P' or tam=='M' or tam=='G' or tam=='p' or tam=='m' or tam=='g':
        if tam=='P' or tam=='p':
            t='P'
            if s=='Cupuaçu':
                valor=9
            elif s=='Açaí':
                valor=11
            print(f'Você pediu um {s} no tamanho {t}: R$ {valor}.00')
        elif tam=='m' or tam=='M':
            t='M'
            if s=='Cupuaçu':
                valor=14
            elif s=='Açaí':
                valor=16
            print(f'Você pediu um {s} no tamanho {t}: R$ {valor}.00')
        elif tam=='g' or tam=='G':
            t='G'
            if s=='Cupuaçu':
                valor=18
            elif s=='Açaí':
                valor=20
            print(f'Você pediu um {s} no tamanho {t}: R$ {valor}.00')
        else:
            print('Tamanho inválido. Tente novamente')
    break
d=input('Deseja mais alguma coisa? (S/N):')

        

