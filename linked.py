class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, value):
        temp = self.head
        prev = None
        while temp and temp.value != value:
            prev = temp
            temp = temp.next
        if temp is None:
            return
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
    
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")
