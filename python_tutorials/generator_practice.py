def fun():
    a=1
    while True:
        yield a*a
        a+=1


for i in fun():
    if(i>25):
        break
    print(i)