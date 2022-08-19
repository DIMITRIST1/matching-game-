from defs import printList, printListcard, giveAnswer, giveLevel, CardsOpen, maxlist
from cards import Card,Deck
from CompareCard import Compare






def main(level,list,listcard,p,result): # Ayth h sunarthsh(3) kaleite gia kathe diaforetiko level h opoia pernei tis antistoixes apanthseis twn paiktwn kai kalei thn sunarthsh compare gia na kanei tis sugkriseis kai na upologisei tous bathmous me bash tis eidikes periptwseis
    cards = False                         
    while cards==False:
        k=1
        while k<=p:
            
            printList(level,list)
                       
            answer1=giveAnswer(level,k,1,listcard)
            an1_0=int(answer1[0])-1
            if len(answer1)==3:
                an1_2=int(answer1[2])-1
            elif len(answer1)==4:
                an1_2=int(answer1[2]+answer1[3])-1

            list[an1_0][an1_2]=listcard[an1_0][an1_2].getName()
            listcard[an1_0][an1_2].setStatus(1)
            printList(level,list)
                        
            answer2=giveAnswer(level,k,2,listcard)
                        
            an2_0=int(answer2[0])-1
            if len(answer2)==3:
                an2_2=int(answer2[2])-1
            elif len(answer2)==4:
                an2_2=int(answer2[2]+answer2[3])-1
                        
            list[an2_0][an2_2]=listcard[an2_0][an2_2].getName()
            listcard[an2_0][an2_2].setStatus(1)
            printList(level,list)
                    
            k=Compare(answer1,answer2,list,listcard,result,k,level)
          
            k+=1

            cards=CardsOpen(listcard,level)
            if cards==True:
                break

        cards=CardsOpen(listcard,level)

    print("Τέλος παιχνιδιού!")
    pointer=maxlist(result)
    print("Νικητής είναι ο παίκτης "+str(pointer-1)+" με "+str(result[pointer])+" βαθμού!")
