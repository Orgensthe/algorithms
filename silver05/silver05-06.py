def solution():
    
    
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.before = None
    
    class LinkedList:

        def __init__(self):
            
            self.head = None
            self.tail = None
            self.num_of_data = 0

        def append(self,node):
            
            if self.num_of_data == 0:
                self.head = node
                self.tail = node
            else:
                node.before = self.tail
                self.tail.next = node
                self.tail = node
                self.tail.next = self.head
            
            self.num_of_data +=1
        
        def delete(self,nth):
            if nth > self.num_of_data:
                return IndexError
            temp_Node = self.head
            for i in range(nth-1):
                temp_Node = temp_Node.next
                if self.tail != temp_Node:
                    temp_Node.before.next = temp_Node.next
                    temp_Node.next.before = temp_Node.before
                else:
                    self.tail = temp_Node.before
                    temp_Node.next = self.head
            
            self.num_of_data -=1

        def print(self):
            temp_node = self.head
            while temp_node != self.tail:
                print(temp_node.data , end = ' ')
                temp_node = temp_node.next
            print(self.tail.data)
    temp_Linked_List = LinkedList()
    
    
    
    result = []
    length, nth = str(input()).split(" ")

    for i in range(1,int(length)+1):
        temp_Linked_List.append(Node(i))
    

    temp_node = None
    
    while temp_Linked_List.num_of_data != 0:
        if temp_node == None:
            temp_node = temp_Linked_List.head
            for i in range(1,int(nth)):
                temp_node = temp_node.next
        else:
            for i in range(1,int(nth)+1):
                temp_node = temp_node.next
            
        result.append(temp_node.data)


        temp_node.next.before = temp_node.before
        temp_node.before.next = temp_node.next
        temp_Linked_List.num_of_data -= 1
    

    print(result)


solution()