# importacao da biblioteca para criação de classes abstrata
from abc import ABC, abstractmethod

#class abstrata, que funciona como inteface
class Conta(ABC): #ABC é uma classe que ja existe, criando a subclasse Conta de ABC. Mas para módulo ela sera um superclasse.

    #interface só possui métodos
    @abstractmethod
    def consultar_saldo(self):
        ... #pode ser substituido por pass ignora esse bloco de comando
    
    @abstractmethod
    def fazer_deposito(self, valor):
        pass
    
    @abstractmethod
    def fazer_saque(self, valor):
        ...

#subclasse conta corrente
class ContaCorrente(Conta):
    #atributos
    def __init__(self, nome, cpf, agencia, conta, saldo):
        self.__nome = nome #todos private
        self.__cpf = cpf
        self.__agencia = agencia
        self.__conta = conta
        self.__saldo = saldo

    #getter
    @property
    def nome(self):
        return self.__nome
    #setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property    
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def agencia(self):
        return self.__agencia
    
    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def conta(self):
        return self.__conta
    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo


# NOTE: par chamar os metodos no programa principal eu preciso chamar os métodos da superclasse dentro da subclasse    

    #metodos da classe abstrata
    def consultar_saldo(self):
        return self.__saldo
    
    def fazer_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo
    
    def fazer_saque(self, valor):
        self.__saldo -= valor
        return self.__saldo
















