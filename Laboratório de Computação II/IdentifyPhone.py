def identifyPhone(L) :
    if len(L) != 14 :
        #print("!= 14")
        return False
    
    for i in range(len(L)) :
        if (i == 0 and L[i] != "(") or (i == 3 and L[i] != ")") or (i == 9 and L[i] != "-") :
            #print(str(i) + " | " + L[i])
            return False
        elif i != 0 and i != 3 and i != 9 :
            try :
                int(L[i])
            except :
                #print(str(i) + " | " + L[i] + " is not a number")
                return False

    return True

def Q_1() :
    L = []
    t = input("Write a telephone number (ex. (DD)DDDDD-DDDD): ")
    for i in t :
        L.append(i)

    if identifyPhone(L) :
        print("Valid number")
    else :
        print("Invalid number")
