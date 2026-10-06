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

""" f=int(input("What is your number?"))
result = f/1
a = f//2
b = f//3
c = f//4              #factors
d = f//5
e = f//6
g = f//7
h = f//8
i = f//9
print(result,a,b,c,d,e,g,h,i) """

""" x = (float, input("What is your first factor?").split()) 
y = (float, input("What is the second factor?").split())
 """
def gcf(x,y):
    var1 = x % i
    var2 = y % 2
    for i in range(x+y):
        

        if var1 == 0 and var2 == 0 and var1 == var2:
            print(i)
gcf(2,2)

   






""" def wizard(N, start, duels):
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
   
        
wizard(3, "A", ["BA", "CB", "DA"]) """