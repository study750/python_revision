x = input("enter a number:")

y=input("enter another number:")
 


try:
    z=int(x)/int(y)
    print(z)

except Exception as e:
    print(e)

finally:
    "this is printed"