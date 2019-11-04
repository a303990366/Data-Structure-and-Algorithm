#!/usr/bin/env python
# coding: utf-8

# In[26]:


class Solution:
    
    def merge_sort(self,arr):
        self.arr=arr
        self.p=0
        self.r=len(self.arr)-1
        self.mergeSort(self.arr,self.p,self.r)
        return self.arr
    def mergeSort(self,arr,p,r):
        if p<r:
            q=int((p+r)/2)
            self.mergeSort(arr,p,q)
            self.mergeSort(arr,q+1,r)
            self.merge(arr,p,q,r)
        return alist    
    #主程式
    
    def merge(self,arr,p,q,r):
 
        final=[]
        if r-p<=1:
            if arr[r]<=arr[p]:
                arr[p],arr[r]=arr[r],arr[p]
            
        else:
            n1=arr[p:q+1]
            n2=arr[q+1:r+1]
            i=0
            j=0
    
            for k in range(0,r-p):
            
                if n1[i]<=n2[j] :
                #temp.append(n1[i])
                    final.append(n1[i])
                    i+=1
                else:      
                #temp.append(n2[j])
                    final.append(n2[j])
                    j+=1
                if len(n1)<=i:
                    for k in range(len(n2)-j):
                    #temp.append(n2[j])
                        final.append(n2[j])
                        j+=1
                    break
                elif len(n2)<=j:
                    for k in range(len(n1)-i):
                    #temp.append(n1[i])
                        final.append(n1[i])
                        i+=1
                    break
            
                   
        
    
            arr[p:r+1]=final
        
 

        


# In[29]:


#alist=[-3,2,-4,6,4,2,19,0,-1,0,100,250]


# In[31]:


#output=Solution().merge_sort(alist)
#output


# In[ ]:




