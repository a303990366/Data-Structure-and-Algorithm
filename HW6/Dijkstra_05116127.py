#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices
        self.graph = [] 
        self.root_set=set()
        self.graph_dict={}
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def Dijkstra(self, s): 
        pass
    def Kruskal(self):
        select_cost=[]
        minest_index=0
        for i in range(0,len(self.graph)):
            select_cost.append(self.graph[i][2])
        for i in range(len(select_cost)):
            minest_cost=min(select_cost)
            for j in range(0,len(self.graph)):
                if self.graph[j][2]==minest_cost:
                    minest_index=j
                    break
            
            if self.graph[minest_index][0] not in self.root_set or self.graph[minest_index][1] not in self.root_set:
                self.graph_dict['%d-%d' %(self.graph[minest_index][0],
                                          self.graph[minest_index][1])]=self.graph[minest_index][2]
                self.root_set.add(self.graph[minest_index][0])
                self.root_set.add(self.graph[minest_index][1])
            if len(self.graph_dict)==self.V-1:
                break
            select_cost.remove(minest_cost)
        return self.graph_dict
    
#資料來源:    
#資料結構與演算法 mininum spanning tree 簡報
# https://www.youtube.com/watch?v=wuU4DDEUu1w

