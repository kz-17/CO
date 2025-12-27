def main():
    # 1. 向使用者詢問要輸入幾個數字
    length = int(input("How many numbers? "))
    
    # 2. 初始化陣列 (在 Python 中稱為 list)
    a = [0] * length
    i = 0
    
    # 3. 讀取數字並存入陣列
    while i < length:
        a[i] = int(input(f"Enter a number for a[{i}]: "))
        i += 1
    
    # 4. 計算總和
    sum_val = 0
    j = 0
    while j < length:
        sum_val = sum_val + a[j]
        j += 1
        
    # 5. 計算並輸出平均值
    if length > 0:
        print(f"The average is {sum_val / length}")
    else:
        print("Division by zero error!")

if __name__ == "__main__":
    main()
