def cal(queue,k):
    q=[]
    stk=[]
    cnt=0
    while(queue!=[]):
        while(cnt<k):
            stk.insert(0,queue[0])
            queue.pop(0)
            cnt+=1

        q.append(queue[0])
        queue.pop(0)
    print(stk)
    print(q)
    while(stk!=[]):
        queue.append(stk[0])
        stk.pop(0)
    while(q!=[]):
        queue.append(q[0])
        q.pop(0)
    return queue

def main():
    queue=[1,2,3,4,5]
    k=3
    print(cal(queue,k))
main()

