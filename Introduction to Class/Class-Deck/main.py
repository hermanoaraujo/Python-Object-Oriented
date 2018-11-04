from importsConfig import *

#      Hermano Araújo
#       13/10/2018


while True:
  print(colored('='*40,'yellow'))
  print('''
  \t Card Game Version 1.4
           _____
          |A .  | _____
          | /.\ ||K ^  | _____
          |(_._)|| / \ ||Q _  | _____
          |  |  || \ / || ( ) ||J_ _ |
          |____A||  .  ||(_'_)||( v )|
                 |____K||  |  || \ / |
                        |____Q||  .  |
                               |____J|                              
  ''')
  print(colored('='*40,'yellow'))
  print(colored("\t[1] - Play Card Game","cyan"))
  print(colored("\t[2] - Decks and Cards Mounted","cyan"))
  print(colored("\t[3] - Credits",'cyan'))
  option = int(input("\nEnter an option: "))
  if(option == 1):
    d = Deck()
    d.createDeck()
    d.shuffleDeck()
    numPlayers = input("Enter a number os players, Default 4 players: ")
    if (numPlayers is not ""):
      d.distributeCards(int(numPlayers))
    else:
      d.distributeCards()
  elif(option == 2):
    print(colored('='*40,'yellow'))
    print("\tDecks: ",Deck.countDecks())
    print("\tCards: ",Card.countCards())
  elif(option == 3):
    print(colored('='*40,'magenta'))
    print(colored("Deck Game V1.4 - Hermano Araújo",'cyan'))
    print(colored('='*40,'magenta'))