### 簡介:
#### 節點與節點所構成的連線稱為路徑(edge)，從一個節點走到另一個節點，或許會有不同的路徑，就像google map 一樣，雖然是一樣的起點跟終點但是不同路徑花費的時間或是金錢成本也都不太一樣。
#### Dijkstra原理:
##### Dijkstra的核心理念為以某一節點作為出發點，計算從該節點出發到所有其他節點的最短路徑，這裡指的「最短路徑」是指edge權重總和最小的路徑。
該演算法首先以某一節點當作出發點，在與其相連且尚未被選取的節點裡，選擇加入離出發點距離最短的節點，並且透過新增的節點更新到達其他節點的距離。 如此重覆加入新節點，直到所有的節點都被加入為止。

#### Kruskal 原理:
##### 按照邊的權重順序（從小到大）將邊加入生成樹中，但是若加入該邊會與生成樹形成環(Loop)則不加入該邊。直到樹中含有(N個頂點-1)條邊為止。這些邊組成的就是該圖的最小生成樹。
#### Dijkstra流程圖:
<a href="https://ibb.co/7jQ5FQh"><img src="https://i.ibb.co/BcGxRGk/IMG-2024.jpg" alt="IMG-2024" border="0"></a>
#### Kruskal 流程圖:
<a href="https://ibb.co/CB3fsTq"><img src="https://i.ibb.co/7vdqN6H/IMG-2025.jpg" alt="IMG-2025" border="0"></a><br /><a target='_blank' href='https://imgbb.com/'>pasta gif</a><br />
#### 學習歷程:
##### 這次作業我是挑kruskal來實作，這次撰寫程式碼的過程的重點應該是找出root，這部分我是參考老師mining spaning tree簡報中的youtube教學影片，參考為如何去判斷是否同一個root，了解概念後基本上就沒有甚麼太大的問題，其餘的就是輸出作業所需要的格式而已。

#### 參考來源: 
##### http://www.csie.ntnu.edu.tw/~u91029/Path.html
##### http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
##### 資料結構與演算法 shortpath 簡報
##### https://zh.wikipedia.org/wiki/%E6%9C%80%E5%B0%8F%E7%94%9F%E6%88%90%E6%A0%91
##### 資料結構與演算法 mininum spanning tree 簡報
