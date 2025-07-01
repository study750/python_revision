from collections import deque

class stack:
    def __init__(self):
        self.dq=deque()

    def push(self,data):
        self.dq.append(data)

    def is_empty(self):
        return len(self.dq) == 0

    def pop(self):
       if(self.is_empty()):
           return 0
       return self.dq.pop()
    
    

    def __iter__(self):
        return iter(self.dq)


st=stack()

s="this is string   "
sn=""

for char in s:
    st.push(char)

while not st.is_empty():
    sn += st.pop()

print(sn)
