from defs import printList, printListcard, giveAnswer, giveLevel, CardsOpen, maxlist
from cards import returnList,Card,Deck
from maindef import main

def game(): #einai h basikh mas sunarthsh(1) h opoia arxika dhmiourgei tous pinakes me ta x kai kalei mia sunarthsh gia to kathe level
    print("Καλωσήλθατε στο Matching Game")
    player=input("Δώστε αριθμό παικτών:")
    p=int(player)
    level=giveLevel()

    result=[]
    for i in range(0,p):
        result.append(0)
    
    list1=[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","X","X","X"]]
    list2=[["X","X","X","X","X","X","X","X","X","X",],["X","X","X","X","X","X","X","X","X","X",],["X","X","X","X","X","X","X","X","X","X",],["X","X","X","X","X","X","X","X","X","X",]]
    list3=[["X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","X","X","X","X"]]
    
    listcard = [[],[],[],[]]
    returnList(level,listcard)
    printListcard(level,listcard)
    
    
    if level==1:
        
        main(level,list1,listcard,p,result)
     
    elif level==2:

        main(level,list2,listcard,p,result)

    elif level==3:
    
        main(level,list3,listcard,p,result)

game()
