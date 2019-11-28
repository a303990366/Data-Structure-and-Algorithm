#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Cryptodome.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
       
class MyHashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        
        h=MD5.new()
        h.update(key.encode("utf-8"))
        h=int(h.hexdigest(),16)
        h=int(h%self.capacity)
        if self.data[h]==None:
            self.data[h]=ListNode(key)
        else:
            self.data[h].next=ListNode(key)
        #self.data[h].append(key)
        #用list的append用太順，之後才發現錯誤...
        return 
             
    def remove(self, key):
       
        if self.contains(key)==False:
            return False
        else:
            h=MD5.new()
            h.update(key.encode("utf-8"))
            h=int(h.hexdigest(),16)
            h=int(h%self.capacity)
            if self.data[h]==None:
                return False
            else:
                cur=self.data[h]
                while True:
                    #if cur.next.val==key:
                    if cur.next.val==key:
                        cur.next=None
                        return True
                    elif cur.next==None:
                        return False
                    else:
                        cur=cur.next
        
    def contains(self, key):
        
        h=MD5.new()
        h.update(key.encode("utf-8"))
        h=int(h.hexdigest(),16)
        h=int(h%self.capacity)
        if self.data[h]==None:
            return False
        else:
            cur=self.data[h]
            while True:
                if cur.val==key:
                    return True
                elif cur.next==None:
                    return False
                else:
                    cur=cur.next
                    

hashSet=MyHashSet(3)
hashSet.add("dog")
hashSet.add('pig')
#hashSet.data[2].next.val
rel=hashSet.contains("pig")
print(rel)
rel=hashSet.contains("dog")
print(rel)
rel=hashSet.contains("cat")
print(rel)
hashSet.add('bird')
rel=hashSet.contains("bird")
print(rel)
hashSet.remove('pig')
rel=hashSet.contains("pig")
print(rel)


# In[ ]:




