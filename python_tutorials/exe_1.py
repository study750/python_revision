dict={}
with open ("C:\\Users\\waghb\\OneDrive\\Desktop\\ai\\python_tutorials\\poem.txt", "r") as fa:
    for line in fa:
        tokens=line.split(" ")
        for token in tokens:
            if token in dict:
                dict[token] += 1
            else:
                dict[token] = 1

maximum = 0
max_key = ""
for key in dict:
    if dict[key] > maximum:
        maximum = dict[key]
        max_key = key

print("The most frequent word is:", max_key)
print("It occurs", maximum, "times.")