class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 递归
    # if head == None or head.next == None:
    #     return head
    # newHead = reverseList(head.next)
    # head.next.next = head
    # head.next = None
    # return newHead
    #原地反转
    if head ==None:
        return None
    plast = None
    pcur = head
    newHead =None
    while pcur != None:
        pnext = pcur.next
        if pnext == None:
            newHead = pcur
        pcur.next = plast
        plast = pcur
        pcur = pnext
    return newHead

def add(head,v):
    while head.next != None:
        head=head.next
    head.next = ListNode(v)
head = ListNode(1)
add(head,2)
add(head,3)
add(head,4)
add(head,5)
reverseList(head)