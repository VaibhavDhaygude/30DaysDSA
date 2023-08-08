def cal(str1,str2):
    for i in str1 :
        if i in str2 :
            continue
        else:
            return False
        
    for i in str2 :
        if i in str1 :
            continue
        else:
            return False
    return True

def main():
    str1='listen'
    str2='silent'
    ans=cal(str1,str2)
    if ans==True:
        print("YES!! Given string are anagrams of each other")
    else:
        print("NO!! Given strings are not anagram of each other")    

main()