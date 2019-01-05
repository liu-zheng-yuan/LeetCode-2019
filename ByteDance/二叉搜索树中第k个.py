#二叉搜索树的中序遍历就是有序的，有序数组找第k个
def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    stack = []
    count = 1
    p = root
    while p != None or len(stack) != 0:
        if p != None:
            stack.append(p)
            p = p.left
        else:
            top = stack.pop()
            if k == count:
                return top.val
            count += 1
            p = top.right