from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome, salarioBase):
        self.__nome = nome
        self.__salarioBase = salarioBase
        self.__grauInstrucao = "Não Definido"
        self.__bonificacao = 0

    def getNome(self):
        return self.__nome

    def setNome(self, novoNome):
        self.__nome = novoNome

    def getSalario(self):
        return self.__salarioBase

    def setSalario(self, novoSalario):
        self.__salarioBase = novoSalario

    def getGrauInstrucao(self):
        return self.__grauInstrucao

    def setGrauInstrucao(self,grau):
        self.__grauInstrucao = grau

    def setBonificacao(self,bonus):
        self.__bonificacao = bonus

    def getBonificacao(self):
        return self.__bonificacao

    def __str__(self):
        return f"Sou um objeto da class {self.__class__.__name__},\n Me Chamo: {self.__nome} e ganho {self.__salarioBase}"

    @abstractmethod
    def addBonificacao(self):
        pass

    def contracheque(self):
        return (self.__salarioBase + self.__bonificacao)

class Gerente(Funcionario):

    def addBonificacao(self):

        self.bonus = 0.30

        if (super().getGrauInstrucao() == "Especialista"):
            super().setBonificacao(super().getSalario()*(self.bonus+0.15))
            super().setSalario(super().getSalario()+super().getBonificacao())
        elif (super().getGrauInstrucao() == "Mestre"):
            super().setBonificacao(super().getSalario() * (self.bonus + 0.25))
            super().setSalario(super().getSalario() + super().getBonificacao())
        elif (super().getGrauInstrucao() == "Doutor"):
            super().setBonificacao(super().getSalario() * (self.bonus + 0.50))
            super().setSalario(super().getSalario() + super().getBonificacao())
        else:
            super().setBonificacao(super().getSalario() * self.bonus)
            super().setSalario(super().getSalario() + super().getBonificacao())


class Presidente(Funcionario):

    def addBonificacao(self):

        if (super().getGrauInstrucao() == "Doutor"):
            super().setBonificacao(super().getSalario() * 4)
            super().setSalario(super().getSalario() + super().getBonificacao())
        else:
            super().setBonificacao(super().getSalario() * 2)
            super().setSalario(super().getSalario() + super().getBonificacao())


class Diretor(Funcionario):
    def addBonificacao(self):
        if (super().getGrauInstrucao() == "Especialista"):
            super().setBonificacao(super().getSalario() * 0.15)
            super().setSalario(super().getSalario()+super().getBonificacao())
        elif (super().getGrauInstrucao() == "Mestre"):
            super().setBonificacao(super().getSalario() * 0.25)
            super().setSalario(super().getSalario() + super().getBonificacao())
        elif (super().getGrauInstrucao() == "Doutor"):
            super().setBonificacao(super().getSalario() * 0.50)
            super().setSalario(super().getSalario() + super().getBonificacao())

