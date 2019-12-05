#!/usr/bin/env python
# coding: utf-8

# In[24]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
       

class MyHashSet:
    def __init__(self, capacity=5):
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
            #return False
            return 
        else:
            h=MD5.new()
            h.update(key.encode("utf-8"))
            h=int(h.hexdigest(),16)
            h=int(h%self.capacity)
            if self.data[h]==None:
                #return False
                return
            else:
                #cur=self.data[h]
                while True:
                    if self.data[h].next is not None:
                        if self.data[h].next.val==key:
                            self.data[h].next=None
                            #return True
                            return
                        elif self.data[h].next==None:
                            #return False
                            return 
                        else:
                            self.data[h]=self.data[h].next
                    else:
                        if self.data[h].val==key:
                            self.data[h]=None
                            #return True
                            return 
                        
        
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


##參考來源:
##http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
##資料結構與演算法 Hash Table 老師簡報 





