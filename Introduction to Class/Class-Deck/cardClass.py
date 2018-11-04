from importsConfig import *

## Classe cards
class Card:
  __numberOfCards = 0
  def __init__(self,number,suit):
    self.__number = number
    self.__suit = suit

    Card.__numberOfCards += 1

  def __str__(self): 
    return "------\n|"+str(self.__number)+"   |\n| of |\n|   "+str(self.__suit)+"|\n------"
  
  @classmethod
  def countCards(cls):
   return cls.__numberOfCards