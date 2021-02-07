class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None
        self.prev_node = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def printList(self):
        node = self.head_node
        while node is not None:
            print(node.value, end=' ')
            if node.next_node is not None:
                print("<->", end=' ')
            node = node.next_node

    def printListReverseOrder(self):
        node = self.head_node
        while node.next_node is not None:
            node = node.next_node
        while node is not None:
            print(node.value, end=' ')
            if node.prev_node is not None:
                print("<->", end=' ')
            node = node.prev_node
            
    def addtotheLast(self, value):
        node = self.head_node
        while node is not None:
            if node.next_node is None:
                temp_node = Node(value) 
                temp_node.prev_node = node
                node.next_node = temp_node
                break
            node = node.next_node

    def addtotheHead(self, value):
        node = self.head_node
        temp_node = Node(value) 
        temp_node.next_node = node
        node.prev_node = temp_node
        self.head_node = temp_node 

    def addAfter(self, value, after_value):
        node = self.head_node
        while node is not None:
            if node.value == after_value:
                temp_node = Node(value) 
                temp_node.next_node = node.next_node 
                temp_node.prev_node = node
                node.next_node = temp_node
                break
            node = node.next_node

    def deleteNodefromMiddle(self, value):
        node = self.head_node
        while node.next_node is not None:
            if node.next_node.value == value:
                node.next_node.next_node.prev_node = node
                node.next_node = node.next_node.next_node
            node = node.next_node

    def deleteFirstNode(self):
        self.head_node.next_node.prev_node = None
        self.head_node = self.head_node.next_node

    def deleteLastNode(self):
        prev_node = self.head_node
        node = self.head_node
        while node.next_node is not None:
            if node.next_node.next_node is None:
                node.next_node = None
                break
            node = node.next_node

if __name__ == "__main__":
    list = LinkedList()
    list.head_node = Node(1)
    list.addtotheLast(2)
    list.addtotheLast(3)
    list.addtotheHead(0)
    list.addAfter(2.5, 2)
    list.addtotheLast(4)
    list.deleteFirstNode()
    list.deleteLastNode()
    list.deleteNodefromMiddle(2.5)
    list.printList()
    print(end='\n')
    list.printListReverseOrder()