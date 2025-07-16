list1= list(x**3 for x in range(1,11) if x%2==0)
list2=list(word.upper() for word in names if len(word)>2)
list3= list(num for row in matrix for num in row)
list4=list("fizz" if x%3==0 else x for x in range(1,21))
list5=list((x,y) for x in [1,2] for y in [3,4])




cubes = list(map(lambda x: x**3, filter(lambda x: x % 2 == 0, nums)))
rev = list(map(lambda x: x[::-1], filter(lambda x: len(x) > 3, words)))
tags = list(map(lambda x: f"{x}-even" if x % 2 == 0 else f"{x}-odd", nums))
names.sort(key=lambda x: x[-1])
# ➤ [8, 64, 216, 512, 1000]

