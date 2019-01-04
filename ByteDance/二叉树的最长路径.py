# 不等于求树的高度！树的高度就是左右子树高度的最大值+1
# 路径最长指的是路径上结点值加起来和最大
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 解法：有点类似求高度。根结点的路径和最大值的确是左右子树最大值加上根节点的值。★但是子树路径最大值不是子树的左右子树最大值之和
#，而是子树的左右子树路径和中最大的那一个，加上子树根结点本身。（因为如果选择了上溯子树根节点的父节点这条路径，就不能选子树根节点的右子树这条路径）
# 递归函数返回值的定义是以当前结点为“终点”的path之和，所以只能取left和right中较大的那个值
# ，而不是两个都要，
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root:TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        res = -2147483648 #总的路径最大值 全局变量 会在递归中增加
        #返回以root为“终点”的路径之和最大值
        #每次递归res加上 以左右子树根节点为“终点”的路径的最大值 再加上根节点本身的值
        def recursive(root:TreeNode):
            if root == None:
                return 0
            leftMax = recursive(root.left) if recursive(root.left)>0 else 0 #因为有负数情况，如果最大值还是负数 就不加
            rightMax = recursive(root.right) if recursive(root.right)>0 else 0
            global res
            res = max(leftMax+rightMax+root.val,res) #存在root.val是负数 加上了反而比上一层的res更小的情况
            return max(leftMax,rightMax)+root.val
        recursive(root)
        return res


