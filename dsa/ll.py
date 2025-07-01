class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class ll:
    def __init__(self):
        self.head=None

    def insert_at_begin(self,data):
        if(self.head==None):
            n = node(data,None)
            self.head=n
            return
        
        n=node(data,self.head)
        self.head=n

    def insert_at_end(self,data):
        if(self.head==None):
            n=node(data,None)
            self.head=n
            return
 
        n=node(data,None)
        itr=self.head
        while itr.next:
            itr=itr.next
        
        itr.next=n

    def Len(self):
        if(self.head==None):
            return 0
 
        count=0
        itr=self.head
        while itr:
            itr=itr.next
            count+=1
        
        return count

    def remove_by_value(self,data):
        if(self.head==None) :
           print("no value presern")
           return
        
        itr=self.head
        while(itr.next.data!=data):
            itr=itr.next

        itr.next=itr.next.next            
    

    def insert_at_any(self, data, index):
        if index < 0 or index > self.Len():
            print("Invalid index")
            return

        if index == 0:
            self.insert_at_begin(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                n = node(data, itr.next)
                itr.next = n
                return
            itr = itr.next
            count += 1

    def Print(self):
        if(self.head==None):
            print("it is empty")
            return
        
        itr = self.head
        s=""

        while(itr):
            s+=str(itr.data)
            itr=itr.next

        return s

    

l = ll()
l.insert_at_begin(1)
l.insert_at_end(2)
l.insert_at_any(3,2)
l.insert_at_any(1.5,1)
print(l.Len())
print(l.Print())
l.remove_by_value(1.5)
print(l.Print())



