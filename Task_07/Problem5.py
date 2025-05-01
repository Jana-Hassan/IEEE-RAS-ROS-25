class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertNode(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = newNode
    
    def deleteNode(self, value):
        temp = self.head
        
        if temp and temp.value == value:
            self.head = temp.next
            return
        
        while temp and temp.next:
            if temp.next.value == value:
                temp.next = temp.next.next
                return
            temp = temp.next
    
    def displayNodes(self):
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
        print()


list = LinkedList()

list.insertNode(1)
list.insertNode(2)
list.insertNode(3)
list.insertNode(4)
print("Initial Linked List:")
list.displayNodes()

list.insertNode(5)
print("After inserting a new node (5):")
list.displayNodes()

list.deleteNode(2)
print("After deleting an existing node (2):")
list.displayNodes()
