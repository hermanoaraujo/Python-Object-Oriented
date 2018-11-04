from importsConfig import *

## Classe do Baralho
class Deck:
  __numberOfDecks = 0

  def __init__(self):
    self.deck = []
    self.suits = ["\u2661","\u2664","\u2667","\u2662"]
    self.numbers = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    Deck.__numberOfDecks += 1
  
  def createDeck(self):
    
    for i in range(len(self.suits)):
      for j in range(len(self.numbers)):
        self.deck.append(Card(self.numbers[j],self.suits[i]))
          
  def getDeck(self):
    for i in range(len(self.deck)):
      print (self.deck[i])
  
  def shuffleDeck(self):
    shuffle(self.deck)
  
  def distributeCards(self,numberOfPlayers=4):
    self.numberCards = int(len(self.deck)/numberOfPlayers)
    self.cont = 0

    for i in range(numberOfPlayers):
      print("\nPlayer", i+1 , "Received: ",self.numberCards," Cards")
      print("="*35)

      for j in range(self.numberCards):
        print(self.deck[self.cont],)
        self.cont += 1
      print("="*35)

  @classmethod
  def countDecks(cls):
   return cls.__numberOfDecks