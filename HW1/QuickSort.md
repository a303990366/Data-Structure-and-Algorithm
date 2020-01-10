## 簡介: 
### 是一種將未排序的數列進行排序的方法
## 特色: 
### 選擇一個數值作為基準點，比該基準點大的放在右堆，比該基準點小放左堆，在左右兩堆分別找基準點進行分類，反覆執行到排序完成。
## 例子:
### 4 2 6 3 5 1
### ----選擇4作為基準點，進行排序後----
### 2 3 1 4 6 5
### 可以觀察到數列尚未排序完成，而且分成了比4小的一堆以及比4大的一堆
### 接下來我們繼續在左右兩堆各選擇一個基準點，進行上述的步驟
### ----選擇2、6作為基準點，並且排序後----
### 1 2 3 4 5 6
### 在排序的過程中，我們可以發現以4作為基準點的左堆是空值，就不用繼續排序了
### 雖然在4的右堆(5、6)我們可以直觀看出已經排序了，但仍需要進行比大小的動作
### 至於一堆裡只有一個值就不用排序了
## 流程圖:
### https://i.ibb.co/5vfGFTg/process.jpg