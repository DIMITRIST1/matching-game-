import random



class Card(object): # Ayth h synarthsh(2) sumbalei sthn Dhmiourgia filwn kai perilambanei diafores sunarthseis pou mas dinoun prosbash sta xarakthristika tous
    
    def __init__(self,symbol,series,value,description,status):
        self.symbol = symbol
        self.series = series
        self.value = value
        self.description = description
        self.status = status

    def getSymbol(self):
        return self.symbol

    def getName(self):
        return self.description

    def getValue(self):
        return self.value

    def getStatus(self):
        return self.status

    def setStatus(self,status):
        self.status = status

    

class Deck(object):
  
  cards =[]

  def build(self):
    for s in ["♣","♠","♦","♥"]:
      for v in range(1,14):
        if v == 1:
          symbol = 'A'
          value = 1
        elif v>=2 and v<=10:
          symbol = str(v)
          value = v
        elif v == 11:
          symbol = 'J'
          value = 10
        elif v == 12:
          symbol = 'Q'
          value = 10
        else:
          symbol = 'K'
          value = 10
        name = symbol+s
        card = Card(symbol,s,value,name,0)
        self.cards.append(card)
   

  def shuffle(self):
    for i in range(len(self.cards)-1,0,-1):
      rand = random.randint(0,i)
      self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i] 

  def ListCreator(self,lev,listcard):
    if lev == 1:
      c = 0
      for i in range(0,4):
        x=0
        while (x<=3):
          card1 = self.cards[c]
          if card1.getSymbol()=='10' or card1.getSymbol()=='J' or card1.getSymbol()=='Q' or card1.getSymbol()=='K':
            listcard[i].append(card1)
            x+=1
          c+=1
    elif lev ==2:
      c=0
      for i in range(0,4):
        x=0
        while(x<=9):
          card1 = self.cards[c]
          if (card1.getSymbol()!='J' and card1.getSymbol()!='Q' and card1.getSymbol()!='K'):
            listcard[i].append(card1)
            x+=1
          c+=1
    elif lev == 3:
      c=0
      for i in range(0,4):
        for j in range(0,13):
          card1 = self.cards[c]
          listcard[i].append(card1)
          c+=1


            
def returnList(L,listcard):
  deck = Deck()
  deck.build()
  deck.shuffle()
  deck.ListCreator(L,listcard)
  return listcard

  
  
    
  
 
    
