def cal(arr,target):
    cnt=0
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]+arr[j]==target):
                cnt=cnt+1
    return cnt

def main():
    arr=[1,2,3,4,5]
    print(cal(arr,6))
main()