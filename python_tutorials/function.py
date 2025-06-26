def add(list):
    total=0
    for item in list:
      total+=item
    return total

list1 = [1, 2, 3, 4, 5]
result = add(list1)
print("The sum of the list is:", result)