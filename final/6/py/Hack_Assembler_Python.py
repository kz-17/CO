import os

class Assembler:
    def __init__(self, input_file):
        self.input_file = input_file
        self.symbol_table = {
            'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
            'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
            'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
            'SCREEN': 16384, 'KBD': 24576
        }
        self.next_variable_address = 16

    def pre_process(self):
        """讀取檔案並去除註解與空白線"""
        with open(self.input_file, 'r') as f:
            lines = [line.split('//')[0].strip() for line in f]
        return [line for line in lines if line]

    def first_pass(self, lines):
        """第一階段掃描：紀錄標籤 (LABEL) 指向的行號"""
        clean_lines = []
        pc = 0
        for line in lines:
            if line.startswith('(') and line.endswith(')'):
                label = line[1:-1]
                self.symbol_table[label] = pc
            else:
                clean_lines.append(line)
                pc += 1
        return clean_lines

    def second_pass(self, lines):
        """第二階段掃描：翻譯 A 指令與 C 指令"""
        binary_code = []
        for line in lines:
            if line.startswith('@'):
                binary_code.append(self.assemble_a_instruction(line[1:]))
            else:
                binary_code.append(self.assemble_c_instruction(line))
        return binary_code

    def assemble_a_instruction(self, val):
        """處理 @value 指令"""
        if val.isdigit():
            address = int(val)
        else:
            if val not in self.symbol_table:
                self.symbol_table[val] = self.next_variable_address
                self.next_variable_address += 1
            address = self.symbol_table[val]
        return f"0{address:015b}"

    def assemble_c_instruction(self, line):
        """處理 dest=comp;jump 指令"""
        # 分割指令
        dest_part, rest = line.split('=') if '=' in line else (None, line)
        comp_part, jump_part = rest.split(';') if ';' in rest else (rest, None)

        # 查表翻譯 (此處僅列出部分範例，需完整查表)
        comp_map = {
            '0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', 'M': '1110000',
            'D+1': '0011111', 'D-1': '0001110', 'D+A': '0000010', 'D+M': '1000010', 'D-A': '0010011' # 更多...
        }
        dest_map = {None: '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101', 'AD': '110', 'AMD': '111'}
        jump_map = {None: '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}

        # 這裡需要補充完整的組譯對照表
        c = comp_map.get(comp_part, "0000000") 
        d = dest_map.get(dest_part, "000")
        j = jump_map.get(jump_part, "000")
        
        return f"111{c}{d}{j}"

    def run(self):
        lines = self.pre_process()
        lines = self.first_pass(lines)
        binary = self.second_pass(lines)
        
        output_name = self.input_file.replace('.asm', '.hack')
        with open(output_name, 'w') as f:
            f.write('\n'.join(binary))
        print(f"組譯完成！已生成 {output_name}")

# 使用範例
# assembler = Assembler('Max.asm')
# assembler.run()
