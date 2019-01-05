s = "abcdefghi"
i = 0
j = len(s)-1
l = list(s)
while i< j:
    l[i],l[j] = l[j],l[i]
    i+=1
    j-=1
print("".join(l))
#或者用栈 依次进栈再出栈