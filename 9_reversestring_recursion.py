def reverse(str,i):
    n=len(str)
    if i==n:
        return
    reverse(str,i+1)
    print(str[i],end=' ')
    return
   
def main():
    str="hello"
    reverse(str,0)

main()