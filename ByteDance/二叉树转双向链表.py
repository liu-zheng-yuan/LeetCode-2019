#对于根节点，把原先指向左子结点的指针调整指向链表前一个结点的指针，原先指向右子结点的指针调整为指向链表下一个结点的指针。
#递归地对每一个子树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def convertToLinkedList(root:TreeNode):
    if root ==None:
        return None
    if root.right==None and root.left == None:
        return root
    #转换左子树
    leftListHead = convertToLinkedList(root.left) #根据节点的左子树转化成的链表的头节点
    p = leftListHead
    #TreeNode没有next p.right就是往链表的下一个节点走
    while p!= None and p.right != None:
        p = p.right
    if leftListHead != None: #如果左子树形成的链表不是空
        #因为是双向链表，两个方向left和right都要设置
        p.right = root
        root.left = p

    #转换右子树
    #注意这里直接将root连接到链表头之前就可以了
    rightListHead = convertToLinkedList(root.right) #根据节点的左子树转化成的链表的头节点
    if rightListHead != None:
        root.right = rightListHead
        rightListHead.left = root

    #返回也要考虑左边链表为空的情况
    return leftListHead if leftListHead != None else root