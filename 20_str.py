# Problem statement:
# Given a sequence of n strings, the task is to check if any two similar words
# come together and then destroy each other then print the number of words left in the 
# sequence after this pairwise destruction.
# Input : ab aa aa bcd ab
# Output : 3

def cal(arr):
    dicti={}
    cnt=0
    for i in range(len(arr)):
        if arr[i] in dicti:
            dicti[arr[i]]=dicti[arr[i]]+1
        else:
            dicti[arr[i]]=1
    print(dicti)
    for i in dicti:
        if dicti[i]%2==1:
            cnt=cnt+1
    return cnt
def main():
    arr1=["aa","aa","ab","abc","ab"]
    print(cal(arr1))

    arr2=["abc","def","def","abc","def"]
    print(cal(arr2))

    arr3=["hello","world","world","hello"]
    print(cal(arr3))

    arr4=["abcdef","jdbhew","njqw","lkj","aab"]
    print(cal(arr4))
main()