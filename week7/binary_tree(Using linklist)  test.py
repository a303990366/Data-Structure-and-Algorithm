#!/usr/bin/env python
# coding: utf-8

# ## 在參考老師簡報前:
# ### 限定:1.如果左側沒有值，則不用歷遍到與左側同層之右側2.完全樹3.addleft需要的index參數是指在某index下增加其左邊子樹(root=root.left)
# ### 需求:1.將樹歷遍 2.查看某index是否有子樹=>程式假設是左側子樹一定要有值，才能在右側子樹添加值
# ### addleft可能狀況:1.整層root.left 和root.right皆為None 2.部分子樹填滿左右側，而部分子樹完全為none 
# ### 3.某子樹可能已經有左側的值，但是沒有右側的值=>問題:是否能增加同層子樹的子樹值?個人覺得可以
# 
# ## 在參考老師簡報後:
# ### 疑問:樹狀結構一定要對稱嗎?還是沒對稱結構也可以?
# ### 個人覺得不一定要對稱，選擇性較高
# 

# In[157]:


class Node:
    def __init__(self,val,parent=None,left=None,right=None):
        self.root=None
        self.size=0
        self.val=val
        self.right=left
        self.left=right
        self.parent=parent


# In[197]:


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
            return -1
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
            return -1
        self.size+=1
        cur.right=Node(val,cur)


# In[302]:


output=Linklist()
output.add_root(6)
output.add_left(0,5)
output.add_right(0,4)
output.add_left(1,3)
output.add_right(1,2)
output.add_left(3,1)
## 錯誤:1在index=4的left 出現
#output.add_left(4,1)
## 沒出錯
#output.add_left(2,1)
## 錯誤:1在index=4的left 出現


# In[303]:


output.size


# In[304]:


output.root.left.val


# In[305]:


output.root.right.val


# In[306]:


output.root.left.left.val


# In[307]:


output.root.left.right.val


# In[309]:


output.root.left.left.left.val


# In[310]:


output.root.left.right.left.val


# ### 一開始放置數值都很正常，但是要執行output.add_left(3,1)時，
# ### 在預期路徑(output.root.left.left.left.val)找不到數值，但self.size卻仍有增加
# ### 開始嘗試找尋不同路徑，發現在(output.root.left.right.left.val)
# ### 後來嘗試在不同parent添加值發現都會跑到output.root.left.right.left這裡
# ### 程式需要再修改

# In[ ]:




