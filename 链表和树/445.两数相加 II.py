class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    def add(head, n):#尾插法
        while head.next != None:
            head = head.next
        head.next = ListNode(n)

    p1 = l1
    p2 = l2
    jinwei = 0
    newHead = ListNode(-999)
    while p1 != None and p2 != None: # 手动模拟加法
        xy = p1.val + p2.val + jinwei
        jinwei = xy // 10
        xy = xy % 10
        add(newHead, xy)
        p1 = p1.next
        p2 = p2.next
    while p1 != None:
        xy = p1.val + jinwei
        jinwei = xy // 10
        xy = xy % 10
        add(newHead, xy)
        p1 = p1.next
    while p2 != None:
        xy = p2.val + jinwei
        jinwei = xy // 10
        xy = xy % 10
        add(newHead, xy)
        p2 = p2.next
    if jinwei != 0:
        add(newHead, jinwei)
    return newHead.next