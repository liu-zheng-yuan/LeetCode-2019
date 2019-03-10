class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def constructFromPrePost(pre, post):
    """
    :type pre: List[int]
    :type post: List[int]
    :rtype: TreeNode
    """
    def recursive(pre,pre_start,pre_end,post,post_start,post_end):
        #根据pre里第一个数 将post分成 左子树和右子树两个部分
        root_val = pre[pre_start]
        root_index = None
        for i in range(post_start,post_end+1):




print(constructFromPrePost([3,9,20,15,7],[9,3,15,20,7]))
print(1)
