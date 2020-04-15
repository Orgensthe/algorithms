class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        result = []

        node =self.head
        while node != None:
            result.append(node.data)
            node = node.next
        return result

node = Node(1)
node1 =  Node(2)
node.next = node1

ll = LinkedList()
ll.head = node

print(ll.traverse())