def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    '''中心思想：1，如果每个元素n 都放在正确的位置 index n-1 上，只需要从1开始到len（nums）遍历一遍，哪个index上的数字不对，这个index+1就是空缺的最小整数
                2，并且空缺的最小正整数只会在[1,len(nums)+1](极端情况下 [1,2]空缺是3)
                3. 任何负数包括0和任何大于len(nums)的数不会对结果造成影响 ([-9999,1,2,3]空缺是4  [1,2,3,9999]结果是4)'''
    '''思路：循环替换，从第一个元素n开始，找到它应该放置的位置（index为n-1），将index n-1位置的元素放置到临时变量中，将n放置在该位置。再找临时变量中元素的正确位置，
    以此类推，当正确位置的index大于len（nums）-1，则跳过。当正确位置的index小于0，则跳过。遇上正确的元素也跳过。跳过之后，对下一个元素循环替换。'''

    for i, v in enumerate(nums):
        if i != v - 1:
            prev = v
            while (True):
                if prev - 1 < 0 or prev - 1 >= len(nums) or nums[prev - 1] == prev:
                    break
                t = nums[prev - 1]  # 因为数组下标也用到了prev python自带的交换变量方法会出错
                nums[prev - 1] = prev
                prev = t
    for n in range(len(nums)):
        if nums[n] != n + 1:
            return n + 1
    return len(nums)+1


if __name__ == '__main__':
    nums = [0]
    print(firstMissingPositive(nums))
