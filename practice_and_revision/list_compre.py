# Make a list of cubes of all even numbers from 1 to 10
# lis
# From ["hello", "a", "world", "go"], keep words with len > 2 and convert to uppercase

# Flatten this list [[10, 20], [30], [40, 50, 60]]

# Replace numbers divisible by 3 with "Fizz", else keep number

# Make a list of (x, y) pairs where x from [1, 2] and y from [3, 4], but only if sum is even


matrix =[[10, 20], [30], [40, 50, 60]]
names=["hello", "a", "world", "go"]

list1= list(x**3 for x in range(1,11) if x%2==0)
list2=list(word.upper() for word in names if len(word)>2)
list3= list(num for row in matrix for num in row)
list4=list("fizz" if x%3==0 else x for x in range(1,21))
list5=list((x,y) for x in [1,2] for y in [3,4])




nums = [1, 2, 3, 4, 5, 6]
names = ["Jon", "Arya", "Sansa", "Tyrion", "Robb"]


# 🧪 1. Cube all even numbers using map() + lambda
cube=list(map(lambda x:x**3, nums))
# 2. Filter out only odd numbers using filter() + lambda
filter_odd=list(filter(lambda x:x%2!=0 , nums))
# 3. Multiply each number by its own index (i.e., val * index) using map() + lambda + enumerate()
map_index=list(map(lambda val*index for val,index in nums.enumerate()))
#  Create list of strings like "Even-4" or "Odd-3" for each number using map()
str=list(map('even',val if val%2==0 else 'odd',val for val in nums.enumerate()))
#   Use reduce() + lambda to multiply all numbers in the list (product)
#  6. Filter names that start with consonants using filter() + lambda
# 7. Sort names by length using lambda in sorted()
# 8. Sort names by last character using lambda in sort()
#  Convert names to "Name: <uppercase>" using map() + lambda