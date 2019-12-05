### Hash Table 概念:

#### 希望能夠將存放資料的「Table」的大小降到「真正會存放進Table的資料的數量」，也就是「有用到的key的數量」，如果套用到程式，是指當沒有資料存進某空間時，某空間即回報None。
#### 但是有時候會發生兩筆資料要放進同一個空間，就會產生出collision 的狀況，這可能使得查詢資料時會失敗，造成key的數量不等於table的大小。
#### 那怎麼解決這個問題呢?可以使用linklist將放在同一個空間的資料串在一起。

### Hash Function 概念:

#### 目的是為了要更快速找到物品，希望「每一個空間只放一個物品」，只要拿著key指出與其對應的index，就能保證是該key所要找的物品。在課堂中，物品指的是linklist，用key指向某一個linklist，再歷遍linklist，找到我們要的資料。

### 學習歷程:
#### 這次作業好像跟上次HW3比真的差很多，然後也不知不覺做出來了，可能是有寫過linklist所以基本上沒有甚麼問題，只有MD5需要再思考一下。
#### 這一次作業發現最多錯誤的是在linklist內添加值的時候，其實是自己有點小蠢，因為是用陣列去包裝linklist，所以很自然地用append函式添加值，那class裡面沒有這個函式所以當然會報錯。

### 參考來源:
#### http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
#### 資料結構與演算法 Hash Table 老師簡報 
