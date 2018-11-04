class Calculadora:
  DESCRIPTION = "Basic Calculator v1"
  def __init__(self,valor=0):
    self.__undo = 0
    self.__registrador = valor
  
  def getRegistrador(self):
    return self.__registrador

  def somar(self,numero):
    self.__undo = self.__registrador
    self.__registrador += numero

  def multiplicar(self,numero):
    self.__undo = self.__registrador
    self.__registrador = (self.__registrador * numero)
  
  def dividir(self,numero):
    self.__undo = self.__registrador
    self.__registrador = (self.__registrador / numero)
  
  def subtrair(self,numero):
    self.__undo = self.__registrador
    self.__registrador = (self.__registrador - numero)
  
  def reset(self):
    self.__undo = self.__registrador
    self.__registrador = 0
  
  def undo(self):
    self.__registrador = self.__undo
