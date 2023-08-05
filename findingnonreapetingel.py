#TC O(n)
def cal(arr):
    maxel=max(arr)
    temp=[0 for i in range(maxel)]
    for i in range(0,len(arr)):
        temp[arr[i]%len(arr)]+=1
    for i in arr:
        if(temp[i%len(arr)]==1):
            return i
        
def main():
    arr=[2,4,7,5,2,7,5]
    print(cal(arr))
main()