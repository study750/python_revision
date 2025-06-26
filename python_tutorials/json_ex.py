dict={}

dict['bhus']={
    "father":"sham",
    "mother":"mani",
}
dict['bhus']['brother'] = "suresh"

dict['shubh']={
    "father":"sanju",
    "mother":"sure",
}

# print(dict)

import json
s= json.dumps(dict)
print(s)
print(type(s))

dict2 = json.loads(s)
print(dict2)
print(type(dict2))