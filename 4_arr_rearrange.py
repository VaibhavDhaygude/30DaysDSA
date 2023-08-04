def arrange(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j]<0):
                arr[i],arr[j]=arr[j],arr[i]
    return arr

def main():
    arr=[1,-2,-3,4,5,-9,7,-6]
    print(arrange(arr))
main()