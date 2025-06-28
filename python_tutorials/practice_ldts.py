list = [1,"bhus" , True ,3.5 ,None]
dict ={1:"apple", 2:"banana", 3:"cherry", 4:3, 5:5.6, 6:True, 7:None}
tuple = (1, "bhus", True, 3.5, None)
set = {1, "bhus", True, 3.5, None}

print(list)
print(list[0])
print(list[2:4])
print(list[::-1])
print(list[1:4:2]) #eachs 2nd element

print(dict)
print(dict[2])
#print(dict[2:4])   # no slicing
# print(dict[::-1])
# print(dict[1:4:2])

print(tuple)
print(tuple[0])
print(tuple[2:4])
print(tuple[::-1])
print(tuple[1:4:2])

print("this is for set")
print(set)
set.add("new")
set.remove(1)
print(set)