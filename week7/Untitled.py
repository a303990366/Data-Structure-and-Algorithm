#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,val,parent=None,left=None,right=None):
        self.root=None
        self.size=0
        self.val=val
        self.right=left
        self.left=right
        self.parent=parent


# In[2]:


class Linklist:
    def __init__(self):
        self.root=None
        self.size=0
    def add_root(self,val):
        if self.root is None:
            self.root=Node(val,self.root,None,None)
            self.size+=1
    def add_left(self,parent,val):
        cur=self.root
        for i in range(0,parent):
            if cur.left is not None:
                cur=cur.left
            if cur.right is not None:
                cur=cur.right
        if cur.left is not None:
            return "place?"
        self.size+=1
        cur.left=Node(val,cur)
        
    def add_right(self,parent,val):
        cur=self.root
        for i in range(0,parent):
            if cur.left is not None:
                cur=cur.left
            if cur.right is not None:
                cur=cur.right
        if cur.right is not None:
            return "place?"
        self.size+=1
        cur.right=Node(val,cur)


# In[3]:


output=Linklist()
output.add_root(6)
output.add_left(0,5)
output.add_right(0,4)
output.add_left(1,3)
output.add_right(1,2)
output.add_left(3,1)
## 錯誤:1在index=2的left 出現
#output.add_left(4,1)
## 沒出錯
#output.add_left(2,1)
## 錯誤:1在index=4的left 出現


# In[7]:


output.root.left.right.left.val


# In[ ]:


def add_left(self,parent,val):
        cur=self.root
        retrun _count=0
        for i in range(0,parent):
            if cur.left is not None:
                if return_count==1:
                    cur=cur.parent#查看前面例子是否會報錯
                    if cur.right is not None:
                        cur=cur.right
                    else:
                        return_count+=1
                        break
                cur=cur.left
            else:
                ## 不一定遠遠小於，看層數以增加迴圈執行次數
                ## 是否檢查右側？
                if i<<parent:
                    # if parent=0時，跳過cur=cur.parent(因為root沒有parent,會報錯)
                    cur=cur.parent
                    return_count+=1
                    if cur.right is not None:
                        cur=cur.right
        if retrun_count==2:
            cur=cur.parent
            return_count=0
            #parent at least 1
            #run for區塊
            
            #當執行次數不到，卻發現左邊遍歷到底，換右邊遍歷
        if cur.left is not None:
            return "place?"
        self.size+=1
        cur.left=Node(val,cur)


# In[9]:


for i in range(0,0):
    print("1")


# In[ ]:




