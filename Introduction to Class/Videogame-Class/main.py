from datetime import date

class Videogame:

  NUM_SERIE = 20180000

  def __init__(self,data_fabricacao=date.today(),marca="Sony",modelo="PS4"):
    self.data_fabricacao = data_fabricacao
    self.marca = marca
    self.modelo = modelo

    self.hd = 500
    self.jogos_instalados = 0
    self.anos_garantia = 1

    Videogame.NUM_SERIE +=1

#Gets and Setters dos metodos 
  def setHD(self,novoHD):
    self.hd = novoHD
  
  def getHD(self):
    return self.hd

  def setJogos(self,numJogos):
    self.jogos_instalados = numJogos
  
  def getNumJogos(self):
    return self.jogos_instalados

  def setGarantia(self,garantia):
    self.anos_garantia = garantia
  
  def getGarantia(self):
    return self.anos_garantia
  
  def showDados(self):
    print(f"Ano de Fabricação: {self.data_fabricacao}")
    print(f"Marca: {self.marca}")
    print(f"Modelo: {self.modelo}")
    print(f"HD: {self.hd} GB")
    print(f"Jogos Instalados: {self.jogos_instalados}")
    print(f"Garantia: {self.getGarantia()} ano")
    print(f"Numero de Serie: {self.NUM_SERIE}")
    print("")
    print("="*30)



v1 = Videogame()
v1.showDados()

v2 = Videogame("2008")
v2.showDados()

v3 = Videogame("2012","Microsoft","Xbox One")
v3.showDados()
