class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL():
    def __init__(self):
        self.head = None
    def insert_beginning(self):
        new_node = Node(10)
        temp = self.head
        new_node.next = temp
        temp.prev = new_node
        self.head = new_node
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<==>",end = " ")
                temp = temp.next
obj = DLL()
n1 = Node(20)
obj.head = n1
n2 = Node(30)
n1.next = n2
n2.prev = n1
n3 = Node(40)
n2.next = n3
n3.prev = n2
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insert_beginning()
obj.display()