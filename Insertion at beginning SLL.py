#Single Linked List insertion at beginning
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL():
    def __init__(self):
        self.head = None
    def insertion_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data,"==>",end=" ")
                temp = temp.next
obj = SLL()
n= Node(10)
obj.head=n
n1=Node(100)
obj.head.next=n1
n2=Node(1000)
n1.next=n2
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insertion_beginning(1)
obj.display()

