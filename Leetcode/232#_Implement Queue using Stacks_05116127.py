class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyQueue:

    def __init__(self):
        
        self.head=None
        self.size=0
        

    def push(self, x: int) -> None:
        
        if self.head is None:
            self.head=Node(x)
            self.size+=1
        else:
            cur=self.head
            while True:
                if cur.next!=None:
                    cur=cur.next
                else:
                    break
            cur.next=Node(x)
                
            self.size+=1
                

    def pop(self) -> int:
        
        if self.size>=2:
            self.size-=1
            temp=self.head.val
            self.head=self.head.next
            return temp
        if self.size==1:
            self.size=0
            temp=self.head.val
            self.head=None
            return temp
                    
            

    def peek(self) -> int:
        
        return self.head.val

    def empty(self) -> bool:
        
        if self.size==0:
            return True
        else:
            return False