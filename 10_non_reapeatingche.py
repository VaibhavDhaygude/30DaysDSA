def cal(str):
    flag=False
    for i in range(0,len(str)):
        if i!=0 and flag==False:
            return str[i-1]
        for j in range(0,len(str)):
            if(i!=j and str[i]==str[j]):
                flag=True
            
def main():
    str="programming"
    print(cal(str))

main()


