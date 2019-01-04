'''
题目描述：一个链表，奇数位升序偶数位降序，让链表变成升序的。

比如：1 8 3 6 5 4 7 2 9，最后输出1 2 3 4 5 6 7 8 9。

分析：

这道题可以分成三步：

首先根据奇数位和偶数位拆分成两个链表。

然后对偶数链表进行反转。

最后将两个有序链表进行合并。
'''


class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


# 反转链表
def reverse(head: Node):
    newHead = None
    pre = None
    cur = head
    while cur != None:
        pnext = cur.next
        if pnext == None:
            newHead = cur
        cur.next = pre
        pre = cur
        cur = pnext

    return newHead


# 按奇数和偶数拆成两个链表
def divide(head: Node):
    if head == None:
        return (None, None)
    head1 = None
    head2 = None
    p1 = None
    p2 = None
    k = 1
    p = head
    while p != None:

        if k == 1:
            head1 = p
            p1 = head1          #记得要设p1，p2跟踪拆成的链表
                   #每分配一个结点 都要讲这个结点next设为空 防止
        elif k == 2:
            head2 = p
            p2 = head2

        elif k % 2 == 1:
            p1.next = p
            p1 = p

        elif k % 2 == 0:
            p2.next = p
            p2 = p
        p = p.next
        k += 1
    #跳出循环时要讲p1，p2下一个设为空 不然会连到其他链上
    p1.next = None
    p2.next = None
    return (head1, head2)


# 合并两个有序链表
def merge(head1: Node, head2: Node):
    p1 = head1
    p2 = head2
    newHead = None
    pHead = None

    while p1 != None and p2 != None:
        if p1 != None and p2 != None and p1.val <= p2.val:
            if newHead == None:
                newHead = Node(p1.val)
                pHead = newHead
                p1 = p1.next
                continue
            pHead.next = Node(p1.val)
            pHead = pHead.next
            p1 = p1.next
        elif p1 != None and p2 != None and p1.val > p2.val:
            if newHead == None:
                newHead = Node(p2.val)
                pHead = newHead
                p2 = p2.next
                continue
            pHead.next = Node(p2.val)
            pHead = pHead.next
            p2 = p2.next
    while p1 != None:
        pHead.next = Node(p1.val)
        pHead = pHead.next
        p1 = p1.next
    while p2 != None:
        pHead.next = Node(p2.val)
        pHead = pHead.next
        p2 = p2.next
    return newHead


node1 = Node(1)
node2 = Node(8)
node3 = Node(3)
node4 = Node(6)
node5 = Node(5)
node6 = Node(4)
node7 = Node(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

head1 =None
head2 =None
head1,head2 = divide(node1)
head2 = reverse(head2)
newHead = merge(head1,head2)
print(newHead)