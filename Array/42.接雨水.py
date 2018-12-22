def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    """
    先遍历一遍找到最高点，然后分别从两边开始，往最高点所在位置遍历，水位只会增高不会减小，且一直和最近遇到的最大高度持平，这样知道了实时水位，就可以边遍历边计算面积。
    从最两边到最高点，海拔高度下降的时候计算水位，左边最近比他高的海拔 减去 自己的海拔 ，这是该海拔的水位量。当遇到更高的海拔的时候更新海拔高度。
    """
    maxHight = 0  # 最高点的高度
    maxIndex = 0  # 最高点的index
    maxHLeft = 0  # 从最左边开始到中间的动态的最高度
    maxHRight = 0  # 从最右边开始到中间的动态的最高度
    count = 0  # 总的积水大小
    for index in range(len(height)):
        if height[index] > maxHight:
            maxIndex = index
            maxHight = height[index]
    for i in range(maxIndex):
        if height[i] >= maxHLeft:
            maxHLeft = height[i]
        else:
            count += maxHLeft - height[i]
    for j in range(len(height) - 1, maxIndex, -1):
        if height[j] >= maxHRight:
            maxHRight = height[j]
        else:
            count += maxHRight - height[j]
    return count
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))