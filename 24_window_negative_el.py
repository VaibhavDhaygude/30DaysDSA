def cal(arr,k):
    ans=[]
    for i in range(0,len(arr)-(k-1)):
        # print()
        for j in range(i,i+k):
            # print(arr[j])
            if arr[j]<0:
                ans.append(arr[j])
                break
            if j ==i+k-1 and arr[j]>0:
                ans.append(0)
    return ans

def main():
    arr=[-8,2,3,-6,10]
    k=2
    print(cal(arr,k))
main()