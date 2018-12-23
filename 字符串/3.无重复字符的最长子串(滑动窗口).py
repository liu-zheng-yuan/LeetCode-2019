# 滑动窗口法：数组/字符串题里经常用。在需要双重遍历，找符合条件的情况时，可以用一个数据结构（set或deque或hashmap）在区间[i,j)上滑动。
# 数据结构能帮助进行更低复杂度的“求区间最大”“判断重复”“统计出现次数”，一般能从On优化到O1的复杂度.(区间最大用deque保存，判断重复用set实现)
# 所谓滑动即区间扩展.当i一定，j判断完时，保持j不变！，i+=1，继续判断j。能从On2优化到On。
# 因为要求的是子串，不能跳过，所以一旦j不满足，就要进行到下一个i，并且i+=1后，区间内仍然是满足条件的最大或者最长，所以可以j不从0开始
# i+=1时，区间数据结构要记得更新，删除过期的i对应的值
# 一般写法：
'''
i=0 j=0
while i<n && j<n
if (数据结构帮助判断是否满足条件){
    dosomething
    j++
}else 不满足条件{
    i++
}
'''


def lengthOfLongestSubstring(s: str):
    """
    :type s: str
    :rtype: int
    """
    maxlength = 0
    i = 0
    j = 0
    contain_set = set() #用来判断是否有重复字符的set
    while i<len(s) and j < len(s):
        if (s[j] not in contain_set):
            contain_set.add(s[j])
            maxlength = max(maxlength,j-i+1)
            j+=1
        else:
            contain_set.remove(s[i])
            i+=1
    return maxlength

print(lengthOfLongestSubstring("abcabcbb"))