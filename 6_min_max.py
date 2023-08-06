def cal(arr):
    min=1000
    max=-1

    for i in arr:
        if(max<i):
            max=i
        if(min>i):
            min=i
    return max,min
def main():
    arr=[5,2,9,1,7]
    max,min=cal(arr)
    print("max: ",max," min: ",min)
    
main()