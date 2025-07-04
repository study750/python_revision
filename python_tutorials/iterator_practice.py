class fibo():
    def __init__(self,limit):
        self.a=0
        self.b=1
        self.idx=0
        self.limit=limit

    def __iter__(self):
        return self

    def __next__(self):
        if(self.idx<self.limit):
            result = self.a + self.b
            self.a = self.b
            self.b = result
            self.idx+=1
            return result 
           
        else:
            raise StopIteration

itr=iter(fibo(5))
while True:
    try:
        print(next(itr))
    except StopIteration:
        break
