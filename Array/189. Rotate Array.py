def rotate(nums, k):
    '''
    1.新建一个跟nums同样长度的结果列表，用0填充
    挨个读取nums中的每一个元素 按照它变换后的位置
    赋给结果列表响应位置 最后将nums变量指向结果列表'''
    # ans=[0 for i in range(len(nums))]
    # for i in range(len(nums)):
    #     new_index=(i+k) % len(nums)
    #     ans[new_index]=nums[i]
    # for i in range(len(nums)):
    #     nums[i]=ans[i]
    '''2.重复k次：列表最后一个元素放入t，所有元素右移一个位置，空出的第一个位置填入t
    会超时'''
    # for j in range(k):
    #     t=nums[len(nums)-1]
    #     for i in range(len(nums)-1,0,-1):
    #         nums[i]=nums[i-1]
    #     nums[0]=t

    '''3.从第一个元素开始，将该元素放置到变换后的位置上，原位置上的元素存入临时变量t，再计算该元素变换后的位置，
    将t赋给变换后的位置，而原来的元素以此类推。最终会跳转到第一个元素上。再对第二个元素继续跳转。设置一个计数器count，
    每放置一个变换后的元素就+1，当count==len（nums） 说明所有元素放置成功'''
    k=k%len(nums)
    start=0
    count=0 #记录变换次数 等于len时停止
    while(count < len(nums)):
        current=start #当前没跳转前的位置
        prev=nums[current]  #当前没跳转前的值
        while(True):
            new_index=(current+k) % len(nums)
            prev,nums[new_index]=nums[new_index],prev
            current=new_index
            count+=1
            if(current==start):
                break
        start+=1




    '''4.rotate K 次 就有k个元素从后面跑到前面来
    可以先将数组整体反转 再反转前K个元素 再反转后len-k 个元素
    就可以得到最后的结果'''
    # k=k%len(nums)
    # reverse(nums,0,len(nums)-1)
    # reverse(nums,0,k-1)
    # reverse(nums,k,len(nums)-1)
'''反转算法 ，start end 都是索引
两个指针分别从两端向中间移动
如果是奇数 最中间的元素不会被调换'''
# def reverse(nums,start,end):
#     while(start < end):
#         nums[start],nums[end] = nums[end],nums[start]
#         start+=1
#         end-=1


if __name__ == '__main__':
    nums=[1,2,3,4,5,6,7]
    k=3
    rotate(nums,k)
    print(nums)
