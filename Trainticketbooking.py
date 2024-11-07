#Train ticket booking for the person in different age category
a=int(input("Enter the number of tickets :"))
price=0
for i in range(a):
    age=int(input("Enter the age of person "))
    if age > 80:
        price+=30
    elif age>12:
        price+=50
    else:
        price+=12

print("The Total price of all the tickets",price)
