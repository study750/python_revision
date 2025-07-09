# names = ["Alice", "Bob", "Zara"]

# def call(x):
#     return x[0]>x[1]

# names.sort()  # Alphabetical sort
# names.sort(key=lambda x: len(x))  # By length
# names.sort(key=call)  # Passing function itself, not call(names)




# names = ["Alice", "Bob", "Zara"]
# def call(x):
#     print(f"Running call on: {x}")
#     return len(x)

# names.sort(key=call)

# Running call on: Alice
# Running call on: Bob
# Running call on: Zara

square = lambda x:x*2
print(square(5))

nums=[1,2,3,4,5,6]
nums.sort(key = lambda x:len(x))
even=list(filter(lambda x : x%2==0 , nums))
sqs=list(map(lambda x : x**x) , nums)
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, nums)))
print(even)
print(sqs)
