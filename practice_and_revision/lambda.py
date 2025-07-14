n=input("enter no")
n=int(n)
check = lambda n: "even" if n % 2 == 0 else "odd"
print(check(n))

from functools import reduce
nums=[1,2,3,4,5]
list2=list(map(lambda x:x**2,nums))
list3=list(filter(lambda x:x%2==0 , nums))
nums.sort(key=lambda x : x%5)
print(nums)
print(list2)
print(list3)
print(reduce(lambda x,y:x*y , nums))
