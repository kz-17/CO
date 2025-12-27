def next_mask(mask):
    """回傳下一個遮罩 (對應 nextMask 函數)"""
    if mask == 0:
        return 1
    else:
        # 在 Jack 中 mask * 2 等同於位元左移
        return mask * 2

def fill_memory(ram, address, length, value):
    """填充連續記憶體空間 (對應 fillMemory 函數)"""
    for i in range(length):
        ram[address + i] = value

def convert(ram, value):
    """將數值轉為二進位並存入模擬的 RAM (對應 convert 函數)"""
    mask = 0
    position = 0
    loop = True
    
    while loop:
        position += 1
        mask = next_mask(mask)
        
        if not (position > 16):
            # 執行位元與 (AND) 運算來檢查位元
            if (value & mask) != 0:
                ram[8000 + position] = 1
            else:
                ram[8000 + position] = 0
        else:
            loop = False

def main():
    # 建立一個長度足以容納到 8016 的列表來模擬 RAM
    ram = [0] * 8017
    
    # 模擬步驟 2: 假設 RAM[8000] 中有一個數值 (例如 13)
    target_value = 13
    ram[8000] = target_value
    
    # 步驟 1: 初始化 RAM[8001..8016] 為 -1
    fill_memory(ram, 8001, 16, -1)
    
    # 步驟 3: 執行轉換
    value_to_convert = ram[8000]
    convert(ram, value_to_convert)
    
    # 輸出結果 (從 RAM[8001] 到 RAM[8016])
    binary_bits = ram[8001:8017]
    print(f"十進位數值: {target_value}")
    print(f"二進位位元 (RAM[8001..8016]): {binary_bits}")

if __name__ == "__main__":
    main()
