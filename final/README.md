### 習題:全由AI生成
# 第六章
Gemini:https://gemini.google.com/share/b5ff2b988831
### 基礎加法 (Add)
**Add.asm**: 最簡單的程式，不含任何符號。用於測試編譯器處理最基本的 A-指令與 C-指令的能力
### 最大值判斷 (Max)
- **Max.asm**: 包含符號與標籤的邏輯判斷程式。
- **MaxL.asm**: `Max.asm` 的無符號版本（Symbol-less）
### 矩形繪製 (Rect)
- **Rect.asm**: 包含循環結構與螢幕輸出指令
- **RectL.asm**: `Rect.asm` 的無符號版本（Symbol-less）
### Pong
- **Pong.asm**: 一個複雜的大型程式，由 Jack 語言編譯而來，包含大量的變數與標籤
- **PongL.asm**: `Pong.asm` 的無符號版本（Symbol-less） 
# 第七章
Gemini:https://gemini.google.com/share/b542e79905cc
### BasicTest
- 測試五種內存段 : local, argument, this, that, temp
### PointerTest
- 專門測試pointer內存段、THIS和THAT指針的修改
### StaticTest
- 測試static 内存段在不同 VM 文件中的處理
### SimpleAdd
- 驗證兩個常數的相加
### StackTest
- 一個複雜的序列，用于測試 VM 對邏輯和比較指令，特别是如何處裡布爾值
# 第八章
Gemini:https://gemini.google.com/share/6c1efded0ed8
### FibonacciElement
- 基礎情況 (Base Case): 若 n < 2，直接回傳 n
- 遞迴情況 (Recursive Step): 若 n \ge 2，則計算並回傳 fib(n-2) + fib(n-1)
### NestedCall
- 測試虛擬機器在處理多層巢狀呼叫（Nested Calls）時的能力
-透過 Sys.vm 檔案中的多個函式互動，驗證堆疊指標（Stack Pointer）與各段暫存器（LCL, ARG, THIS, THAT）在函式呼叫與回傳過程中的變化
### SimpleFunction
- 測試虛擬機器在處理單一函式呼叫時的基礎能力
- 著重於 function 定義、區域變數（local variables）的初始化，以及 return 指令對堆疊與指標的恢復運作
### StaticsTest
- 測試 VM 翻譯器處理不同檔案中**靜態變數（Static Variables）**的隔離能力
- 不同 VM 檔案中的靜態變數應被翻譯成相互獨立的組合語言符號，以避免命名衝突
### BasicLoop
- 關於虛擬機器（VM）控制流（Control Flow）的基礎練習
- 測試 label、goto 以及 if-goto 指令在實作迴圈邏輯時的正確性
- 透過一個簡單的加總程式，驗證 VM 翻譯器是否能正確轉換條件分支指令，並精確管理堆疊與記憶體段
### FibonacciSeries
- 測試虛擬機器處理非遞迴迴圈與 pointer 段操作的能力
- 程式會計算斐波那契數列的前 $n$ 個數字，並將結果依序存入指定的記憶體位址

