s = ""
list1 = set()
dic = {}
count = 0
# print("s is:", len(s))
if (len(s)==0):
    dic[count] = 0
    # maximum = 0
for i in s:
    # print(i)
    if (i not in list1):
        list1.add(i)
    else:
        dic[count] = len(list1)
        list1.clear()
        list1.add(i)
        count += 1
maximum = max(dic.values(), default=0)

print(maximum)
# print(max(dic.values()))
