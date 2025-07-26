arr=[1,2,3,4,2,5,1,3]
list=[]
for i in arr:
    if arr.count(i) > 1 and i not in list:
        list.append(i)
print(list)