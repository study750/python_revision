a='bhus'
b=300
c=True
d=3.134
print(type(a))
print(type(int))
print(a)
print(b)
print(c)
print(d)

# type of int comes under type class .
#type is masterclass . everyone bows under it .. all clasees
# u can create classes dynamically with it 
# Sword = type('Sword', (object,), {'sharpness': 100})
#          name of class   default   content
# class Sword:
    #sharpness = 100


#variable is just a reference to memory 
# a=14
# b=1
# a is b .. both referencing same memeo

e=b
print(e is b)