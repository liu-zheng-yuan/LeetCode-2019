class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    def mergeSort(head,tail):
        if head == tail or head == None:
            return
        # 不断二分的过程中 一半划分出前大后小，并且没一次划分至少区间长度要减小1
        # 找到mid点
        p1 = None # p1一定要从None开始 不然会多走一格
        p2 = head
        # 结束条件和if 都是手动试出来的
        while p2!=tail and p2 != tail.next: #结束条件要设置为等于tail 而不能是None
            if p2 == head:
                p1 = p2
            else:
                p1 = p1.next
            if p2.next != None:
                p2 = p2.next.next
            else:
                p2 = p2.next
        mid = p1.next if p2 == tail else p1
        #排序[head,mid]区间内的数
        mergeSort(head,mid)
        # 排序[mid.next,tail]区间内的数
        mergeSort(mid.next,tail)
        merge(head,mid,tail)
    def merge(head:ListNode,mid:ListNode,tail:ListNode):
        temp=[] # 合并之后 有序的数列
        p1 = head
        p2 = mid.next
        #
        while p1 != mid.next and p2 !=tail.next:
            if p1.val < p2.val:
                temp.append(p1.val)
                p1 = p1.next
            else:
                temp.append(p2.val)
                p2 = p2.next
        while p1!=mid.next:
            temp.append(p1.val)
            p1 = p1.next
        while p2 != tail.next:
            temp.append(p2.val)
            p2=p2.next
        i=0
        while head != tail.next:
            head.val = temp[i]
            head = head.next
            i+=1

    p = head
    tail =head
    while p!=None:
        if p.next == None:
            tail = p
        p = p.next
    mergeSort(head,tail)
    return head


def add(head,v):
    while head.next != None:
        head=head.next
    head.next = ListNode(v)
head = ListNode(5)
add(head,4)
add(head,3)
add(head,2)
add(head,1)
hh=sortList(head)
print({1:1}[2])

