eh_multiplo_dez = lambda x: (x % 10) == 0

numero = int(input('\nConsulte se o valor é multiplo de 10: '))

if eh_multiplo_dez (numero) == True:
    print('\nO NUMERO DIGITADO É MULTIPLO DE 10\n')
else:
    print('\nO NUMERO DIGITADO NÃO É MULTIPLO DE 10\n')
