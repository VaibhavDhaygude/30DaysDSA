def cal(arr,sum):
    for i in range(0,len(arr)):
        sum_t=arr[i]
        for j in range(i+1,len(arr)):
            sum_t=sum_t+arr[j]
            if(sum_t==sum):
                return i,j

        
            
            

def main():
    arr=[3,2,1,5,6]
    sum=6
    x,y=cal(arr,sum)
    print("for the sum: ",sum)
    print("subarray is:  ")
    for i in range(x,y+1):
        print(arr[i],end=" ")

main()