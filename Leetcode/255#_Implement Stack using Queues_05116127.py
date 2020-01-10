class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        


class MyStack:

    def __init__(self):
       
        self.head=None
        self.size=0

    def push(self, x: int) -> None:
        
        if self.head is None:
            self.head=Node(x)
        else:
            cur=self.head
            for i in range(self.size-1):
                cur=cur.next
            cur.next=Node(x)
        self.size+=1
    def pop(self) -> int:
        
        if self.size==1:
            temp=self.head.val
            self.head=None
        else:
            cur=self.head
            for i in range(self.size-2):
                cur=cur.next
            temp=cur.next.val
            cur.next=None
        self.size-=1
        return temp

            

    def top(self) -> int:
        
        cur=self.head
        for i in range(self.size-1):
            cur=cur.next
        return cur.val

    def empty(self) -> bool:
        
        if self.size==0:
            return True
        else:
            return False
