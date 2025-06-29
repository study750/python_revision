# a=10
# try:
#     print(a/0)
# except Exception as e:
#     print(e)
# finally:
#     print("This will always execute.")

# str =" hello"

# try:
#     print(int(str))
# except Exception as e:
#     print(e)

# try:
#     with open("file.txt", "r") as f:
#         content = f.read()
# except Exception as e:
#     print(e)

a=input("Enter a number: "  )
b=input("Enter another number: "  )

try:
    a=int(a)
    b=int(b)
except Exception as e:
    print("fucker give proper input")

try:
    print(a/b)
except Exception as e:
    print("sucker dont divide by zer0")

finally:
    print("here  cum feels pussy")