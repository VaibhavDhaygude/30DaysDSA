def occurences(arr,x):
    count=0
    arr.sort()
    for i in range(len(arr)):
        if arr[i]==x:
            count=count+1
        if(arr[i]>x or i==len(arr)-1):
            return count
        
def main():
    arr=[6,3,4,2,1,8,8,8,2,3,8,8]
    print(occurences(arr,8))
            
main()
        



