def cal(n1,n2):
    mini=min(n1,n2)
    for i in range(mini,-1,-1):
        if n1%i==0 and n2%i==0:
            return i
        

def main():
    n1=21
    n2=35
    print(cal(n1,n2))
main()