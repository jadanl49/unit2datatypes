""" f=int(input("What is your number"))
result = f%2
if result == 1:
    print("odd")
else:
    print("even")
 """
""" def bilcalc(b):
    b=str(input("how much was the bill"))
    if b == "bad":
        print("0%")
    elif b == "okay":
        print("15%")
    elif b =="good":             #bill
        print("20%")
    elif b == "great":
        print("25%")
bilcalc(b=True) """



def factors(x):
    for i in range(x+1):
        while x % i > 0:
            if x % i == 0:
                break
            z = i
                
        print(z)
factors(9)




""" 
def gcf(x,y):

    for i in range(1,x+y):
        var1 = x % i
        var2 = y % i
        if var1 == 0 and var2 == 0 and var1 == var2:
            z=i
    print(z)        
gcf(100,20)

    """






""" def wizard(N start, duels):
    owner = start
    num_owners= 1
   #checks if switches hand
    for i in range(N):
     if duels[i][1] == owner:
        owner = duels[i][0]
        num_owners += 1
    print(owner)
    print(num_owners)
    #check if wand switches hands
   
        
wizard(3, "A", ["BA", "CB", "DA"])  """