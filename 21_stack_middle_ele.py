import math
def cal(stk,newstk):
    n=len(stk)
    while(stk!=[]):
        
        if len(newstk)+1==len(stk) or (len(newstk)==len(stk) and n%2==0) :
            stk.pop(0)
            continue
        else:
            newstk.append(stk[0])
            stk.pop(0)
        print(stk)
        print(newstk)

    return newstk
def main():
    stk1=[1,2,3,4,5]
    stk2=[5,10,15,20]
    stk3=[100]
    newstk=[]
    print(cal(stk3,newstk))
main()