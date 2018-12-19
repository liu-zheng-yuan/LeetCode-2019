# n2logn的 用了二分搜索 实际上还是n3方的暴力 用list和counter来去重
# from collections import Counter
# def threeSum(nums: list):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     length = len(nums)
#     ans = []
#     nums.sort()
#     k=[]
#     for i in range(length - 2):
#         for j in range(i + 1, length - 1):  # 要从i+1开始
#             left = j + 1
#             right = length - 1
#             while left <= right: # 二分搜索进入条件是left等于right 不然left等于right时没法进入判断
#                 mid = (left + right) // 2  # py的地板除
#                 if nums[i] + nums[j] + nums[mid] > 0:
#                     right = mid - 1
#                 elif nums[i] + nums[j] + nums[mid] < 0:
#                     left = mid + 1
#                 elif nums[i] + nums[j] + nums[mid] == 0 and Counter([nums[i], nums[j], nums[mid]]) not in k:
#                     ans.append([nums[i], nums[j], nums[mid]])
#                     k.append(Counter([nums[i], nums[j], nums[mid]]))
#                     break
#                 else:
#                     break
#     return ans

# 用双指针法：先依次确定第一个负数 需要O（n）。然后就变成两数之和。排序之后，一左一右双指针。去重的话，是判断邻近两个数相同就指针移动
# 什么都不做
def threeSum(nums: list):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    length = len(nums)
    ans = []
    nums.sort()
    for i in range(length - 2):
        if i> 0 and nums[i-1] == nums[i]: # 用来防止排序后连续两个一样的数字 会导致重复
            continue
        if nums[i] <= 0:
            left = i + 1
            right = length - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:   # 以下两个while为了防止双指针内部出现重复的两组数组都满足条件
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
    return ans


print(threeSum([-2,0,0,2,2]))
