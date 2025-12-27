import os

class VMTranslator:
    def __init__(self, filename):
        self.filename = os.path.basename(filename).replace(".vm", "")
        self.label_count = 0
        # 記憶體段基地址映射
        self.segments = {
            "local": "LCL",
            "argument": "ARG",
            "this": "THIS",
            "that": "THAT"
        }

    def write_push_pop(self, command, segment, index):
        asm = [f"// {command} {segment} {index}"]
        
        if command == "C_PUSH":
            if segment == "constant":
                asm += [f"@{index}", "D=A"]
            elif segment in self.segments:
                asm += [f"@{self.segments[segment]}", "D=M", f"@{index}", "A=D+A", "D=M"]
            elif segment == "temp":
                asm += [f"@{5 + int(index)}", "D=M"]
            elif segment == "pointer":
                target = "THIS" if index == "0" else "THAT"
                asm += [f"@{target}", "D=M"]
            elif segment == "static":
                asm += [f"@{self.filename}.{index}", "D=M"]
            
            # 通用的 Push 結束動作：將 D 的值壓入棧
            asm += ["@SP", "A=M", "M=D", "@SP", "M=M+1"]

        elif command == "C_POP":
            if segment in self.segments:
                asm += [f"@{self.segments[segment]}", "D=M", f"@{index}", "D=D+A", "@R13", "M=D"]
            elif segment == "temp":
                asm += [f"@{5 + int(index)}", "D=A", "@R13", "M=D"]
            elif segment == "pointer":
                target = "THIS" if index == "0" else "THAT"
                asm += [f"@{target}", "D=A", "@R13", "M=D"]
            elif segment == "static":
                asm += [f"@{self.filename}.{index}", "D=A", "@R13", "M=D"]
            
            # 通用的 Pop 結束動作：從棧彈出值到 R13 指向的地址
            asm += ["@SP", "AM=M-1", "D=M", "@R13", "A=M", "M=D"]
            
        return "\n".join(asm)

# 使用範例
translator = VMTranslator("BasicTest.vm")

# 模擬 BasicTest.vm 中的幾條指令
commands = [
    ("C_PUSH", "constant", "10"),
    ("C_POP", "local", "0"),
    ("C_PUSH", "pointer", "1"),
    ("C_PUSH", "static", "8")
]

for cmd, seg, idx in commands:
    print(translator.write_push_pop(cmd, seg, idx))
    print("-" * 20)
