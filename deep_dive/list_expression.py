# [x for x in data if ...]       # FILTER
# [x if ... else y for x in ...] # TRANSFORM



nums=[1,2,3,4,5]
names=['bhus','sak','shaurya']
list1=[x**2 for x in nums]
list2=[x for x in nums if x%2==0]
list3=[name.upper() for name in names]
print(list1)
print(list2)
print(list3)

matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print(flattened) 





# Cube of only odd numbers from range(10)

# From ["hello", "a", "world", "go"], keep only words with length > 2 and convert to upper

# Flatten this: [[1,2], [3], [4,5,6]] → [1, 2, 3, 4, 5, 6]

list1 = [x**3   for x in range(10) if x%2==0]
print(list1)

list2=["hello", "a", "world", "go"]
list3=[x.upper()  for x in list2 if len(x)>2]
print(list3)

list4= [[1,2], [3], [4,5,6]]
list5= [num for row in list4 for num in row]
print(list5)




# Convert  into a dict with keys as words and values as their first letters
# ➤ Output: {"apple": "a", "banana": "b", ...}

# From list [1, 2, 2, 3, 4], get a set of only squares of even numbers


list1=["apple", "banana", "cherry"]
dicto={word:word[0] for word in list1}
print(dicto)

list2=[1,2,2,3,4]
seti={x:x**2 for x in list2 if x%2==0}
print(seti)


nums = [1, 2, 3, 4, 5, 6]
# key -even val -cube

words = ["jamie", "cersei", "tyrion", "arya", "jon", "sansa"]
# word of len 4 and rev

dicto={val : val**3 for val in nums if val%2==0}
list2 = [x[::-1] for x in words if len(x)>4]
print(dicto)
print(list2)