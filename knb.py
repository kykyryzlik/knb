import random

def one(mm):
    #mm = 10
    x = random.randint(0,mm)
    y = random.randint(0,mm)
    
    if x == y:
        w = "nothing"
        print(x, "or ", y, "Winer IS: ", w)        
    elif x != 0 and y !=0:
        w = max(x,y)
        print(x, "or ", y, "winer is: ", w)
    elif (x == 0 or y == 0) and (x != mm or y != mm) :
        w = max(x,y)
        print(x, "or ", y, "winer is: ", w)
    elif (x == 0 or y == 0) and (x == mm or y == mm) :
        w = min(x,y)
        print(x, "or ", y, "winer is: ", w)
       
    if w == x :
        w = "A"
    elif w == y:
        w = "B"
    elif w == "nothing":
        w = "nothing"
        
    return(w)

Awin = 0
Bwin = 0
Nwin = 0

k = 10
d = 10
for i in range(0,d):
    Z = one(k)
    i = i+1   
    if Z == "A":
        Awin = Awin+1
    elif Z == "B":
        Bwin = Bwin+1
    elif Z == "nothing":
        Nwin = Nwin+1
        
print("Winer A is: ", Awin, "times")
print("Winer B is: ", Bwin, "times")
print("Winer NOTHING is: ", Nwin, "times")
    
    
    
    
    
    
    
    