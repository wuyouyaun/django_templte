



# a=[1,3,43,54,5]
# b=a
# print(b)
from copy import deepcopy
import copy
listA=[1,2,3,4,["a","b"]]
c=copy.copy(listA)
listA.append(7)
print(listA)
print("1222222222",c)
listA[4].append("c")
print(listA)
print("c浅拷贝",c)
d1 = {"a": 1, "b": 2}
b1=d1
print(b1)
b2=deepcopy(d1)
b1["a"]=11
print(b1)
print(d1)

b2=deepcopy(d1)
print(b2)




a= [1,4,6,3,5,54]
b=sorted(a)
c=set(a)
print(c)
print(b)


a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# b=[i for i in a if i > 0]
# print("正整数个数：%s"%len(b))
#
#
# a=[1,3,5,7]
# a.insert(3,a[0])
# print(a)
# print(a[1:])











a=[1,2,1,2,2,2,3,4,5,6,56,7,1,3,4]
# print(set(a))
print(list(set(a)))
print(sorted(list(set(a))))
# print(a.count(1))
#
# print("ceshi",len(a))
#
# for i in a :
#     print(a.count(i))

#ffddfff
























