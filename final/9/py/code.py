def main():
    # 1. 詢問使用者要輸入多少個數字
    length = int(input("How many numbers? "))
    
    # 2. 初始化變數
    a = []    # 在 Python 中，我們通常使用 list
    sum_val = 0
    i = 0
    
    # 3. 資料輸入與累加迴圈
    while i < length:
        # 讀取輸入並加入列表與總和
        val = int(input("Enter a number: "))
        a.append(val)
        sum_val += val
        i += 1
    
    # 4. 輸出結果 (Python 3 的 // 是整數除法，對應 Jack 的運算方式)
    if length > 0:
        avg = sum_val // length
        print(f"The average is {avg}")
    else:
        print("Length must be greater than 0")

if __name__ == "__main__":
    main()
