# Make a closure that:starts with count = 0 returns a function every time you call it, it increases and returns the count
def outer():
    x=5
    def inner():
        nonlocal x
        print(x)
        x+=1

    return inner

a = outer()
# a()
# a()
# a()
# a()

# Create a closure called make_counter(start) that:

# Starts counting from start

# Every time the returned function is called, it increases by 2

# Keeps track of its own state

def make_counter(start):
    def inner():
        nonlocal start
        start+=2
        return start
    return inner

b=make_counter(5)
print(b())
print(b())
print(b())


