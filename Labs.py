s = "()[]{}"
temp = []
top = s[0]
for i in s:
    temp.append(i)
    top = temp[0]
    