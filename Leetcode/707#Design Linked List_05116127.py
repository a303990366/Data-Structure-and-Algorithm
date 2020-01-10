class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList(object):
 
    def __init__(self):
       
        self.head = None
        self.size = 0
 
    def get(self, index):
       
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        
        for i in range(0, index):            
            cur = cur.next

        return cur.val
    
    def addAtHead(self, val):
        
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size += 1
 
    def addAtTail(self, val):
        
        cur = self.head
        if cur is None:
            self.head = Node(val)
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(val)

        self.size += 1
        
 
    def addAtIndex(self, index, val):
      
        if index > self.size:
            return
        
        cur = self.head
        newNode = Node(val)
                
        if index <= 0:
            newNode.next = cur
            self.head = newNode
        else:                        
            for i in range(index - 1):
                cur = cur.next
            newNode.next = cur.next
            cur.next = newNode    
            
        self.size += 1
        
    def deleteAtIndex(self, index):
        
        if  index >= self.size:
            return
        if index<0:
            return 
        
        cur = self.head
        
        if index == 0:
            self.head = self.head.next
        else:
            for i in range(0, index - 1):
                cur = cur.next
            cur.next = cur.next.next              
 
        self.size -= 1