# x = 3
# y = float(3)
# print(x,y)
 
# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i)

# print(values[0])
# print(values[6])

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """


""" bill = input("how much was the bill?")
print(int(bill) * 20) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}")
 """
""" odd = [1,3,5,7,9]

even = [2,4,6,8,10]

number = input("Enter your number")
if number == odd:
    print('odd')
if number == even:
    print('even')

else: print('too large')


print(odd)

print(odd[1])

for odd in odd:
    if odd =="1":
        print(f'we found {odd}') 
 """


""" 
x = input("input a sentence")
y= x.split( )
z = y[0]
print(y)
print(z)
 """
def bilcalc(b):
    b=str(input("how much was the bill"))
    if b == "bad":
        print("0%")
    elif b == "okay":
        print("15%")
    elif b =="good":
        print("20%")
    elif b == "great":
        print("25%")
bilcalc(b=True)