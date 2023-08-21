import math
def cal(stk,newstk):
    while(stk!=[]):
        
        if len(newstk)==math.ceil((len(stk))/2):
            stk.pop(0)
            continue
        else:
            newstk.append(stk[0])
            stk.pop(0)
        print(stk)
        print(newstk)

    return newstk
def main():
    stk=[1,2,3,4,5]
    newstk=[]
    print(cal(stk,newstk))
main()