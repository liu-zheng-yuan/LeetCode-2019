def longestConsecutive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    longest = 0
    m = {} # 字典 key是nums[i]的值 value是nums[i]所在的连续序列的长度
    #先看nums[i]能不能和它左边或右边拼成一个更长的，如果能长度就是m[num[i]-1]的值加上m[num[i]+1]再加本身的长度1，然后更新这个更长
    #的序列的起始位和末位的字典值，即序列长度
    for i in range(len(nums)):
        if nums[i] not in m.keys(): # 如果nums[i]在map中说明已经处理过了 就跳过重复数字
            left = m[nums[i]-1] if nums[i]-1 in m else 0
            right =m[nums[i]+1] if nums[i]+1 in m else 0
            m[nums[i]] = left+right+1
            #为什么nums[i] - left 就是该最长序列的起始数？
            #因为对于nums[i]而言 left表示以nums[i]-1结尾的连续序列的长度，因为是连续，末尾数减去长度，就是起始的数
            if left != 0:
                m[nums[i] - left] = left+right+1
            if right != 0:
                m[nums[i] + right] = right+left+1
            longest = longest if longest > (left+right+1) else left+right+1

    return longest
print(longestConsecutive([100,4,200,1,3,2]))