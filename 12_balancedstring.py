def cal(str):
    stack=[]
    for i in str:
        if i=='(' or i=='[' or i=='{':
            stack.append(i)
        elif (i==')' and stack[len(stack)-1]=='(') or (i==']' and stack[len(stack)-1]=='[') or (i=='}' and stack[len(stack)-1]=='{')   :
            stack.pop()
        print(stack)
    if len(stack)!=0:
        return False
    else:
        return True
    
def main():
    str='{({[]})}'
    result=cal(str)
    if result==True:
        print("Given string is balanced!!")
    else:
        print("Given string is not balanced!!")
main()