def main():
    # 1. 詢問數字的數量 (對應 Keyboard.readInt)
    try:
        length = int(input("How many numbers? "))
    except ValueError:
        print("請輸入有效的數字")
        return

    # 2. 初始化陣列與變數
    a = [0] * length  # 雖然 Python 可以動態增加，這裡維持與 Jack 邏輯一致的固定長度
    sum_val = 0
    i = 0

    # 3. 迴圈讀取數字並累加 (對應 while 迴圈)
    while i < length:
        try:
            val = int(input("Enter a number: "))
            a[i] = val
            sum_val += a[i]
            i += 1
        except ValueError:
            print("請輸入整數。")

    # 4. 輸出結果 (注意：Jack 使用的是整數除法 //)
    if length > 0:
        print("The average is", sum_val // length)
    else:
        print("數量必須大於 0")

if __name__ == "__main__":
    main()
