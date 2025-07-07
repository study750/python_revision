x = [1, 2, 3]
y = x[:]

print(x == y)  # True — same values
print(x is y)  # False — different memory  copy of list createed


# for i in x[:]:
#     i+=2                       .. create shallow copy

# for i in range(len(x)):
#     i+=2                     .. modify list 