a = {1,2,3,4,4,4,4,4,5}
print(a)
b = {"Python",True,2,3.4}
print(b)
c = set([1,2,3,4,3])
print(c)
x = set([0,1,2,3,4])
print("before removing:",x)
x.pop()
print("after removing",x)
x.remove(3)
print("remove number 5:",x)