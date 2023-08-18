import math
def cal(m,n):
    #x^n=m -> n*logx=logm
    ans=math.exp(math.log(m)/n)
    ans=round(ans,4)
    # print(ans)
    if int(ans)==ans:
        return ans
    else:
        return -1
def main():
    print(cal(25,3))
    print(cal(27,3))
    print(cal(8,2))
main()