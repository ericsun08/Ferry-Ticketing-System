import datetime
today = datetime.date.today()

def seatschoicesP1():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP1[0:10])
                print("         ==============================")
                print("")
                if listP1[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP1()       
                else:                        
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP1[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP1[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP1[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesP1()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP1()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesP1()
                        else:
                                print("Invalid Key")
                                seatschoicesP1()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP1[10:20])
                print("\t",listP1[20:30])
                print("\t",listP1[30:40])
                print("\t",listP1[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP1[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP1[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP1[10:20])
                                        print("\t",listP1[20:30])
                                        print("\t",listP1[30:40])
                                        print("\t",listP1[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesP1()
                                else:
                                        print("Invalid Key")
                                        seatschoicesP1()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesP1()
                else:
                        print("Invalid Key")
                        seatschoicesP1()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP1()
            
listP1 = []
listP1 = list(range(0,50))
for no in range(0,50):
        listP1[no]=0


def FerryId1():
    print("Ferry ID:001\n1. 10.00 AM (Penang - Langkawi)\n2. 11.00 AM (Langkawi - Penang)")
    choose = int(input("Please select destination: "))
    if choose == 1:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listP1[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listP1[10:20])
        print("\t",listP1[20:30])
        print("\t",listP1[30:40])
        print("\t",listP1[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId1()
    elif choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listL2[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listL2[10:20])
        print("\t",listL2[20:30])
        print("\t",listL2[30:40])
        print("\t",listL2[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId1()
    
        
def seatschoicesP2():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP2[0:10])
                print("         ==============================")
                print("")
                if listP2[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP2()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP2[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP2[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP2[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                print("")
                                                seatschoicesP2()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP2()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        print("")
                                        seatschoicesP2()
                        else:
                                print("Invalid Key")
                                seatschoicesP2()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP2[10:20])
                print("\t",listP2[20:30])
                print("\t",listP2[30:40])
                print("\t",listP2[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP2[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP2[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP2[10:20])
                                        print("\t",listP2[20:30])
                                        print("\t",listP2[30:40])
                                        print("\t",listP2[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesP2()
                                else:
                                        print("Invalid Key")
                                        seatschoicesP2()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesP2()
                else:
                        print("Invalid Key")
                        seatschoicesP2()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP2()
            
listP2 = []
listP2 = list(range(0,50))
for no in range(0,50):
        listP2[no]=0

def FerryId2():
    print("Ferry ID:002\n1. 10.00 AM (Langkawi - Penang)\n2. 11.00 Am (Penang - Langkawi)")
    choose = int(input("Please select destination: "))
    if choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listP2[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listP2[10:20])
        print("\t",listP2[20:30])
        print("\t",listP2[30:40])
        print("\t",listP2[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId2()
    elif choose == 1:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listL1[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listL1[10:20])
        print("\t",listL1[20:30])
        print("\t",listL1[30:40])
        print("\t",listL1[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId2()
        
def seatschoicesP3():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP3[0:10])
                print("         ==============================")
                print("")
                if listP3[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP3()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP3[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP3[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP3[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesP3()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP3()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesP3()
                        else:
                                print("Invalid Key")
                                seatschoicesP3()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP3[10:20])
                print("\t",listP3[20:30])
                print("\t",listP3[30:40])
                print("\t",listP3[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP3[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP3[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP3[10:20])
                                        print("\t",listP3[20:30])
                                        print("\t",listP3[30:40])
                                        print("\t",listP3[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        return listP3
                                else:
                                        print("Invalid Key")
                        else:
                                print("Seat is booked, please choose another seat")
                                return listP3
                else:
                        print("Invalid Key")
                        seatschoicesP3()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP3()
            
listP3 = []
listP3 = list(range(0,50))
for no in range(0,50):
        listP3[no]=0

def FerryId3():
    print("Ferry ID:003\n1. 12.00 PM(Penang - Langkawi)\n2. 13.00 PM (Langkawi - Penang)")
    choose = int(input("Please select destination: "))
    if choose == 1:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listP3[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listP3[10:20])
        print("\t",listP3[20:30])
        print("\t",listP3[30:40])
        print("\t",listP3[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId3()
    elif choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ===============================")
        print("         Business Class (1-10)")
        print("\t",listL4[0:10])
        print("         ===============================")
        print("         Economy Class (11-50)")
        print("\t",listL4[10:20])
        print("\t",listL4[20:30])
        print("\t",listL4[30:40])
        print("\t",listL4[40:50])
        print("         ===============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId4()
        
def seatschoicesP4():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP4[0:10])
                print("         ==============================")
                print("")
                if listP4[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP4()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP4[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP4[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP4[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesP4()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP4()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesP4()
                        else:
                                print("Invalid Key")
                                seatschoicesP4()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP4[10:20])
                print("\t",listP4[20:30])
                print("\t",listP4[30:40])
                print("\t",listP4[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP4[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP4[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP4[10:20])
                                        print("\t",listP4[20:30])
                                        print("\t",listP4[30:40])
                                        print("\t",listP4[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesP4()
                                else:
                                        print("Invalid Key")
                                        seatschoicesP4()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesP4()
                else:
                        print("Invalid Key")
                        seatschoicesP4()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP4()
            
listP4 = []
listP4 = list(range(0,50))
for no in range(0,50):
        listP4[no]=0

def FerryId4():
    print("Ferry ID:004\n1. 12.00 PM(Langkawi - Penang)\n2. 13.00 PM (Penang - Langkawi)")
    choose = int(input("Please select destination: "))
    if choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listP4[0,10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listP4[10:20])
        print("\t",listP4[20:30])
        print("\t",listP4[30:40])
        print("\t",listP4[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId4()
    elif choose == 1:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listL3[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listL3[10:20])
        print("\t",listL3[20:30])
        print("\t",listL3[30:40])
        print("\t",listL3[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId4()
        
def seatschoicesP5():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP5[0:10])
                print("         ==============================")
                print("")
                if listP5[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP5()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP5[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP5[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP5[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesP5()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP5()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesP5()
                        else:
                                print("Invalid Key")
                                seatschoicesP5()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP5[10:20])
                print("\t",listP5[20:30])
                print("\t",listP5[30:40])
                print("\t",listP5[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP5[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP5[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP5[10:20])
                                        print("\t",listP5[20:30])
                                        print("\t",listP5[30:40])
                                        print("\t",listP5[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesP5()
                                else:
                                        print("Invalid Key")
                                        seatschoicesP5()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesP5()
                else:
                        print("Invalid Key")
                        seatschoicesP5()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP5()
            
listP5 = []
listP5 = list(range(0,50))
for no in range(0,50):
        listP5[no]=0

def FerryId5():
    print("Ferry ID:005\n1. 14.00 PM(Penang - Langkawi)\n2. 15.00 PM (Langkawi - Penang)")
    choose = int(input("Please select destination: "))
    if choose == 1:
        print("")
        print("          Note: 1 -> Seat is booked")
        print("                0 -> Seat is empty")
        print("         ===============================")
        print("         Business Class (1-10)")
        print("\t",listP5[0:
                          10])
        print("         ===============================")
        print("         Economy Class (11-50)")
        print("\t",listP5[10:20])
        print("\t",listP5[20:30])
        print("\t",listP5[30:40])
        print("\t",listP5[40:50])
        print("         ===============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId5()
    elif choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listL6[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listL6[10:20])
        print("\t",listL6[20:30])
        print("\t",listL6[30:40])
        print("\t",listL6[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId5()
                    
def seatschoicesP6():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP6[0:10])
                print("         ==============================")
                print("")
                if listP6[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP6()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP6[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP6[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP6[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesP6()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP6()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesP6()
                        else:
                                print("Invalid Key")
                                seatschoicesP6()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP6[10:20])
                print("\t",listP6[20:30])
                print("\t",listP6[30:40])
                print("\t",listP6[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP6[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP6[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP6[10:20])
                                        print("\t",listP6[20:30])
                                        print("\t",listP6[30:40])
                                        print("\t",listP6[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesP6()
                                else:
                                        print("Invalid Key")
                                        seatschoicesP6()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesP6()
                else:
                        print("Invalid Key")
                        seatschoicesP6()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP6()
listP6 = []
listP6 = list(range(0,50))
for no in range(0,50):
        listP6[no]=0

def FerryId6():
    print("Ferry ID:006\n1. 14.00 PM(Langkawi - Penang)\n2. 15.00 PM (Penang - Langkawi)")
    choose = int(input("Please select destination: "))
    if choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listP6[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listP6[10:20])
        print("\t",listP6[20:30])
        print("\t",listP6[30:40])
        print("\t",listP6[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
             print ("Invalid key")
             FerryId6()
    elif choose == 1:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listLB5[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listL5[10:20])
        print("\t",listL5[20:30])
        print("\t",listL5[30:40])
        print("\t",listL5[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId6()
                
def seatschoicesP7():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP7[0:10])
                print("         ==============================")
                print("")
                if listP7[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP7()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP7[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP7[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP7[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesP7()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP7()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesP7()
                        else:
                                print("Invalid Key")
                                seatschoicesP7()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP7[10:20])
                print("\t",listP7[20:30])
                print("\t",listP7[30:40])
                print("\t",listP7[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP7[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP7[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP7[10:20])
                                        print("\t",listP7[20:30])
                                        print("\t",listP7[30:40])
                                        print("\t",listP7[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesP7()
                                else:
                                        print("Invalid Key")
                                        seatschoicesP7()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesP7()
                else:
                        print("Invalid Key")
                        seatschoicesP7()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP7()
            
listP7 = []
listP7 = list(range(0,50))
for no in range(0,50):
        listP7[no]=0

def FerryId7():
    print("Ferry ID:007\n1. 16.00 PM(Penang - Langkawi)\n2. 17.00 PM (Langkawi - Penang)")
    choose = int(input("Please select destination: "))
    if choose == 1:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listP7[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listP7[10:20])
        print("\t",listP7[20:30])
        print("\t",listP7[30:40])
        print("\t",listP7[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId7()
    elif choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listL8[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listL8[10:20])
        print("\t",listL8[20:30])
        print("\t",listL8[30:40])
        print("\t",listL8[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId7()
             
        
def seatschoicesP8():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listP8[0:10])
                print("         ==============================")
                print("")
                if listP8[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesP8()
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listP8[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listP8[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listP8[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesP8()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesP8()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesP8()
                        else:
                                print("Invalid Key")
                                seatschoicesP8()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listP8[10:20])
                print("\t",listP8[20:30])
                print("\t",listP8[30:40])
                print("\t",listP8[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listP8[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listP8[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listP8[10:20])
                                        print("\t",listP8[20:30])
                                        print("\t",listP8[30:40])
                                        print("\t",listP8[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesP8()
                                else:
                                        print("Invalid Key")
                                        seatschoicesP8()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesP8()
                else:
                        print("Invalid Key")
                        seatschoicesP8()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesP8()

listP8 = []
listP8 = list(range(0,50))
for no in range(0,50):
        listP8[no]=0

def FerryId8():
    print("Ferry ID:008\n1. 16.00 PM(Langkawi - Penang)\n2. 17.00 PM (Penang - Langkawi)")
    choose = int(input("Please select destination: "))
    if choose == 2:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listPB8[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listP8[10:20])
        print("\t",listP8[20:30])
        print("\t",listP8[30:40])
        print("\t",listP8[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId8()
    elif choose  == 1:
        print("")
        print("         Note: 1 -> Seat is booked")
        print("               0 -> Seat is empty")
        print("         ==============================")
        print("         Business Class (1-10)")
        print("\t",listL7[0:10])
        print("         ==============================")
        print("         Economy Class (11-50)")
        print("\t",listL7[10:20])
        print("\t",listL7[20:30])
        print("\t",listL7[30:40])
        print("\t",listL7[40:50])
        print("         ==============================")
        print("         B - View another Ferry ID")
        print("         M - Main Menu")
        print("")
        proceed2 = str(input("Please select: "))
        if(proceed2=="B") or (proceed2=="b"):
             subMenuforV()
        elif(proceed2=="M") or (proceed2=="m"):
             mainMenu()
        else :
                print ("Invalid key")
                FerryId8()
            
def seatschoicesL1():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL1[0:10])
                print("         ==============================")
                print("")
                if listL1[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL1()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL1[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL1[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL1[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL1()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL1()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL1()
                        else:
                                print("Invalid Key")
                                seatschoicesL1()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL1[10:20])
                print("\t",listL1[20:30])
                print("\t",listL1[30:40])
                print("\t",listL1[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL1[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL1[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL1[10:20])
                                        print("\t",listL1[20:30])
                                        print("\t",listL1[30:40])
                                        print("\t",listL1[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesL1()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL1()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL1()
                else:
                        print("Invalid Key")
                        seatschoicesL1()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL1()
            
listL1 = []
listL1 = list(range(0,50))
for no in range(0,50):
        listL1[no]=0

def seatschoicesL2():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL2[0:10])
                print("         ==============================")
                print("")
                if listL2[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL2()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL2[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL2[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL2[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL2()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL2()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL2()
                        else:
                                print("Invalid Key")
                                seatschoicesL2()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL2[10:20])
                print("\t",listL2[20:30])
                print("\t",listL2[30:40])
                print("\t",listL2[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL2[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL2[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL2[10:20])
                                        print("\t",listL2[20:30])
                                        print("\t",listL2[30:40])
                                        print("\t",listL2[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesL2()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL2()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL2()
                else:
                        print("Invalid Key")
                        seatschoicesL2()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL2()
            
listL2 = []
listL2 = list(range(0,50))
for no in range(0,50):
        listL2[no]=0

def seatschoicesL3():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL3[0:10])
                print("         ==============================")
                print("")
                if listL3[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL3()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL3[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL3[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL3[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL3()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL3()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL3()
                        else:
                                print("Invalid Key")
                                seatschoicesL3()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL3[10:20])
                print("\t",listL3[20:30])
                print("\t",listL3[30:40])
                print("\t",listL3[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL3[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL3[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL3[10:20])
                                        print("\t",listL3[20:30])
                                        print("\t",listL3[30:40])
                                        print("\t",listL3[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesL3()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL3()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL3()
                else:
                        print("Invalid Key")
                        seatschoicesL3()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL3()
            
listL3 = []
listL3 = list(range(0,50))
for no in range(0,50):
        listL3[no]=0

def seatschoicesL4():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("Note: 1 -> Seat is booked")
                print("      0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL4[0:10])
                print("         ==============================")
                print("")
                if listL4[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL4()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL4[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL4[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL4[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL4()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL4()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL4()
                        else:
                                print("Invalid Key")
                                seatschoicesL4()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL4[10:20])
                print("\t",listL4[20:30])
                print("\t",listL4[30:40])
                print("\t",listL4[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL4[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL4[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL4[10:20])
                                        print("\t",listL4[20:30])
                                        print("\t",listL4[30:40])
                                        print("\t",listL4[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesL4()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL4()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL4()                
                else:
                        print("Invalid Key")
                        seatschoicesL4()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL4()
            
listL4 = []
listL4 = list(range(0,50))
for no in range(0,50):
        listL4[no]=0

def seatschoicesL5():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL5[0:10])
                print("         ==============================")
                print("")
                if listL5[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL5()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL5[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL5[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL5[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL5()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL5()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL5()
                        else:
                                print("Invalid Key")
                                seatschoicesL5()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL5[10:20])
                print("\t",listL5[20:30])
                print("\t",listL5[30:40])
                print("\t",listL5[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL5[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL5[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL5[10:20])
                                        print("\t",listL5[20:30])
                                        print("\t",listL5[30:40])
                                        print("\t",listL5[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesL5()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL5()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL5()
                else:
                        print("Invalid Key")
                        seatschoicesL5()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL5()
            
listL5 = []
listL5 = list(range(0,50))
for no in range(0,50):
        listL5[no]=0

def seatschoicesL6():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL6[0:10])
                print("         ==============================")
                print("")
                if listL6[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL6()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL6[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL6[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL6[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL6()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL6()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL6()
                        else:
                                print("Invalid Key")
                                seatschoicesL6()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL6[10:20])
                print("\t",listL6[20:30])
                print("\t",listL6[30:40])
                print("\t",listL6[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL6[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL6[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL6[10:20])
                                        print("\t",listL6[20:30])
                                        print("\t",listL6[30:40])
                                        print("\t",listL6[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                         seatschoicesL6()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL6()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL6()
                else:
                        print("Invalid Key")
                        seatschoicesL6()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL6()
            
listL6 = []
listL6 = list(range(0,50))
for no in range(0,50):
        listL6[no]=0

def seatschoicesL7():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL7[0:10])
                print("         ==============================")
                print("")
                if listL7[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL7()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL7[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL7[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL7[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL7()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL7()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL7()
                        else:
                                print("Invalid Key")
                                seatschoicesL7()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL7[10:20])
                print("\t",listL7[20:30])
                print("\t",listL7[30:40])
                print("\t",listL7[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL7[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL7[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL7[10:20])
                                        print("\t",listL7[20:30])
                                        print("\t",listL7[30:40])
                                        print("\t",listL7[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesL7()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL7()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL7()
                else:
                        print("Invalid Key")
                        seatschoicesL7()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL7()
            
listL7 = []
listL7 = list(range(0,50))
for no in range(0,50):
        listL7[no]=0

def seatschoicesL8():
        print("")
        print("      ========================================= ")
        print("     |B - to purchase ticket for Business class|")
        print("     |E - to purchase ticket for Economy class |")
        print("     |M - to return to Main Menu               |")
        print("      ========================================= ")
        print("")
        selection2 = str(input("Please Select the class: "))
        global typeclass
        if (selection2 == "B") or (selection2 == "b"):
                typeclass = "Business Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Business Class (1-10)")
                print("\t",listL8[0:10])
                print("         ==============================")
                print("")
                if listL8[0:10]== [1,1,1,1,1,1,1,1,1,1]:
                        print("Business class is full\nPlease choose another seat in Economy class")
                        seatschoicesL8()
                else:
                        global i
                        i = int(input("Select Seat: "))
                        if (i >= 1) and (i <=10):
                                if listL8[i-1] == 0:
                                        print("")
                                        print("Seat",i, "is empty, would you like to book this seat? ")
                                        print("Y - YES\nN - NO")
                                        print("")
                                        select = str(input("Please select: "))
                                        if (select == "Y") or (select == "y"):
                                                listL8[i-1]=1
                                                print("")
                                                print("         ==============================")
                                                print("         Business class (1-10)")
                                                print("\t",listL8[0:10])
                                                print("         ==============================")
                                                print("")
                                                customerdata()
                                        elif (select == "N") or (select == "n"):
                                                seatschoicesL8()
                                        else:
                                                print("Invalid Key")
                                                seatschoicesL8()
                                else:
                                        print("Seat is booked, please choose another seat")
                                        seatschoicesL8()
                        else:
                                print("Invalid Key")
                                seatschoicesL8()
        elif (selection2 == "E") or (selection2 == "e"):
                typeclass = "Economy Class"
                print("")
                print("         Note: 1 -> Seat is booked")
                print("               0 -> Seat is empty")
                print("         ==============================")
                print("         Economy class (11-50)")
                print("\t",listL8[10:20])
                print("\t",listL8[20:30])
                print("\t",listL8[30:40])
                print("\t",listL8[40:50])
                print("         ==============================")
                print("")
                i = int(input("Select Seat: "))
                if (i >= 11) and (i <=50):
                        if listL8[i-1] == 0:
                                print("")
                                print("Seat",i,"is empty, would you like to book this seat?")
                                print("Y - YES\nN - NO")
                                print("")
                                select = str(input("Please select: "))
                                if (select == "Y") or (select == "y"):
                                        listL8[i-1]=1
                                        print("")
                                        print("         ==============================")
                                        print("         Economy class (11-50)")
                                        print("\t",listL8[10:20])
                                        print("\t",listL8[20:30])
                                        print("\t",listL8[30:40])
                                        print("\t",listL8[40:50])
                                        print("         ==============================")
                                        print("")
                                        customerdata()
                                elif (select == "N") or (select == "n"):
                                        seatschoicesL8()
                                else:
                                        print("Invalid Key")
                                        seatschoicesL8()
                        else:
                                print("Seat is booked, please choose another seat")
                                seatschoicesL8()
                else:
                        print("Invalid Key")
                        seatschoicesL8()
        elif (selection2 == "M") or (selection2 == "m"):
            mainMenu()
        else:
            print("Invalid Key")
            seatschoicesL8()
            
listL8 = []
listL8 = list(range(0,50))
for no in range(0,50):
        listL8[no]=0
         
def departuretimeforP():
        print("")
        print("Penang - Langkawi\n===================\n1.10.00 AM\n2.11.00 AM\n3.12.00 PM\n4.13.00 PM\n5.14.00 PM\n6.15.00 PM\n7.16.00 PM\n8.17.00 PM\n===================")
        print("9.Return to routes")
        print("")
        timeselection = int(input("Please select departure time (1-8): "))
        global timeselection1
        global FerryID
        if(timeselection == 1):
                timeselection1 = "10.00 AM"
                FerryID = "001"
                seatschoicesP1()
        elif(timeselection == 2):
                timeselection1 = "11.00 AM"
                FerryID = "002"
                seatschoicesP2()
        elif(timeselection == 3):
                timeselection1 = "12.00 PM"
                FerryID = "003"
                seatschoicesP3()
        elif(timeselection == 4):
                timeselection1 = "13.00 PM"
                FerryID = "004"
                seatschoicesP4()
        elif(timeselection == 5):
                timeselection1 = "14.00 PM"
                FerryID = "005"
                seatschoicesP5()
        elif(timeselection == 6):
                timeselection1 = "15.00 PM"
                FerryID = "006"
                seatschoicesP6()
        elif(timeselection == 7):
                timeselection1 = "16.00 PM"
                FerryID = "007"
                seatschoicesP7()
        elif(timeselection == 8):
                timeselection1 = "17.00 PM"
                FerryID = "008"
                seatschoicesP8()
        elif(timeselection == 9):
                subMenuforP()
        else:
                print("Invalid Key")
                departuretimeforP()
def departuretimeforL():
        print("")
        print("Langkawi - Penang\n=====================\n1.10.00 AM\n2.11.00 AM\n3.12.00 PM\n4.13.00 PM\n5.14.00 PM\n6.15.00 PM\n7.16.00 PM\n8.17.00 PM\n=====================")
        print("9.Return to routes")
        print("")
        global timeselection
        timeselection = int(input("Please select departure time (1-8): "))
        global timeselection1
        global FerryID
        if(timeselection == 1):
                timeselection1 = "10.00 AM"
                FerryID = "002"
                seatschoicesL1()
        elif(timeselection == 2):
                timeselection1 = "11.00 AM"
                FerryID = "001"
                seatschoicesL2()
        elif(timeselection == 3):
                timeselection1 = "12.00 PM"
                FerryID = "004"
                seatschoicesL3()
        elif(timeselection == 4):
                timeselection1 = "13.00 PM"
                FerryID = "003"
                seatschoicesL4()
        elif(timeselection == 5):
                timeselection1 = "14.00 PM"
                FerryID = "006"
                seatschoicesL5()
        elif(timeselection == 6):
                timeselection1 = "15.00 PM"
                FerryID = "005"
                seatschoicesL6()
        elif(timeselection == 7):
                timeselection1 = "16.00 PM"
                FerryID = "008"
                seatschoicesL7()
        elif(timeselection == 8):
                timeselection1 = "17.00 PM"
                FerryID = "007"
                seatschoicesL8()
        elif(timeselection == 9):
                subMenuforP()
        else:
                print("Invalid Key")
                departuretimeforL
                
def subMenuforP():
    print("")
    print("         =========================")
    print("         Routes")
    print("         =========================")
    print("         P - Penang to Langkawi   ")
    print("         L - Langkawi to Penang   ")
    print("         M - Main Menu            ")
    print("         =========================")
    print("")
    route1 = str(input("Choose your trip route : "))
    global route2
    global route3
    if(route1 == "P") or (route1 == "p"):
        route2 = "Penang"
        route3 = "Langkawi"
        departuretimeforP()
    elif(route1 == "L") or (route1 == "l"):
        route3 = "Penang"
        route2 = "Langkawi"
        departuretimeforL()
    elif(route1 == "M") or (route1 == "m"):
        mainMenu()
    else:
        print("Invalid Key.")
        subMenuforP()

def customerdata():
    print("")
    print("Please fill up the guest details.")
    print("=================================")
    global name1
    global name2
    global gender
    name1 = str(input("First name   : "))
    name2 = str(input("Family name  : "))
    gender = str(input("Gender (Male or Female): "))
    print("")
    print("")
    payment()
def payment():
    print("")
    print ("****************************************")
    print ("\tPAYMENT SECTION")
    print ("Total price included Add-ons baggage,Food Package and Life Insurance")
    print ("Ticket Price    : MYR50 ")
    print ("PAYMENT")
    print (" A - Paid by Cash")
    print (" B - Paid in Debit/Credit Card")
    print("***************************************")
    print("")
    paidby = str(input("Please select : "))
    if (paidby=="A") or (paidby=="a")or(paidby=="B") or (paidby=="b"):
            boardingpass()        
    else:
            print ("Invalid Key")
            payment()
def boardingpass():
    print("")
    print("")
    print("===========================================")
    print("\tBOARDING PASS")
    print("Name                :",name1,name2)
    print("Gender              :",gender)
    print("Departure Date      :",today)
    print("Ferry ID            :",FerryID)
    print("From                :",route2)
    print("To                  :",route3)
    print("Departure time      :",timeselection1)
    print("Type of seat        :",typeclass)
    print("Seat no             :",i)
    print("===========================================")
    mainMenu()        
            
def subMenuforV():
    print("")
    print("             ========================= ")
    print("            |F - to select Ferry ID   |")
    print("            |T - to select Trip Time  |")
    print("            |M - return to Main Menu  |")
    print("             ========================= ")
    print("")
    selection3 = str(input("Please select: "))
    if (selection3 == "F") or (selection3 == "f"):
              print("")
              print("     *****************     ")
              print("     ***    001    ***     ")
              print("     ***    002    ***     ")
              print("     ***    003    ***     ")
              print("     ***    004    ***     ")
              print("     ***    005    ***     ")
              print("     ***    006    ***     ")
              print("     ***    007    ***     ")
              print("     ***    008    ***     ")
              print("     *****************     ")
              print("     9 - Back"         )
              print("")
              ferryID = int(input("Select Ferry ID (1-8): "))
              if (ferryID == 1):
                  FerryId1()
              elif (ferryID == 2):
                  FerryId2()      
              elif (ferryID == 3):
                  FerryId3()  
              elif (ferryID == 4):
                  FerryId4()        
              elif (ferryID == 5):
                  FerryId5()  
              elif (ferryID == 6):
                  FerryId6() 
              elif (ferryID == 7):
                  FerryId7()  
              elif (ferryID == 8):
                  FerryId8()
              elif (ferryID == 9):
                    subMenuforV()
              else:
                  print("Invalid Key")
                  subMenuforV()             
    elif (selection3 == "T") or (selection3 == "t"):
        print("Penang - Langkawi\n10.00 AM\n11.00 AM\n12.00 PM\n13.00 PM\n14.00 PM\n16.00 PM\n17.00 PM\n\n"
               "Langkawi - Penang\n10.00 AM\n11.00 AM\n12.00 PM\n13.00 PM\n14.00 PM\n16.00 PM\n17.00 PM")
        print("\nThe trip may take one hour time")
        print("Proceed into Purchasing Ticket Menu")
        print("Y - YES")
        print("N - NO")
        proceed2 = str(input("Please select: "))
        if(proceed2 == "Y") or (proceed2 == "y"):
            subMenuforP()
        elif(proceed2 == "N") or (proceed2 == "n"):
            mainMenu()
        else :
            print ("Invalid key")
            subMenuforV()
    elif (selection3 == "M") or (selection3 == "m"):
            mainMenu()
    else:
            print("Invalid Key")
            subMenuforV()
def mainMenu():
    print("")
    print("     Date:",today)
    print("")
    print("     ***** WElCOME TO FERRY TICKETING SYSTEM *****")
    print("           =================================      ")
    print("          |P - to Purchase Ticket          |      ")
    print("          |V - to View Seating Arrangement |      ")
    print("          |Q - to Quit the system          |      ")
    print("           =================================      ")
    print("")
    selection1 = str(input("Please Select: "))  
    if (selection1 == "P") or (selection1 == "p"):
        subMenuforP()
    elif (selection1 == "V") or (selection1 == "v"):
        subMenuforV()
    elif (selection1 == "Q") or (selection1 == "q"):
        exit
    else:
        print("Invalid Key")
        mainMenu()

mainMenu()


          








