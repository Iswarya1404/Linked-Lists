# Insertion at end in SLL
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL():
    def __init__(self):
        self.head = None
    def insertion_end(self,data):
        new_node = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next= new_node
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp = temp.next
obj = SLL()
n= Node(1)
obj.head=n
n1=Node(10)
obj.head.next=n1
n2=Node(100)
n1.next=n2
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insertion_end(1000)
obj.display()
