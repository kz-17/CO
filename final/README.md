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
