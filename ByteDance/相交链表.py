class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headB==None or headA==None:
        return None
    p1 = headA
    p2 = headB
    len1 = 1
    len2 = 1
    while p1.next != None:
        len1 += 1
        p1 = p1.next
    while p2.next != None:
        len2 += 1
        p2 = p2.next
    if p1 != p2:
        return None
    # 算出两个链表的长度之差
    diff = abs(len2 - len1)
    # 保证head2最长
    if len1 > len2:
        headB, headA = headA, headB
    # 重置
    p1 = headA
    p2 = headB
    for i in range(diff):
        p2 = p2.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1
node1 = Node(4)
node2 = Node(1)
node3 = Node(8)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
headA =node1

node6 = Node(5)
node7 = Node(0)
node8 = Node(1)
node6.next = node7
node7.next = node8
node8.next = node3
headB = node6

print(getIntersectionNode(headA,headB))