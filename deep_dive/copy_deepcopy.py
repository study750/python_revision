import copy
a=[1,2,3]
b=copy.deepcopy(a)
print(b)
b[0]=4
print(a)


[1, 2, 3]
[1, 2, 3]


b = a              # assignment
c = a[:]           # shallow copy via slicing
d = list(a)        # another shallow copy
e = copy.copy(a)   # shallow copy
f = copy.deepcopy(a)  # deep copy