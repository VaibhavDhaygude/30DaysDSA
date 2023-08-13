def cal(str):
    dic={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    result=0
    for i in str:
        num=dic[i]
        if(result<num):
            result=num-result
        else:
            result=result+num
    return result

def main():
    str='LXXX'
    print(cal(str))
main()

