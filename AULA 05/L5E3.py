import os
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
        return self.saldo
    
    def sacar (self,valor):
        self.saldo = self.saldo - valor
        return self.saldo 
op = int(1)
conta_corrente = Conta('IANN GABRIEL', 4675)

while op != 0:
    print('TITULAR: ', conta_corrente.titular)
    print('SALDO ATUALIZADO: R$', conta_corrente.saldo)
    op = int(input('\nESCOLHA A OPÇÃO DESEJADA:\n'
           '0 - SAIR\n1 - DEPOSITAR\n2 - SACAR: ')) 
    if  op == 1:
        os.system ('CLS')
        valor = float(input('QUAL VALOR DESEJA DEPOSITAR: '))
        conta_corrente.depositar(valor)
    
    elif op == 2:
        os.system('CLS')
        valor = float(input('QUAL VALOR DESEJA SACAR: '))
        conta_corrente.sacar(valor)
    elif op == 0:
        pass
    else:
        print('\nOPÇÃO INVALIDA. TENTE NOVAMENTE.\n')