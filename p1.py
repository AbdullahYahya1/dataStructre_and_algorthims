from typing import List
class node:
    def __init__(self,data=None) -> None:
        self.data=data
        self.next=None
    def __str__(self) -> str:
        return str(self.data) + ' ' + str(self.next)

class linked_list:
    def __init__(self) -> None:
        self.head=node()

    def append(self,data:int)->None:
        temp = self.head
        while(temp.next!=None):
            temp=temp.next
        temp.next=node(data)
    
    def display(self)->None:
        temp=self.head
        while(temp.next!=None):
            temp=temp.next
            print(temp.data)
    def __sizeof__(self) -> int:
        counter=0
        temp=self.head
        while(temp.next!=None):
            counter+=1
            temp=temp.next
        return counter
    
    def get(self , index:int):
        if index > self.__sizeof__()-1 or index < 0:
            return None
        temp = self.head
        counter=0
        index+=1 
        temp=self.head
        while(temp!=None and counter !=index ):
            counter+=1
            temp=temp.next  
        return temp.data
    def erase(self , index):
        if index > self.__sizeof__()-1 or index < 0:
            return 'index out of boundry '
        pre =None
        nextN=self.head
        counter=0 

        while True:
            pre= nextN
            nextN=nextN.next
            if counter == index:
                pre.next = nextN.next 
                return
            counter+=1 




linked = linked_list()
linked.append(1)
linked.append(2)
linked.append(3)
linked.erase(0)
linked.display()
print('size : ',linked.__sizeof__())
i=4
print('index of',i,': ' , linked.get(i))