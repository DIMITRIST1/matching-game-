
from defs import printList, giveAnswer
from cards import Card,Deck


def Compare(answer1,answer2,list1,listcard,s,k,level): # Ayth h sunarhthsh(4)kanei tis sugkriseis metaju twn kartwn kai upologizei tous bathmous analoga me thn kathe periptwsh

    an1_0=int(answer1[0])-1
    if len(answer1)==3:
        an1_2=int(answer1[2])-1
    elif len(answer1)==4:
        an1_2=int(answer1[2]+answer1[3])-1

    an2_0=int(answer2[0])-1
    if len(answer2)==3:
        an2_2=int(answer2[2])-1
    elif len(answer2)==4:
        an2_2=int(answer2[2]+answer2[3])-1

    
    if listcard[an1_0][an1_2].getSymbol() == listcard[an2_0][an2_2].getSymbol():
        s[k-1]=s[k-1]+listcard[an1_0][an1_2].getValue()
        print(' Επιτυχές ταίριασμα +'+str(listcard[an1_0][an1_2].getValue())+' πόντοι! Παίκτη '+str(k)+' έχεις συνολικά '+str(s[k-1])+' πόντους.')
        if listcard[an1_0][an1_2].getSymbol()=="J":
            k-=1
        elif listcard[an1_0][an1_2].getSymbol()=="K":
            k+=1

    elif (listcard[an1_0][an1_2].getSymbol()=="K" and listcard[an2_0][an2_2].getSymbol()=="Q") or (listcard[an1_0][an1_2].getSymbol()=="Q" and listcard[an2_0][an2_2].getSymbol()=="K"):
        
        answer3 = giveAnswer(level,k,3,listcard)
        an3_0=int(answer3[0])-1
        if len(answer3)==3:
            an3_2=int(answer3[2])-1
        elif len(answer3)==4:
            an3_2=int(answer3[2]+answer3[3])-1

        list1[an3_0][an3_2] =listcard[an3_0][an3_2].getName()
        printList(level,list1)

        if listcard[an1_0][an1_2].getSymbol() == listcard[an3_0][an3_2].getSymbol():
            s[k-1]=s[k-1]+listcard[an1_0][an1_2].getValue()
            list1[an2_0][an2_2]="X"
            print(' Επιτυχές ταίριασμα +'+str(listcard[an1_0][an1_2].getValue())+' πόντοι! Παίκτη '+str(k)+' έχεις συνολικά '+str(s[k-1])+' πόντους.')
        elif listcard[an2_0][an2_2].getSymbol()==listcard[an3_0][an3_2].getSymbol():
            s[k-1]=s[k-1]+listcard[an2_0][an2_2].getValue()
            list1[an1_0][an1_2]="X"
            print(' Επιτυχές ταίριασμα +'+str(listcard[an2_0][an2_2].getValue())+' πόντοι! Παίκτη '+str(k)+' έχεις συνολικά '+str(s[k-1])+' πόντους.')
        else:
            listcard[an1_0][an1_2].setStatus(0)
            listcard[an2_0][an2_2].setStatus(0)
            listcard[an3_0][an3_2].setStatus(0)
            list1[an1_0][an1_2]="X"
            list1[an2_0][an2_2]="X"
            list1[an3_0][an3_2]="X"

    else:
        listcard[an1_0][an1_2].setStatus(0)
        listcard[an2_0][an2_2].setStatus(0)
        list1[an1_0][an1_2]="X"
        list1[an2_0][an2_2]="X"

    return k
    
          
