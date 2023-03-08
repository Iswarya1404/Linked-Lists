class Node():
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL():
    def __init__(self):
        self.head = None
    def delete_beginning(self):
        temp = self.head
        temp.next.prev = None
        self.head = temp.next
        temp.next = None
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
n3 = Node(30)
n2.next = n3
n3.prev = n2
print("before deletion")
obj.display()
print("")
print("after deletion")
obj.delete_beginning()
obj.display()