# 第九章
Gemini:https://gemini.google.com/share/14a10625f76a
### Average
- 計算一組整數的平均值
1. 變數宣告
程式首先定義了 Main 類別與 main 函數，並宣告了所需的變數：  
- Array a: 用於儲存使用者輸入的數字序列
-  int length: 紀錄使用者預計輸入的數字總數
-  int i, sum: i 作為迴圈計數器，sum 則用來累加所有輸入數字的總和
2. 初始化與陣列建立
- 讀取長度：透過 Keyboard.readInt 詢問使用者「要輸入多少個數字？」
- 建立陣列：使用 Array.new(length) 依照使用者指定的長度配置記憶體空間給陣列
### ComplexArrays
- 測試 Jack 語言 處理「複雜陣列（Complex Arrays）」與「巢狀參考」的能力
- 展示了 Jack 語言中陣列本質上是記憶體指標的特性，並透過幾項測試來驗證運算邏輯是否正確
### ConvertToBin
- 將一個 16 位元的十進位整數轉換為二進位表示法，並將結果存放在電腦的記憶體
- 從 RAM[8000] 讀取一個數值
- 將轉換後的 16 個位元（0 或 1）分別存放在 RAM[8001] 到 RAM[8016]
- 在轉換開始前，會先將目標記憶體範圍（RAM[8001]..8016）初始化為 -1，以確保測試結果的正確性
### Fraction
- 定義與使用 物件（Object）
- 建立一個自定義的「分數（Fraction）」資料型別，並執行分數的加法運算
1. 屬性 (Field)
- 宣告了兩個成員變數（field）：numerator (分子) 與 denominator (分母)
2. 建構子 (Constructor)
- new(int x, int y)：建立新的分數物件
- 它會將傳入的參數設定給成員變數，並立即呼叫 reduce() 方法進行約分
- 最後回傳 this（該物件在記憶體中的參考位址）
3. 核心運算方法 (Methods)
- plus(Fraction other)：執行加法運算
- reduce()：自動約分
- print()：以 x/y 的格式將數值顯示在螢幕上
- dispose()：手動釋放記憶體
### HelloWorld
- Jack 程式的基本結構以及如何與內建作業系統（OS）類別進行互動
- 相當於print("Hello world!")
### LIST
- Jack 語言中實作與使用基礎的資料結構：單向鏈結串列（Linked List）
- 列的結構，它是一種遞迴式的資料結構
### Pong
- 構成了一個完整的 Pong（乒乓球）遊戲
- 這套程式碼展示了 Jack 語言處理圖形與物件互動的能力：
1. 封裝：將球、球拍、遊戲邏輯分別寫在不同檔案
2. 事件驅動：透過輪詢鍵盤狀態來改變球拍方向 
3. 座標計算：球的反射角度並非簡單的物理反射，而是透過比例計算重設目的地 (setDestination) 。
### Squre
- 玩家透過鍵盤控制螢幕上一個黑色正方形的移動與大小
- 展示了**物件導向程式設計（OOP）**在 Jack 語言中的應用：
1. 封裝：將繪圖細節封裝在 Square，將規則封裝在 SquareGame
2. 互動性：透過輪詢（Polling）鍵盤狀態來實現即時反饋
3. 資源管理：手動實作 dispose() 以管理系統有限的記憶體資源

# 第十章
Gimini:https://gemini.google.com/share/f714cc72e0dd
### ArrayTest
- 向使用者詢問數字數量，存入陣列，計算總和，最後輸出平均值
### Sqaure Game
- 使用者可以使用方向鍵移動螢幕上的正方形，並按鍵縮放它
### Square
- Square.jack：定義正方形的屬性（位置 x, y 和大小 size）及其行為（移動、增減大小、繪製、清除）
- SquareGame.jack：遊戲主邏輯。負責處理輸入、控制正方形的移動方向，並包含遊戲的主迴圈。
- T.xml (Tokenizer)：詞法分析結果。將程式碼中的每個字（關鍵字、符號、變數名）貼上標籤。
- .xml (Parser)：語法解析結果。將標記組織成樹狀結構
# 第十一章
### Average
- 要求使用者輸入一組數字，並計算它們的平均值
### ComplexArray
- 測試巢狀陣列與指標操作
### ConvertTobin
- 將一個 16 位元的十進位整數轉換為二進位表示法，並將結果存入特定的記憶體位址中
### Pong
- 由四個類別組成，分別負責遊戲主程式、遊戲邏輯、球板以及球的行為
### Seven
- 計算結果為 7
### Square
- 屬性：儲存左上角的座標 (x, y) 以及正方形的長度 
- 繪製與擦除：draw 使用黑色繪製矩形，erase 則使用白色（背景色）將其覆蓋 
- 縮放功能：incSize 和 decSize 會先擦除舊的正方形，改變 size 數值後再重新繪製 
- 移動機制：為了提高效能，移動並非重新繪製整個正方形，而是僅擦除移動後會消失的邊緣，並繪製新出現的邊緣
# 第十二章
Gimini:https://gemini.google.com/share/b3655c55a402
### Array
在 Jack 語言中，陣列被視為 Array 類別的實例  
核心功能：
- new：建立一個指定大小的新陣列
- 特性：陣列可以儲存原始資料型態或物件，且同一個陣列的不同索引處可以儲存不同型態的資料
### Keyboard
- 處理使用者的鍵盤輸入
### Math
- 提供常用的數學函式
### Memory
- 提供對電腦主記憶體（RAM）的直接存取以及動態記憶體分配
### Output
- 負責在螢幕上顯示文字與字元
### Screen
- 管理 512x256 像素的物理螢幕繪圖
### String
- 提供字串物件的操作介面
### Sys
- 提供程式執行的基礎支援服務
