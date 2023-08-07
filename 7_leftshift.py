def leftshift(arr,n):
    ans=[0 for i in range(0,len(arr))]
    for i in range(0,len(arr)):
        j=len(arr)-abs(i-n)
        if i>=n:
            ans[i-n]=arr[i]
        elif(i<n):
            ans[len(arr)-(n-i)]=arr[i]
    return ans

def main():
    arr=[10,20,30,40,50]
    n=3
    print(leftshift(arr,n))

main()


