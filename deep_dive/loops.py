# Print numbers 1 to 10 using for loop
# Print only even numbers using range
# Use while loop to countdown from 5 to 1
# Break a loop when number reaches 3
for i in range(1,11):
    print(i)

for i in range(0,11,2):
    print(i)

a=5
while(a>0):
    print(a)
    a-=1

while(a<5):
    if(a==3):
        break
    print(a)
    a+=1


# range uses iterator
# nums=[10,20,30]
# itr= iter(nums)
# print(type(itr))
# print(itr)
# <class 'list_iterator'>
# <list_iterator object at 0x7b3b0148dc90>

# nums=[10,20,30]
# itr= iter(nums)
# print(type(itr))
# print(itr)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))

# 10
# 20
# 30
# Traceback (most recent call last):
#   File "<main.py>", line 8, in <module>
# StopIteration