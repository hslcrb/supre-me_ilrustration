import tkinter as tk

class ფერების_პალიტრა:
    def __init__(self, მშობელი, 도구):
        self.ჩარჩო = tk.Frame(მშობელი)
        self.ჩარჩო.pack(side=tk.LEFT, padx=5)
        
        self.도구 = 도구
        self.ფერები = ["black", "gray", "red", "orange", "yellow", "green", "blue", "purple", "brown", "pink"]
        
        for ფერი in self.ფერები:
            ღილაკი = tk.Button(
                self.ჩარჩო, 
                bg=ფერი, 
                width=2,
                command=lambda f=ფერი: self.변경(f)
            )
            ღილაკი.pack(side=tk.LEFT, padx=1)

    def 변경(self, 顏色):
        self.도구.ფერი = 顏色
