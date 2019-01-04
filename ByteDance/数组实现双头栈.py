class MyStack:
    def __init__(self, N=None):
        self.N = 10 if N == None else N
        self.arr = [None] * N
        self.top1 = -1
        self.top2 = N

    def put1(self, val):
        if self.top1 + 1 < self.top2:
            self.arr[self.top1 + 1] = val
            self.top1 += 1
        else:
            print("stack1 is full")
    def put2(self, val):
        if self.top1 < self.top2 - 1:
            self.arr[self.top2 - 1] = val
            self.top2 -= 1
        else:
            print("stack2 is full")
    def pop1(self):
        if self.top1 > -1:
            ans = self.arr[self.top1]
            self.arr[self.top1] = None
            self.top1 -= 1
            return ans
    def pop2(self):
        if self.top2 < self.N:
            ans = self.arr[self.top2]
            self.arr[self.top2] = None
            self.top2 += 1
            return ans
ms = MyStack(3)
ms.put1(1)
ms.put2(3)
ms.put1(2)
ms.put2(4)
ms.pop1()
ms.pop2()

print(ms)
