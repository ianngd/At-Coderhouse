soma = 0 
frase = input('DIGITE UMA FRASE:')
palavras = frase.split()

for i in range (len(palavras)):
    print (palavras[i] ,': TEM {} CARACTERE(S)\n'.format(len(palavras[i])))
    soma += int (len (palavras[i]))

print ('\n\nTOTAL DE {} CARACTERE(S)'.format(soma))