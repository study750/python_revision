# 🧪 Mini Challenge:
# Create a decorator called announce() that:

# prints "🔔 About to run function..." before

# prints "✅ Function complete!" after

# works on any function (accepts *args, **kwargs)

# Apply it to a function battle(hero) that prints:

def announce(func):
    def wrapper(x):
        print("about to run function")
        print("funcoint complerte")
        result = func(x)
        return result
    return wrapper

@announce
def fun(x):
    return x*2

print(fun(3))
print(fun(4))
print(fun(5))

