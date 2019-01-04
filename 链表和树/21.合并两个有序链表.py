class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 == None or l2 == None:
        return l1 if l2 == None else l2
    ans = ListNode(-999)
    pAns = ans
    p1 = l1
    p2 = l2
    while p1!=None and p2!=None: #这里判断条件不是p1.next != None  因为最后一个节点的pnext确实是None 但它还有值
        if p1.val < p2.val:
            nowNode = ListNode(p1.val)
            pAns.next = nowNode
            pAns = pAns.next
            p1 = p1.next
        else:
            nowNode = ListNode(p2.val)
            pAns.next = nowNode
            pAns = pAns.next
            p2 = p2.next
    while p1 != None: #同理 合并问题的判断条件不能是next ！= None
        nowNode = ListNode(p1.val)
        pAns.next = nowNode
        pAns = pAns.next
        p1 = p1.next
    while p2 != None:
        nowNode = ListNode(p2.val)
        pAns.next = nowNode
        pAns = pAns.next
        p2 = p2.next
    return ans.next