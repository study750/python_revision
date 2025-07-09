def decorator_func(func):
    def wrapper():
        print("before dec")
        result = func()
        print(result)
        print("after dec")
       
        
    return wrapper
    
@decorator_func
def greet():
    return "hello"

@decorator_func
def meet():
    return "hi"
greet()
meet()


    



def parent(func):
    def wrapper(*args,**kwargs):
        print("before")
        print("Positional:", args)
        print("Keyword:", kwargs)
        result=func(*args,*kwargs)
        print(result)
        print("after")
        
    return wrapper
      


@parent
def greet(a,b ,age=15):
    return f"{a+b} and {age}"
    
print(greet(3,4))






def limit_calls(func):
    count = 0  # Closure variable

    def wrapper(*args, **kwargs):
        nonlocal count
        if count < 3:
            count += 1
            return func(*args, **kwargs)
        else:
            print("⚠️ Limit reached! Can't call anymore.")
    return wrapper


@limit_calls
def greet(name):
    print(f"Hello, {name}")

greet("Bhu")   # ✅
greet("Snow")  # ✅
greet("King")  # ✅
greet("Stop")  # ⚠️ Blocked
