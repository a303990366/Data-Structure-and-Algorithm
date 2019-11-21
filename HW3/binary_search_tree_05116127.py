#!/usr/bin/env python
# coding: utf-8

# In[7]:


class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
       

    
    def preorder(self):
        if self:
            print(str(self.val))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()
                
class Solution(object):
    
    def insert(self,root,val):
        if root:
             
            if root.val>=val:
                if root.left:
                    self.insert(root.left,val)
                else:
                    root.left=TreeNode(val)
            else:
                if root.right:
                    self.insert(root.right,val)
                else:
                    root.right=TreeNode(val)
                    
            return self.search(root,val)
#  
    def node_parent(self,root,target,parent=None):
        
        if root.left.val==target or root.right.val==target:
            self.parent=root
            #return root,root.parent
            return self.parent
        if root.val>target:
            
            if root.left:
                 return self.node_parent(root.left,target)
            else:
                return False
        else:
            if root.right:
                 return self.node_parent(root.right,target)
            else:
                return False        
    
    def search(self,root,target):
        if root.val==target:
            #return root,root.parent
            return root
        if root.val>target:
            if root.left:
                return self.search(root.left,target)
            else:
                return False
        else:
            if root.right:
                return self.search(root.right,target)
            else:
                return False
     
    def delete(self,root,target):
        
        while True:
            node=self.search(root,target)
            if node is not False:
                count=0
                if node.left is not None:
                    count+=1
                if node.right is not None:
                    count+=1
                parent=self.node_parent(root,target)
                if count==0:
                    if parent.left == node:
                        parent.left=None
                    else:
                        parent.right=None
                elif count==1:
                    if parent.left == node:
                        if node.left is not None:
                            parent.left=node.left
                            node=None
                        else:
                            parent.left=node.right
                            node=None
                else:
                    while True:
                        if parent.left is node:
                            parent.left.val=node.left.val
                            parent=node
                        else:# parent.right==node:
                            parent.right.val=node.left.val
                            parent=node.left
                        if node.left==None:
                            if node.right==None:
                                node=None
                                break
                            else:
                                node.val=node.right.val
                                node.right=None
                                break
            else: 
                return root

    def modify(self,root,target,new_val):
        while self.search(root,target)!=False:
            self.delete(root,target)
            self.insert(root,new_val)
            
        return root


# In[ ]:




