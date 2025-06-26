# f= open("C:\\Users\\waghb\\OneDrive\\Desktop\\ai\\python_tutorials\\test.txt","a")
# f.write("hello me")
# f.close()

fa=open("C:\\Users\\waghb\\OneDrive\\Desktop\\ai\\python_tutorials\\test.txt","r")
# print(fa.read())
# print()              #as it is wholse file is read


# for line in fa:
#     print(line)

for line in fa:
    tokens= line.split(' ')
    print(tokens)
    print(type(tokens))

fa.seek(0)

for line in fa:
    tokens= line.split(' ')
    print(len(tokens))
fa.close()