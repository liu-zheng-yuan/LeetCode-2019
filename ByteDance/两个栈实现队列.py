class myqueue:
    def __init__(self):
        self.s1 = []  # 用来存的
        self.s2 = []  # 用来颠倒顺序输出的

    def push(self, val):
        self.s1.append(val)

    def pop(self):
        if len(self.s2) != 0:
            return self.s2.pop()
        while len(self.s1) != 0:
            top = self.s1.pop()
            self.s2.append(top)
        return self.s2.pop()

    def front(self):  # 返回队首元素 如果s2 不是空那就是s2的顶 如果s2是空 那就把s1里的转到s2 返回s2的顶
        if len(self.s2) == 0:
            while len(self.s1) != 0:
                top = self.s1.pop()
                self.s2.append(top)
        return self.s2[len(self.s2) - 1]

    def back(self): # 如果s2是空 队尾元素就是s1的栈顶 如果s2 不是空 队尾还是s1的栈顶
        return self.s1[len(self.s1) - 1]

