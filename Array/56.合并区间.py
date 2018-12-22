# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def merge(intervals:list):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if len(intervals) == 0 or len(intervals) == 1:
        return intervals
    # 先按start排序，如果前一个的end比后一个的start还大，说明能合并，合并后跟下一个比；如果不能，则再也合并不了了，加入ans
    intervals.sort(key=lambda interval:interval.start)
    ans = []
    for i in range(1,len(intervals)):
        last = intervals[i-1]
        now = intervals[i]
        if last.end > now.start:
            # 不需要实际上把这两个区间合并起来 只要下一个区间和当前区间对比时，当前区间的start和end是合并过之后的结果就行了
            now.start = last.start
            now.end = max(now.end,last.end)
        else:
            ans.append(last)
    # 最后原数组里肯定剩下一个，对比过后的now，要么是所有的都合并完了剩下来的，要加入ans数组
    ans.append(intervals[len(intervals)-1])
    return ans
