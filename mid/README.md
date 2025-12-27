習題:全由AI生成，都只能從名稱猜他要幹嘛
# 第一章
### 基礎邏輯門 (Basic Gates)
- Not,"Nand(in, in)"
- NAnd,"Not(Nand(a, b))"
- Or,"Nand(Not a, Not b)"
- Xor,(a And Not b) Or (Not a And b)
- Mux,(a And Not sel) Or (b And sel)
- DMux,"a = in And Not sel, b = in And sel"
### 多位元邏輯門 (Multi-bit Gates)
- Not16 / And16 / Or16: 對索引 [0] 到 [15] 重複執行對應的基礎門運算
- Mux16: 16 個 Mux 門共用同一個 sel 訊號
### 多路選擇器與解多工器 (Multi-way Gates)
Or8Way
- 將 8 位元輸入縮減為 1 位元輸出。只要任一輸入為 1，輸出即為 1
- 實作方法：樹狀結構，兩兩配對進行 Or 運算
Mux4Way16 / Mux8Way16
- 從 4 組或 8 組 16 位元輸入中選取一組輸出
- 設計模式：分層選擇
DMux4Way / DMux8Way
- 將單一輸入分流至 4 或 8 個可能的輸出端
- 設計模式：先根據高位元決定區域（上半部或下半部），再根據低位元精確定位
#  第二章
### 加法器Adders
- HalfAdder : 加總兩個位元
- FullAdder : 加總三個位元 (含進位)
- Add16 : 16 位元加法器
- Inc16 : 16 位元增量器 (out = in + 1)
### ALU
透過 6 個控制位元（zx, nx, zy, ny, f, no）可以產生 18 種不同的運算結果  
控制位元功能：
- zx / zy：將輸入 x 或 y 歸零
- nx / ny：將輸入 x 或 y 按位元取反 (Not)
- f：選擇運算類型（1 為加法 x+y，0 為位元與 x&y）
- no：將最終輸出結果按位元取反
輸出標誌位元 (Flags)：
- zr (Zero Flag)：若輸出為 0 則為 1。實作上使用 Or8Way 檢查所有位元是否皆為 0
- ng (Negative Flag)：若輸出為負則為 1。實作上直接讀取輸出總線的最高位元（out[15]）
# 第三章
Gemini:https://gemini.google.com/share/3d8cbf168c33
### DFF 與時鐘 
所有的記憶體單元最終都建立在 DFF (Data Flip-Flop) 之上。DFF 的基本行為是 out(t+1) = in(t)，這一個週期的延遲正是電腦產生「記憶」的關鍵
### 晶片階層結構   
- 建構順序遵循由下而上 (Bottom-up) 的設計原則
1. Bit (1-bit 暫存器)
2. Register (16-bit 暫存器)
3. RAM8 -> RAM64 -> RAM512 -> RAM4K -> RAM16K
4. PC (程式計數器)
### 基礎儲存單元  
Bit (1-bit Register) : 使用一個 Mux 和一個 DFF 組成。當 load=1 時存入新值，否則維持舊值  
Register (16-bit) : 由 16 個 Bit 晶片並行組成，共享同一個 load 信號
### 隨機存取記憶體 (RAM)
使用 DMux 分發 load 信號，使用 Mux 彙整輸出
### PC
CPU 的導航員，具有遞增、加載與重置功能

# 第四章
Gemini:https://gemini.google.com/share/ab88ddeb4173
### 無窮迴圈 (Infinite Loop)
持續偵測鍵盤狀態
### 鍵盤位址 ($KBD$)
在 Hack 架構中，記憶體位址 $24576$ 會即時反映鍵盤按下的鍵值
### 螢幕位址 ($SCREEN$)
從位址 $16384$ 開始，每一位元 (bit) 代表一個像素

# 第五章
Gemini:https://gemini.google.com/share/fab42dd40430
### CPU.hdl (中央處理器)
- 指令解碼：區分 A-instruction (常數設定) 與 C-instruction (運算)
- 暫存器管理：控制 A (Address) 暫存器與 D (Data) 暫存器的讀寫
- ALU (算術邏輯單元)：執行二進制運算並回傳狀態位元 (zr, ng)
- 跳轉邏輯 (Jump Logic)：根據 ALU 狀態決定程式計數器 (PC) 是遞增 (inc) 還是跳轉 (load)
### Memory.hdl (資料記憶體)
- 將整個電腦的位址空間（32K 字組）進行統一管理，實現 記憶體映射 I/O
- RAM16K：0x0000 - 0x3FFF (一般的數據存儲)
- Screen：0x4000 - 0x5FFF (控制 512x256 像素螢幕輸出)
- Keyboard：0x6000 (讀取目前按下按鍵的 ASCII 掃描碼)
### Computer.hdl (主機)
- 最頂層的晶片，將 ROM、CPU 與 Memory 串聯
- ROM32K：儲存程式指令，接收 CPU 傳來的位址並輸出指令
- 重置 (Reset)：提供重新啟動程式的功能
