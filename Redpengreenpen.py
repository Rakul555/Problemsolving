#You are a teacher creating an engaging math activity for your students by writing N numbers on the classroom white board. You use a green pen for odd numbers and red pen for even numbers. Your task is to find to return the number of pen switches while writing numbers.
arr=list(map(int,input().split()))
count=0
for i in range(len(arr)-1):
    if(arr[i+1]%2==0):
        count+=1
print(count)
