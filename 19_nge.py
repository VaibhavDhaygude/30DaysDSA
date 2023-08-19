def cal(arr):
    ans=[-1  for i in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]>arr[i]:
                ans[i]=arr[j]
                break
        
    print(ans)

def main():
    arr=[100,90,110,95]
    cal(arr)
main()