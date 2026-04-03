import tkinter as tk

class РазмерКисти:
    def __init__(self, მშობელი, 도구):
        self.ჩარჩო = tk.Frame(მშობელი)
        self.ჩარჩო.pack(side=tk.LEFT, padx=10)
        
        self.도구 = 도구
        
        self.라벨 = tk.Label(self.ჩარჩო, text="브러시 크기:")
        self.라벨.pack(side=tk.LEFT)
        
        self.Слайдер = tk.Scale(
            self.ჩარჩო, 
            from_=1, 
            to=50, 
            orient=tk.HORIZONTAL,
            command=self.업데이트
        )
        self.Слайдер.set(3)
        self.Слайдер.pack(side=tk.LEFT)

    def 업데이트(self, 大小):
        self.도구.размер = int(大小)
