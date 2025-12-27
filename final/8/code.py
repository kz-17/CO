def main_fibonacci(n):
    """
    對應 Main.vm 中的 Main.fibonacci 函式。
    遞迴計算斐波那契數列的第 n 個數字。
    """
    # 基礎情況：if n < 2 return n
    if n < 2:
        return n
    else:
        # 遞迴情況：return fib(n-2) + fib(n-1)
        return main_fibonacci(n - 2) + main_fibonacci(n - 1)

def sys_init():
    """
    對應 Sys.vm 中的 Sys.init 函式。
    初始化計算參數並啟動程式。
    """
    test_value = 4
    result = main_fibonacci(test_value)
    return result

if __name__ == "__main__":
    # 執行模擬
    print("--- FibonacciElement 執行開始 ---")
    final_result = sys_init()
    print(f"計算結果 (n=4): {final_result}")
    
    # 驗證結果是否符合 FibonacciElement.cmp
    if final_result == 3:
        print("狀態：測試通過！結果與預期檔 (.cmp) 一致。")
    else:
        print("狀態：結果錯誤。")

  
