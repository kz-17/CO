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

- 
