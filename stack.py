class node:
    def __init__(self,data):
        self.data=data 
        self.next=None
class stack:
    def __init__(self):
        self.__head=None
        self.__count=0
    def push(self,element):
        newnode=node(element)
        newnode.next=self.__head
        self.__head=newnode
        self.__count+=1
    def pop(self):   
        if self.isEmpty() is True:
            print("empty")
            return
        data =self.__head.data
        self.__head=self.__head.next
        self.__count-=1
        return data
    def top(self):   
        if self.isEmpty() is True:
            print("empty")
            return
        data =self.__head.data
        return data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size()==0

s=stack()
s.push(10)
s.push(20)
s.push(30)
s.pop()
while s.isEmpty() is False:
    print(s.pop())
s.top()
"""
20
10
empty"""
