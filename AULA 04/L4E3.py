nomes= ['João Carlos','Maria Eduarda','Ana Rute','Ana Clara']


def primeiro_nome(nome_completo):
    nome=nome_completo.split()
    p_nome=nome[0]
    return p_nome

entrada_nome_completo=input('\nDIGITE O NOME COMPLETO: ')
print(primeiro_nome (entrada_nome_completo))

p_nomes=list(map(primeiro_nome,nomes))
print (p_nomes)