class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root == None:
        return []
    flag = True
    queue = deque()
    ans = []
    queue.append(root)
    while len(queue) != 0:
        size = len(queue)
        temp = []
        for i in range(size):
            p = queue.popleft()
            temp.append(p.val)
            if p.left !=None:
                queue.append(p.left)
            if p.right !=None:
                queue.append(p.right)
        if flag == True:
            ans.append(temp)
        else:
            temp.reverse()
            ans.append(temp)
        flag = False if flag == True else True
    return ans

