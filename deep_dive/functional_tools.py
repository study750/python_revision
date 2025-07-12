from functools import reduce
nums=[1,2,3,4,5]
nums2= list(map(lambda x : 2*x ,nums))
nums3=list(filter(lambda x:x%2==0 ,nums))
total = reduce(lambda x,y:x*y ,nums)
zipped = list(zip(nums,nums2,nums3))


words = ["hi", "hello", "yo", "winterfell", "go"]
for i, j in enumerate(words):
    if(len(j)>4):
        
      print(i,j)

if any( x=='hi' for x in words):
   print("found")

if all(x for x in words):          # just e.g for demonstartoin .. dont find logic
   print(1)


#most imp
students.sort(key=lambda x: x[1], reverse=True)