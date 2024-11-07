#Consider two Integers m and n. Calculate the sum of the cubes of the integer values m to n
m=int(input("Enter the value of m :"))
n=int(input("Enter the value of n :"))
sum=0
if m>n :
    print(0)
else:
    for i in range(m,n):
        sum+=(i**3)
print(sum)
