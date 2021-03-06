class Node:
    def __init__(self,val,nextNode=None):
        #nextNode=None 表示沒有下一個
        self.temp_min=val
        #將最小的數字放在temp_min中
        self.val=val
        self.next=nextNode
class MinStack:

    def __init__(self):
       
        self.topNode=None

    def push(self, x: int) -> None:
        #if區塊使用於一開始創建的時候，後來添加值進來都跑else區塊
        #sel.topNode=Node(x,None)的None是預設topNode.next=None
        if self.topNode is None:
            self.topNode=Node(x,None)
        else:
            temp=self.topNode.temp_min
            #sel.topNode=Node(x,self.topNode)的第二個參數是將topNode=topNode.next
            self.topNode=Node(x,self.topNode)
            #一開始else區塊儲存的temp是前一個topNode的val值
            #而在跑過Node(x,self.top.node)後，temp變成新topNode的val值
            if temp>self.topNode.temp_min:
                self.topNode.temp_min=self.topNode.temp_min
            else:
                self.topNode.temp_min=temp

    def pop(self) -> None:
        #將由上至下的第二個箱子變成第一個˙
        self.topNode=self.topNode.next

    def top(self) -> int:
        return self.topNode.val

    def getMin(self) -> int:
        return self.topNode.temp_min

