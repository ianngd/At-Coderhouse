from datetime import date, timedelta

def escrever_dia (ent_data):
    data = entrada_data.split('/')
    dia = int(data[0])
    mes = int(data[1])
    ano = int(data[2])
    formatar = date(ano,mes,dia)
    formatado = formatar.strftime('%A')
    return(formatado)

entrada_data = input('DIGITE A DATA DESEJADA (DD/MM/AAAA): ')
print (escrever_dia(entrada_data))