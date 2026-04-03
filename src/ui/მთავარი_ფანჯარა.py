import tkinter as tk
from src.tools.кисть import Рисование

class 畫板App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Supre-me 슈프리미 Супре-ми სუპრე-მი 秀普里米")
        self.root.geometry("800x600")
        
        self.ჩარჩო = tk.Frame(self.root)
        self.ჩარჩო.pack(side=tk.TOP, fill=tk.X)
        
        self.지우기_버튼 = tk.Button(self.ჩარჩო, text="Очистить | 지우기 | წაშლა | 刪除 | Clear", command=self.чисто)
        self.지우기_버튼.pack(side=tk.LEFT)
        
        self.გამოსვლა = tk.Button(self.ჩარჩო, text="Выход | 나가기 | გასვლა | 離開 | Exit", command=self.root.quit)
        self.გამოსვლა.pack(side=tk.RIGHT)

        self.ტილო = tk.Canvas(self.root, bg="white")
        self.ტილო.pack(fill=tk.BOTH, expand=True)
        
        self.инструмент = Рисование(self.ტილო)
        self.ტილო.bind("<B1-Motion>", self.инструмент.ხატვა)
        self.ტილო.bind("<ButtonRelease-1>", self.инструмент.დასრულება)

    def чисто(self):
        self.ტილო.delete("all")

    def 시작(self):
        self.root.mainloop()
