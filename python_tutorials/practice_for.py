# list = [1,2,34,5]

# for i in range(len(list)):
#     print(i ,list[i])

# for i in list:
#     print(i)

# dict = {1:"apple", 2:"banana", 3:"cherry", 4:3, 5:5.6, 6:True, 7:None}

# for key in dict:
#     print(key ,dict[key])

# for key ,value in dict.items():
#     print(key,value)


pairs = [(1, 9), (3, 4), (2, 5)]

pairs.sort(key=lambda x:x[0]%x[1])
print(pairs)
