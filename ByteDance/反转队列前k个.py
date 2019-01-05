from queue import Queue
#利用额外k的栈，先将前k个入栈。再将这k个逆序入队列。再将队列前n-k个，依次入栈一个，出栈入队列一个
#不用额外开辟一个队列
def reverseK(q:Queue,k):
    stack = []
    for i in range(k):
        stack.append(q.get())
    while len(stack)!=0:
        q.put(stack.pop())
    for i in range(q.qsize() - k):
        stack.append(q.get())
        q.put(stack.pop())

q = Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
reverseK(q,3)
print(q)