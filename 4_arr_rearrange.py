#TC O(n*n)
# def arrange(arr):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if(arr[j]<0):
#                 arr[i],arr[j]=arr[j],arr[i]
#     return arr


#TC O(n)
def arrange(arr):
    queue=[]
    for i in range(0,len(arr)):
        if(arr[i]>=0):
            queue.append(i)
        else:
            if(len(queue)>0 ):
                if(len(queue)>1):
                    if(queue[0]>queue[1]):
                        print(queue[0]," ",queue[1])
                        queue.pop(0)
                        print(queue[0])
                arr[queue[0]],arr[i]=arr[i],arr[queue[0]]
                queue[0]=i

                # queue.pop(0)
            
    return arr




def main():
    arr=[1,-2,3,-4,5,-6]
    print(arrange(arr))
main()