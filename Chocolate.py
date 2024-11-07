#A chocolate factory is packing chocolates into the packets. Then the chocolate packets have the array of N numbers of integer values. The take is to find the empty packets of chocolate and push it to the end of the conveyor belt. Also sort the array and remove the duplicate values.
n=int(input("Enter the number of packets"))
arr=list(map(int,input("Enter the number of chocolates in the packets").split()))
arr1=[]
arr2=[]
for i in arr:
    if(i==0):
        arr2.append(0)
    else:
        arr1.append(i)
new_arr=sorted(arr1)
final_arr=[]
for j in range(len(new_arr)):
    if not final_arr or new_arr[j] != final_arr[-1]:
        final_arr.append(new_arr[j])


        
final_arr=final_arr+arr2
print(final_arr)
    
