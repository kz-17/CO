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
