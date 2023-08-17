def cal(target):
    n1=0
    n2=1
    while True:
        if fibo(n1,n2)==target:
            return True
        
        if fibo(n1,n2)>target:
            return False
        temp=n1
        n1=n2
        n2=fibo(temp,n2)


def fibo(n1,n2):
    return n1+n2
def main():
    print(cal(11))
    print(cal(5))
    print(cal(13))
    print(cal(4))
main()
