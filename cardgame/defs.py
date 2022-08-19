from cards import Card,Deck




def printList(level,list): # H sugkekrimenh sunarthsh ektupwnei toys pinakes me ta x kai tis diafores allages poy exoyn ginei kata thn diarkeia poy trexei to programma
    n=1
    for i in range(0,4):
        str1="   "
        if i==0:
            if level==1:
                print("    1    2    3    4    ")
            elif level==2:
                print("    1    2    3    4    5    6    7    8    9    10    ")
            elif level==3:
                print("    1    2    3    4    5    6    7    8    9    10   11   12   13   ")
        for j in range(0,len(list[0])):
            if j==0:
                if len(list[i][j])==3:
                    str1=str(n)+str1+str(list[i][j])+"  "
                elif len(list[i][j])==2:
                    str1=str(n)+str1+str(list[i][j])+"   "
                elif len(list[i][j])==1:
                    str1=str(n)+str1+str(list[i][j])+"    "
            else:    
                if len(list[i][j])==3:
                    str1=str1+str(list[i][j])+"  "
                elif len(list[i][j])==2:
                    str1=str1+str(list[i][j])+"   "
                elif len(list[i][j])==1:
                    str1=str1+str(list[i][j])+"    "
        print(str1)
        print("\n")
        n=n+1
   
def printListcard(level,listcard):
    n=1
    for i in range(0,4):
        str1="  "
        if i==0:
            if level==1:
                print("   1    2    3    4    ")
            elif level==2:
                print("   1    2    3    4    5    6    7    8    9    10    ")
            elif level==3:
                print("   1    2    3    4    5    6    7    8    9    10   11   12   13   ")
        for j in range(0,len(listcard[0])):
            if j==0:
                if len(listcard[i][j].getName())==3:
                    str1=str(n)+str1+str(listcard[i][j].getName())+"  "
                elif len(listcard[i][j].getName())==2:
                    str1=str(n)+str1+str(listcard[i][j].getName())+"   "
            else:    
                if len(listcard[i][j].getName())==3:
                    str1=str1+str(listcard[i][j].getName())+"  "
                elif len(listcard[i][j].getName())==2:
                    str1=str1+str(listcard[i][j].getName())+"   "
        print(str1)
        print("\n")
        n=n+1


def giveAnswer(level,player,r,listcard):
    t = True
    while t:
        if r==1:
            display='Παίκτη '+str(player)+': Δώσε γραμμή και στήλη πρώτης κάρτας (πχ 1 10):'
        elif r==2:
            display='Παίκτη '+str(player)+': Δώσε γραμμή και στήλη δεύτερης κάρτας (πχ 1 10):'
        elif r==3:
            display='Παίκτη '+str(player)+': Δώσε γραμμή και στήλη τρίτης κάρτας (πχ 1 10):'
        answer=input(display)
        print("\n")
        an0=int(answer[0])-1
        if len(answer)==3:
            an2=int(answer[2])-1
        elif len(answer)==4:
            an2=int(answer[2]+answer[3])-1
        if level == 1:
            if (an0>=0 and an0<=3) and (an2>=0 and an2<=3):
                if listcard[an0][an2].getStatus() == 0:                    
                    t=False
                else:
                   print("Η κάρτα που επιλέξατε είναι ήδη ανοικτή, δοκιμάστε ξανά.")   
            else:
                print("Δώσατε λάθος δεδομένα, δοκιμάστε ξανά.")
        elif level == 2:
            if (an0>=0 and an0<=3) and (an2>=0 and an2<=9):
                if listcard[an0][an2].getStatus() == 0:                    
                    t=False
                else:
                    print("Η κάρτα που επιλέξατε είναι ήδη ανοικτή, δοκιμάστε ξανά.")
            else:
                print("Δώσατε λάθος δεδομένα, δοκιμάστε ξανά.")
        else:
            if (an0>=0 and an0<=3) and (an2>=0 and an2<=12):
                if listcard[an0][an2].getStatus() == 0:                    
                    t=False
                else:
                    print("Η κάρτα που επιλέξατε είναι ήδη ανοικτή, δοκιμάστε ξανά.")
            else:
                print("Δώσατε λάθος δεδομένα, δοκιμάστε ξανά.")
    return answer



def giveLevel():
    t = True
    while t:
        lev=input("Δώστε επίπεδο δυσκολίας Εύκολο (1), Μέτριο (2), Δύσκολο (3):")
        level=int(lev)

        if level==1 or level==2 or level==3:
            return level
            break
        else:
            print("Δώσατε λάθος δεδομένα, δοκιμάστε ξανά.")




def CardsOpen(listcard,level):
    openCard=True
    while openCard:
        if level==1:
            for i in range(0,4):
                for j in range(0,4):
                    if listcard[i][j].getStatus()==0:
                        openCard=False
                        break
        elif level==2:
            for i in range(0,4):
                for j in range(0,10):
                    if listcard[i][j].getStatus()==0:
                        openCard=False
                        break
        else:
            for i in range(0,4):
                for j in range(0,13):
                    if listcard[i][j].getStatus()==0:
                        openCard=False
                        break

    return openCard



def maxlist(result):
    max1=0
    p=0
    for i in range(0,len(result)):
        if max1<result[i]:
            max1=result[i]
            p=i
    return p














        
