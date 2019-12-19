#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,val):
        self.val=val
        self.next=None

class MyStack:
    def __init__(self):
        self.head=None
        self.size=0

    def push1(self, x):
        if self.head is None:
            self.head=Node(x)
        else:
            cur=self.head
            for i in range(self.size-1):
                cur=cur.next
            cur.next=Node(x)
        self.size+=1
    def pop1(self) -> int:
        
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
    
    def top1(self) -> int:
        
        cur=self.head
        for i in range(self.size-1):
            cur=cur.next
        return cur.val
    
    def find1(self,x):
        if self.head!=None:
            cur=self.head
            for i in range(self.size):
                if cur.val==x:
                    return True
                if cur.next==None:
                    return False
                else:
                    cur=cur.next
        else:
            return False

class MyQueue:
    def __init__(self):   
        self.head=None
        self.size=0
        
    def push(self, x):
      
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

    def pop(self):
       
        if self.size>=2:
            self.size-=1
            temp=self.head.val
            self.head=self.head.next
            return temp
        if self.size==1:
            self.size-=1
            temp=self.head.val
            self.head=None
            return temp
        
    def find(self,x):
        cur=self.head
        for i in range(self.size):
            if cur.val==x:
                return True
            if cur.next==None:
                return False
            else:
                cur=cur.next
            
from collections import defaultdict 
  
class Graph:
   
    def __init__(self): 
       
        self.graph = defaultdict(list) 

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s): 
        temp=MyQueue()
        return_list=[]
        temp.push(s)
        for j in range(len(self.graph)):
            for i in range(0,len(self.graph[s])):
                num=self.graph[s][i]
                if temp.find(num)==False:
                    x=self.graph[s][i]
                    if x not in return_list:
                        temp.push(x)
                       
                    else:
                        pass               
            return_list.append(temp.head.val)
            temp.pop()
            if j!=len(self.graph)-1:
                s=temp.head.val 
        return return_list

    def DFS(self, s): 
     
        temp=MyStack()
        return_list=[]
        temp.push1(s)     
        for j in range(len(self.graph)):
            for i in range(0,len(self.graph[s])):
                if s not in return_list:
                    temp.pop1()
                    return_list.append(s)
                num=self.graph[s][i]
                if temp.find1(num)==False:
                    x=self.graph[s][i]
                    if x not in return_list:
                        temp.push1(x)
                        size=temp.size
                        tail=temp.top1()
                    else:
                        pass
                
            if j!=len(self.graph)-1:
                return_list.append(temp.top1())
                s=temp.top1()
                temp.pop1()
                size=temp.size
           
            
        return return_list

#資料來源:
#http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
#http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html
#資料結構與演算法上課簡報depth first search
#資料結構與演算法上課簡報Breadth first search

