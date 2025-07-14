# Write a function combine_all() that takes:

# any number of positional numbers (*args)

# any number of keyword multipliers like x=2, y=3

# Your function should:

# Add all positional args

# Multiply that sum by the sum of all values in kwargs

def combine_all(*args,**kwargs):
    tot=0 
    for i in args:
        tot+=i

    tot2= 0
    for k,v in kwargs.items():
        tot2+=v

    return tot*tot2

print(combine_all(2,3,4,x=10,y=2))
