def calc_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input('\nDigite um numero para calcular seu fatorial: '))
resultado = calc_fatorial(numero)
print("O fatorial de", numero, "é", resultado)