#Restaurent menu card
print("1) PIZZA -200rs")
print("2) BURGER -180rs")
print("3) BRIYANI -250rs")
print("4) DOSA -80rs")
print("5) IDLY -50rs")
n=int(input("Enter the items you want to order"))
price=0
for i in range(1,n+1):
    a=int(input("Enter the Dish no"))
    n=int(input("Enter the Quantity of the dish"))
    if(a==1):
        price+=(n*200)
    elif(a==2):
        price+=n*180
    elif(a==3):
        price+=n*250
    elif(a==4):
        price+=n*80
    elif(a==5):
        price+=n*50
    else:
        print("Enter the correct numbers for dishes")
    
if(price>500):
    a=int(input("Congratulations you have 10% offer would you like to grab it If yes type 1 or Type 0"))
    if(a==1):
        price_new=price-(price/10)
        print("Total bill amount is",price_new)
    else:
        print("Total bill amount is",price)
else:
    print("Total bill amount is",price)

    
