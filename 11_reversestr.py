def cal(str):
    arr=str.split(" ")
    # print(arr)
    result=""
    for i in range(len(arr)-1,-1,-1):
        result=result+" "+arr[i]
    return result



def main():
    str="i love programming"
    print(cal(str))
main()
