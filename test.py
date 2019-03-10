# coding=utf-8
class Node{


def __init__(self, x):
    self.val = x
    self.parent = None

}

def findParent(n1, n2):
    p1 = n1
    p2 = n2
    len1 = 0
    len2 = 0
    while p1.parent != None:
        len1 += 1
        p1 = p1.parent
    while p2.parent != None:
        len2 += 1
        p2 = p2.parent
    if len1 > len2:
        diff = len1 - len2
        p1 = head1
        p2 = head2
        for i in range(diff):
            p1 = p1.parent
        while p1 != p2:
            p1 = p1.parent
            p2 = p2.parent
    else:
        diff = len2 - len1
        p1 = head1
        p2 = head2
        for i in range(diff):
            p2 = p2.parent
        while p1 != p2:
            p1 = p1.parent
            p2 = p2.parent
    return p1
