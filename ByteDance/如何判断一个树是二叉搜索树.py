# 1.父节点的值大于左子树中的最大值，小于右子树中的最小值
# 2.中序遍历列表是升序的则是二叉搜索树
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isBST(root:TreeNode):
    p = root
    stack = []
    prev = None #保存前一个结点的值 如果前一个结点的值一直小于当前结点的值 那就是BST
    flag = True
    while p!=None or len(stack) != 0:
        if p!=None:
            stack.append(p)
            p = p.left
        else:
            top = stack.pop()
            if prev == None:
                prev = top.val
            if prev > top.val:
                flag = False
            prev = top.val
            p = top.right

    return flag
root = TreeNode(3)
n1 = TreeNode(2)
n2 = TreeNode(5)
n3 = TreeNode(1)
n4 = TreeNode(6)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
print(isBST(root))