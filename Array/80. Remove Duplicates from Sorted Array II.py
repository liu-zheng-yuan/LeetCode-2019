def removeDuplicates( nums):
    # if nums==[]:
    #     return 0
    # i =0
    # is_dup_once=False
    # for j in range(1,len(nums)):
    #     if(nums[j]!=nums[i]):
    #         i+=1
    #         nums[i]=nums[j]
    #         is_dup_once=False
    #     elif(nums[j]==nums[i] and is_dup_once==False ):
    #         i += 1
    #         nums[i]=nums[j]
    #         is_dup_once=True
    # return i+1
    # i = 0
    # for n in nums:
    #     if( i < 2 or n != nums[i-2]):
    #         nums[i]=n
    #         i=i+1
    # return i
    # if nums==[]:return 0
    # i=1
    # count=1
    # for j in range(1,len(nums)):
    #     if(nums[j]==nums[j-1]):
    #         count+=1
    #         if(count > 2):
    #             continue
    #     else:
    #         count=1
    #     nums[i]=nums[j]
    #     i+=1
    # return i
    if nums==[]:return 0
    i=1
    count=1
    j=1
    while(j < len(nums)):
        if(nums[j] != nums[j-1]):
            count=1
            nums[i]=nums[j]
            i+=1
        else:
            if(count < 2):
                count+=1
                nums[i]=nums[j]
                i+=1
        j+=1
    return i


if __name__ == '__main__':
    nums=[1,1,1,2,2,3]
    print(removeDuplicates(nums))