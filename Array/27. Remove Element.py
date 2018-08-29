def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    # if nums==[]:
    #     return 0
    # nums.sort()
    # begin=-1
    # end=-1
    # for i in range(len(nums)):
    #     if(nums[i] == val):
    #         begin=i
    #         end=i
    #         while( end<=len(nums)-1 and nums[end]==val):
    #             end=end+1
    #         end=end-1
    #         break
    # if(begin==-1):
    #     return len(nums)
    # t=nums[begin]
    # for j in range(begin,end+1):
    #     nums.remove(t)
    # return len(nums)

    # i=0
    # for j in range(len(nums)):
    #     if(nums[j]!=val):
    #         nums[i]=nums[j]
    #         i+=1
    #
    # return i

    n=len(nums)
    i=0
    while(i<n):
        if(nums[i]==val):
            nums[i]=nums[n-1]
            n=n-1
        else:
            i=i+1
    return n

if __name__ == '__main__':
    nums=[3,4,8,5,6,7,8,8]
    val=8
    print(removeElement(nums,val))