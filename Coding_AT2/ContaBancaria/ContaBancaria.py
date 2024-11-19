# Parte 1 Encapsulamento

# Criacao de uma classe ContaBancaria com os atributos privados
class ContaBancaria:
    def __init__(self, numeroConta, titular):
        # Uso prefixo __ nos atributos para indicar que são privados
        self.__numeroConta = numeroConta
        self.__titular = titular
        # Garantir que o saldo nunca possa ser alterado diretamente de fora da classe
        self.__saldo = 0

    # Implementação dos métodos públicos
    def getNumeroConta(self):
        return self.__numeroConta
    
    def getTitular(self):
        return self.__titular
    
    # Método Consultar o saldo atual
    def getSaldo(self):
        return self.__saldo
    
    def setNumeroConta(self, numeroConta):
        self.__numeroConta = numeroConta
    
    def setTitular(self, titular):
        self.__titular = titular
    
    # Método depositar um valor na conta
    def depositar(self, valor):
        self.__saldo += valor

    # Método Sacar um valor da conta (apenas se houver saldo suficiente)
    def sacar(self, valor):
        if valor > self.__saldo:
            print('Saldo insuficiente para saque.')
        else:
            self.__saldo -= valor
