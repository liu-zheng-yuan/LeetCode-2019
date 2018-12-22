def findLengthOfLCIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # dp[i] = max{1,dp[i-1]+1} if nums[i] >nums[i-1]
    if nums == []:
        return 0
    dp = [0] * len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            dp[i] = max(1, dp[i - 1] + 1)
        else:
            dp[i] = 1
    maxL = 0
    for i in range(len(nums)):
        if maxL < dp[i]:
            maxL = dp[i]
    return maxL
