def cal(string,start_index):
    ans=0
    stk=[]
    if string[start_index]=='(' or string[start_index]=='[' or string[start_index]=='{':
        pass
    else:
        return -1
    for i in range(start_index,len(string)):
        # print(stk)
        if string[i]=='(' or string[i]=='[' or string[i]=='{':
            stk.insert(0,string[i])
        elif (stk[0]=='(' and string[i]==')') or (stk[0]=='[' and string[i]==']' or (stk[0]=='{' and string[i]=='}')):
            stk.pop(0)
        else:
            continue
        if stk==[]:
            return i
    return -1

def main():
    string="[abc[23]][89]"
    print(cal(string,0))
main()
     



