#!/usr/bin/env python
# coding: utf-8

# In[14]:


class Solution:
    
    def heap_sort(self,arr):
        num=len(arr)
        final=[]
        for i in range(num,0,-1):
            self.heapify(arr)
            arr[0],arr[num-1]=arr[num-1],arr[0]
            final.insert(0,arr[num-1])
            num-=1
            arr=arr[0:num]
        
        
        return final
    
    
    def heapify(self,arr):
        n=len(arr)
        count=int(n/2)
        for i in range(count,-1,-1):
            j=2*i+1
            k=2*i+2
            if j<n:
            
                if k>=n:
                    if arr[i]<=arr[j]:
                        arr[i],arr[j]=arr[j],arr[i]
                else:
                    largest=i
                    if arr[i]<=arr[j]:
                        largest=j
                    if arr[largest]<arr[k]:
                        largest=k
                    arr[i],arr[largest]=arr[largest],arr[i]
            
        return arr


# In[15]:


#output=Solution().heap_sort(arr)

