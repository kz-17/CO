def double_val(a):
    return a * 2

def fill(a, size):
    # 在 Python 中，這會建立一個二維列表
    while size > 0:
        size -= 1
        a[size] = [0, 0, 0] # 建立一個長度為 3 的子列表 (對應 Array.new(3))

def main():
    # 初始化陣列 
    a = [0] * 10
    b = [0] * 5
    c = [0] * 1
    
    # Test 1 & 2 的邏輯
    a[3] = 2
    a[4] = 8
    a[5] = 4
    b[a[3]] = a[3] + 3 # b[2] = 5 
    
    # 複雜索引運算 
    # a[b[2]] = a[4] * b[((7 - 2) - 4) + 1] -> a[5] = 8 * b[2] -> 8 * 5 = 40
    index_part = ((7 - a[3]) - double_val(2)) + 1
    a[b[a[3]]] = a[a[5]] * b[index_part]
    
    print(f"Test 1: expected result: 5; actual result: {b[2]}")
    print(f"Test 2: expected result: 40; actual result: {a[5]}")

    # Test 3: Null 測試 [cite: 9, 11]
    c[0] = None
    c = c[0]
    print(f"Test 3: expected result: 0; actual result: {0 if c is None else c}")

    # Test 4 & 5: 二維結構 [cite: 12, 13, 14]
    c = None
    if c is None:
        fill(a, 10) # 將 a 填滿子列表
        c = a[3]    # c 指向 a[3] 這個子列表
        c[1] = 33
        c = a[7]    # c 現在改指向 a[7]
        c[1] = 77
        b = a[3]    # b 指向 a[3]
        b[1] = b[1] + c[1] # 33 + 77 = 110

    print(f"Test 4: expected result: 77; actual result: {c[1]}")
    print(f"Test 5: expected result: 110; actual result: {b[1]}")

if __name__ == "__main__":
    main()
