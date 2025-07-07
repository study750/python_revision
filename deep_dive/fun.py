def show(*args, **kwargs):
    print(args)
    print(kwargs)


# *args → Multiple positional arguments

# **kwargs → Multiple keyword arguments

show(1, 2, 3, name="Python", level="Hardcore")

square = lambda x,y: x ** x
print(square(4,5))  # 16

def sum(*args):
    sss=0
    for num in args:
        sss+=num
    return sss

print(sum(3,4,5,5))
print(sum(3,4,5,5,5,5,5,5,5))       ### passing unlimited arguments ...
