def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    # """
    # i=0
    # n=len(nums)
    # while i < n:
    #     j=i+1
    #     while(j < n):
    #         if(nums[i]==nums[j]):
    #             t=j+1
    #             while(t<n):
    #                 nums[t-1]=nums[t]
    #                 t=t+1
    #             n=n-1
    #         else:
    #             break
    #     i=i+1
    #
    # return n

    if nums==[]:
        return 0
    i=0
    for j in range(1,len(nums)):
        if(nums[j]!=nums[i]):
            i=i+1
            nums[i]=nums[j]

    return i+1
if __name__ == '__main__':
    nums=[]
    print(removeDuplicates(nums))