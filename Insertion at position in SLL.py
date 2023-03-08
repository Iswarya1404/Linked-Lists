
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL():
    def __init__(self):
        self.head=None
    def insert_position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.next = temp.next
        temp.next = np
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp = temp.next
    
obj = SLL()
n1=Node(100)
obj.head=n1
n2=Node(200)
n1.next = n2
n3=Node(400)
n2.next = n3
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insert_position(2,300)
obj.display()