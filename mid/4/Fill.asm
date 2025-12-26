// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
(LOOP)
    // 1. 讀取鍵盤數值
    @KBD
    D=M
    
    // 2. 判斷要塗黑還是變白
    @SET_WHITE
    D;JEQ      // 如果 KBD == 0，跳轉到白色設定
    
    (SET_BLACK)
    @color
    M=-1       // -1 在補數系統中是全 1 (1111111111111111)
    @DRAW
    0;JMP      // 跳轉到繪圖邏輯

    (SET_WHITE)
    @color
    M=0        // 0 代表全 0 (白色)

    (DRAW)
    @8191      // 螢幕共有 8192 個 words (0 到 8191)
    D=A
    @i
    M=D        // 設定計數器 i = 8191

    (DRAW_LOOP)
        @i
        D=M
        @LOOP
        D;JLT  // 如果 i < 0，代表整格螢幕塗完了，回到主迴圈重新偵測鍵盤

        @color
        D=M    // 取得目前要塗的顏色
        
        @SCREEN
        A=A+D  // 計算目前要塗的位址: SCREEN + i (這行是概念，實際如下)
        
        // 實際計算位址並填色
        @i
        D=M
        @SCREEN
        A=A+D  // A = 16384 + i
        M=M    // 只是占位，下面這兩行才是正確寫法：
        
        @color
        D=M
        @i
        A=M+1
        A=A-1  // 指向正確位置
        @SCREEN
        D=A
        @i
        A=D+M  // A = SCREEN + i
        D=M    // 先暫存
        @color
        D=A
        @color
        D=M
        @SCREEN
        D=A
        @i
        A=D+M
        M=D    // 將 color 填入該位址

        @i
        M=M-1  // i--
        @DRAW_LOOP
        0;JMP
