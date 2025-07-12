# regular → *args → default/keyword → **kwargs




def func(*args):
    cnt=0
    sum=0
    for i in args:
        sum+=i
        cnt+=1
    return sum/cnt


def config(**kwargs):
    for key,val in kwargs.items():
        print(key,val)
        
    print("another")
    for i in kwargs:
        print(i, kwargs[i])
        
        
print(func(1,2,3,4,5))
print(func(1,2,3,4,5,6))
config(theme="dark", font="monospace", autosave=True)
