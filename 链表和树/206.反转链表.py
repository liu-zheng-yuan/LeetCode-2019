class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList( head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    #1.递归做法：recursive（head） 返回head链表反转后的头节点
    # def recursive(cur:ListNode):
    #     if cur == None or cur.next ==None:
    #         return cur
    #     # 递归地找到下一个节点反转后的头节点 一直向上返回的就是它
    #     newHead = recursive(cur.next)
    #     #反转操作
    #     cur.next.next = cur
    #     cur.next = None   # 反转下一个节点后 要记得将当前节点的next设置为none
    #     return newHead
    # return recursive(head)

    #2.用栈模拟递归
    # def useStack(head):
    #     if head == None:
    #         return head
    #     stack = []
    #     p = head
    #     while p!=None:
    #         stack.append(p)
    #         p = p.next
    #     newHead = stack[len(stack) - 1]
    #     while len(stack) != 0:
    #         cur = stack.pop()
    #         if len(stack) != 0:
    #             last = stack[len(stack) - 1]
    #             cur.next = last
    #             last.next = None
    #         else:
    #             cur.next = None
    #     return newHead
    # return useStack(head)

    #3.循环遍历，原地反转
    # def inPlace(head):
    #     if head == None:
    #         return head
    #     plast = None # 当前节点的上一个节点的指针
    #     pcur = head
    #     pnext = None
    #     newHead = None
    #     while pcur != None:
    #         pnext = pcur.next
    #         #如果到了尾节点，那当前pcur就是新头节点
    #         if pnext == None:
    #             newHead = pcur
    #         pcur.next = plast
    #         plast = pcur
    #         pcur = pnext
    #     return newHead
    # return inPlace(head)

    #4.新建链表，依次头插
    if head == None:
        return None
    newHead = ListNode(-999)
    p1 = newHead.next
    p = head
    while p != None:
        nowNode =ListNode(p.val)
        nowNode.next = p1
        newHead.next = nowNode
        p1 = nowNode
        p = p.next
    return newHead.next

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