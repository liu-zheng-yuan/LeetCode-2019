# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# class Solution(object):
#     def postorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         stack = []
#         p = root
#         flag = None #标记
#         res = []
#         while p!=None or len(stack)!=0:
#             if p!=None:
#                 stack.append(p)
#                 p = p.left
#             else:
#                 #判断栈顶结点的右子树进栈了没？没，转向右子树，入栈，然后看左子树。有，访问栈顶元素
#                 top = stack[len(stack)-1]
#                 if top.right != None and top.right != flag:
#                     #转向右子树
#                     p = top.right
#                     stack.append(p)
#                     #转向右子树的左子树
#                     p = p.left
#                 else:
#                     top = stack.pop() #真正弹出并访问
#                     #访问
#                     res.append(top.val)
#                     #★标记最近访问过的结点
#                     flag = top
#                     # 访问结束后 重置P结点 可不加 因为数中没用top 而是还用的p
#                     p = None
#
#         return res
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if root == None:
            return None
        stack = []
        flag = None
        p = root
        res = []
        while p!=None or len(stack)!=0:
            if p != None:
                stack.append(p)
                p = p.left
            else:
                top = stack[len(stack)-1]
                if top.right != None and top.right!=flag:
                    p = top.right
                    stack.append(p)
                    p = p.left
                else:
                    top = stack.pop()
                    res.append(top.val)
                    flag = top
        return res