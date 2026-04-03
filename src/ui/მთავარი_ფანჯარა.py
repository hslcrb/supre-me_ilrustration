import tkinter as tk
from src.tools.кисть import Рисование
from src.ui.палитра import ფერების_პალიტრა
from src.ui.크기_조절기 import РазмерКисти

class 畫板App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Supre-me 슈프리미 Супре-ми სუპრე-მი 秀普里米 - 高級版 (Advanced)")
        self.root.geometry("1000x700")
        
        self.ტილო = tk.Canvas(self.root, bg="white")
        self.инструмент = Рисование(self.ტილო)
        
        self.верхняя_панель = tk.Frame(self.root, bg="#e0e0e0", pady=5)
        self.верхняя_панель.pack(side=tk.TOP, fill=tk.X)
        
        self.공구상자 = tk.Frame(self.верхняя_панель, bg="#e0e0e0")
        self.공구상자.pack(side=tk.LEFT, padx=10)
        
        self.палитра = ფერების_პალიტრა(self.공구상자, self.инструмент)
        self.სრიალი = РазмерКисти(self.공구상자, self.инструмент)
        
        self.지우개_버튼 = tk.Button(self.공구상자, text="Ластик | 지우개 | საშლელი | 橡皮擦 | Eraser", command=self.사용_지우개)
        self.지우개_버튼.pack(side=tk.LEFT, padx=5)

        self.지우기_버튼 = tk.Button(self.공구상자, text="Очистить | 화면 지우기 | წაშლა | 刪除全部 | Clear All", command=self.чисто)
        self.지우기_버튼.pack(side=tk.LEFT, padx=5)
        
        self.გამოსვლა = tk.Button(self.верхняя_панель, text="Выход | 나가기 | გასვლა | 離開 | Exit", command=self.root.quit, bg="#ffcccc")
        self.გამოსვლა.pack(side=tk.RIGHT, padx=10)

        self.ტილო.pack(fill=tk.BOTH, expand=True)
        
        self.ტილო.bind("<B1-Motion>", self.инструмент.ხატვა)
        self.ტილო.bind("<ButtonRelease-1>", self.инструмент.დასრულება)

    def 사용_지우개(self):
        self.инструмент.ფერი = "white"

    def чисто(self):
        self.ტილო.delete("all")

    def 시작(self):
        self.root.mainloop()
