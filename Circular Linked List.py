class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class CreateList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    def add(self,data):
        new_node = Node(data)
        if self.head.data is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
        else:
            print("Nodes of the circular linked list are:")
            print(current.data,"==>")
            while(current.next != self.head):
                current = current.next
                print(current.data,"==>")
class CircularLinkedList():
    c1 = CreateList()
    c1.add("s")
    c1.add("m")
    c1.add("i")
    c1.add("l")
    c1.add("e")
    c1.display()
    
                
              
            
            

