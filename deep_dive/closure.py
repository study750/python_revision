def outer(cnt):
    
    def inner():
        nonlocal cnt
        cnt+=1
        return cnt
    return inner
    
a = outer(5)
print(a())
print(a())
print(a())

# it let any stupid .. code die .. jsut preserve necessay
# 678


def outer(cnt):
    b=5   
    def inner():
        nonlocal cnt
        cnt+=1
        return cnt
    print(b)
    return inner
    
a = outer(5)    
print(a()) 
print(a())
print(a())





def outer():
    name = "Jon Snow"  # outer is done .. but still inner remembers that b=5 .. after 
    def inner():
        print("Hello", name)
    return inner

a=outer("jon nsow")
a()             

# 5678