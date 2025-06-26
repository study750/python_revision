dict = {1:"apple", 2:"banana", 3:"cherry", 4:3, 5:5.6, 6:True, 7:None}
dict2 = {8:"orange", 9:"kiwi", 10:"melon"}
print(dict)
dict[11] = "grape"
print(dict[11])

del dict[1]
print(dict)

for key in dict:
    print(key, " ",dict[key])