'''
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。换句话说，第一个字符串的排列之一是第二个字符串的子串。
枚举每个子串：要求子串长度等于s1，并且子串中每个字母出现的次数等于s1中每个字母出现的次数，就说明是s1的一个排列
'''
'''
hashmap保存[i,j]区间的字符出现频率,看有没有等于s1的map的.如果没有,j++,i++,hashmap中减去过期的i对应的字符出现次数一次
因为此题里区间长度固定,所以i和j同步增加,所以此题用i的for循环代替i和jwhile循环
'''
from collections import Counter


def checkInclusion(s1: str, s2: str):
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    # c1 = Counter(s1)
    # for left in range(len(s2) - len(s1)+1):
    #     right = left + len(s1) - 1
    #     #判断[left,right]内的子串是不是s1的排列
    #     c2 = Counter(s2[left:right+1])
    #     if c1.items() == c2.items():
    #         return True
    # return False
    if len(s1) > len(s2):
        return False
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        c1[ord(s1[i]) - ord("a")] += 1
        c2[ord(s2[i]) - ord("a")] += 1
    for left in range(len(s2) - len(s1)): #本来应该到len(s2) - len(s1)+1开区间,但是因为下面有right+1,为防止数组越界,for里少判断最后一组
        right = left + len(s1) -1
        #[left,right]内的子串的出现频率保存在滑动的hashmap即c1,c2中
        if c1 == c2:
            return True
        #统计滑动窗口下一位的字符出现频率
        c2[ord(s2[right+1]) - ord("a")] +=1
        #减去将要过期的left的字符的出现频率
        c2[ord(s2[left]) - ord("a")] -= 1
    #因为for里少判断了最后一组,所以最后返回前要判断最后一组(for里已经更新了最后一组的map)
    return c1 == c2


print(checkInclusion("ab", "eidbaoo"))
