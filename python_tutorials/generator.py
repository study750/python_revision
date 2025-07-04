def fun():
    a=5
    while(True):
        yield a

        a+=5

for i in fun():  # i is returned by yield
    if(i>50):
        break
    print(i)