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

# 5678