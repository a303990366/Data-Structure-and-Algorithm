# Heap Sort
## 簡介:
###    基於樹狀結構的一種排序方法
## 時間複雜度:
###    NlogN
## 特徵:
###    1.完全二元樹，即父節點下有只有兩個子節點
## 類型:
###    max heap 和 min heap
### 父節點大於子節點即為max heap;反之，則為min heap以及樹根(root)必為最大或是最小  
###<a href="https://ibb.co/6RBdPZS"><img src="https://i.ibb.co/8Dch5Bw/1.png" alt="1" border="0"></a>
## 程式實作概念:
###    1.heapify=>將串列轉為樹狀結構，並反覆比較父節點與子節點間大小，將最大(小)的作為父節點
###    2.排序=>將頂端的值與最後一個值互換，繼續讓目前位於頂端的新值進行heapify的動作

## 排序流程:
###    <a href="https://ibb.co/fSWr7wL"><img src="https://i.ibb.co/4fL4xr3/unnamed.jpg" alt="unnamed" border="0" /></a>
### p.s上述流程圖以max heap作為範例


