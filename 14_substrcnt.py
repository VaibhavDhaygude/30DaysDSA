def cal(str,k):
    cnt=0
    for i in range(0,len(str)-(k-1)):
        cnt=cnt+1
    return cnt
def main():
    str='abc'
    k=2
    print(cal(str,k))
main()