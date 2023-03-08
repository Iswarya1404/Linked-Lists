class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL():
    def __init__(self):
        self.head = None
    def insert_position(self,pos):
        new_node = Node(30)
        temp = self.head
        for i in range(1,pos-1):
            temp = temp.next
        new_node.prev = temp
        new_node.next = temp.next
        temp.next.prev = new_node
        temp.next = new_node
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"<==>",end = " ")
                temp = temp.next
obj = DLL()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(40)
n2.next = n3
n3.prev = n2
print("before insertion")
obj.display()
print(" ")
print("after insertion")
obj.insert_position(3)
obj.display()

