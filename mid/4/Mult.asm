// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
// The algorithm is based on repetitive addition.

//// Replace this comment with your code.
// 初始化 R2 為 0
    @R2
    M=0

(LOOP)
    // 檢查 R1 是否大於 0，如果 R1 <= 0 則跳到結束
    @R1
    D=M
    @END
    D;JLE    // If R1 <= 0 goto END

    // 執行加法：R2 = R2 + R0
    @R0
    D=M
    @R2
    M=D+M

    // 計數器減 1：R1 = R1 - 1
    @R1
    M=M-1

    // 回到迴圈起點
    @LOOP
    0;JMP

(END)
    @END
    0;JMP    // 無窮迴圈，代表程式結束
