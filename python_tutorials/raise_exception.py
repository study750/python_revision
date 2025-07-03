# def vote(age):
#     if age < 18:
#         raise ValueError("Not eligible to vote")
#     else:
#         print("Eligible to vote")

# try:
#     vote(19)
# except ValueError as e:
#     print(e)


class UnderAgeError(Exception):
    def __init__(self, age):
       print(f"Age {age} is too young to marry!")

def marry(age):
    if age < 21:
        raise UnderAgeError(age)               
    else: 
        print("Marriage allowed")

try:
    marry(18)
except UnderAgeError as e:
    print(e)