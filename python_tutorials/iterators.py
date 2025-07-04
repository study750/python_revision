list=[1,2,3,45,5]
itr = iter(list)

try:
  print()
#   print(next(itr))
#   print(next(itr))
#   print(next(itr))
#   print(next(itr))     
#   print(next(itr))        # give exception once it cross last
#   print(next(itr))
except Exception as e:
  print(e)


#above was for inbuild iterator

class remote():
    def __init__(self):
       self.channels=["hbo","star","sony","warner bros","pixels"]
       self.index=-1

    def __iter__(self):
       return self
    
    def __next__(self):
       self.index+=1
       if(self.index==len(self.channels)):
          raise StopIteration
       
       return self.channels[self.index]
    

r = remote()
iter = iter(r)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))