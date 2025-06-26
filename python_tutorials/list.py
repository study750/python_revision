list= ['apple', 'banana', 'cherry',3, 5.6, True, None]
list2= ['orange', 'kiwi', 'melon']
print(list[0])
print(list[1:3])
print(list[:2])
print(list[::-1])
print(list[-2])

list.append("orange")
print(list[-1])
print(list+list2)
list.extend(list2)
list.insert(2, "kiwi")
print(list)
list.remove("kiwi")
list.remove("kiwi")
print(list)

print(len(list))
print("banana" in list) 



