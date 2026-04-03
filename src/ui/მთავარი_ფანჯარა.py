import tkinter as tk
from src.tools.кисть import Рисование
from src.ui.палитра import ფერების_პალიტრა
from src.ui.크기_조절기 import РазмерКисти
from src.tools.𓀀_𒀀_מדי_लेखन import 𓀀_आकृति_צורה_𒀀

class 畫板App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Supre-me 슈프리미 Супре-ми სუპრე-მი 秀普里米 𓀀 𒀀 चित्र צורה")
        self.root.geometry("1100x800")
        
        self.ტილო = tk.Canvas(self.root, bg="white")
        self.інструмент = Рисование(self.ტილო)
        self.ආକୃති_도구 = 𓀀_आकृति_צורה_𒀀(self.ტილო)
        
        # '​' is a Zero Width Space character (invisible)
        self.공구상자 = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        self.공구상자.pack(side=tk.TOP, fill=tk.X)
        
        self.палитра = ფერების_პალიტრა(self.공구상자, self.інструмент)
        self.სრიალი = РазмерКисти(self.공구상자, self.інструмент)
        
        self.현_모드 = "자유" # brush
        
        # Tools row
        self.형상_패널 = tk.Frame(self.공구상자, bg="#f0f0f0")
        self.형상_패널.pack(side=tk.LEFT, padx=10)
        
        # Using Zero Width Space in labels
        tk.Button(self.형상_패널, text="🖌️ Карандаш | ​붓 | 𓏟 | लेखन", command=self.선택_붓).pack(side=tk.LEFT)
        tk.Button(self.형상_패널, text="⬛ Четырёхугольник | 네​모 | 𓄹 | चतुर्भुज", command=lambda: self.선택_형상("rect")).pack(side=tk.LEFT)
        tk.Button(self.형상_패널, text="🟡 Эллипс | 타​원 | 𒀀 | दीर्घवृत्त", command=lambda: self.선택_형상("oval")).pack(side=tk.LEFT)
        tk.Button(self.형상_패널, text="➖ Линия | 직​선 | 𓐮 | रेखा", command=lambda: self.선택_형상("line")).pack(side=tk.LEFT)
        
        self.지우개_버튼 = tk.Button(self.형상_패널, text="𓀁 საშლელი", command=self.사용_지우개)
        self.지우개_버튼.pack(side=tk.LEFT, padx=5)

        self.지우기_버튼 = tk.Button(self.형상_패널, text="מחק הכל | 𓀃 𒀀 𓃠", command=self.чисто)
        self.지우기_버튼.pack(side=tk.LEFT, padx=5)
        
        self.გამოსვლა = tk.Button(self.root, text="❌ Выход | 離開 | გასვლა | יציאה", command=self.root.quit, bg="#ffcccc")
        self.გამოსვლა.pack(side=tk.BOTTOM, fill=tk.X)

        self.ტილო.pack(fill=tk.BOTH, expand=True)
        
        self.ტილო.bind("<Button-1>", self.시작_액션)
        self.ტილო.bind("<B1-Motion>", self.이동_액션)
        self.ტილო.bind("<ButtonRelease-1>", self.종료_액션)

    def 선택_붓(self):
        self.현_모드 = "자유"

    def 선택_형상(self, תבנית):
        self.현_모드 = "형상"
        self.ආକୃති_도구.प्रकार = תבנית

    def 시작_액션(self, 이벤트):
        if self.현_모드 == "자유":
            self.інструмент.x = 이벤트.x
            self.інструмент.y = 이벤트.y
        else:
            self.ආକୃති_도구.ฟერი = self.інструмент.ფერი
            self.ආକୃති_도구.גودל = self.інструмент.размер
            self.ආକୃති_도구.𓁹_시작(이벤트)

    def 이동_액션(self, 이벤트):
        if self.현_모드 == "자유":
            self.інструмент.ხატვა(이벤트)
        else:
            self.ආକୃති_도구.𓃠_그리기(이벤트)

    def 종료_액션(self, 이벤트):
        if self.현_모드 == "자유":
            self.інструмент.დასრულება(이벤트)
        else:
            self.ආକୃති_도구.𓏏_종료(이벤트)

    def 사용_지우개(self):
        self.현_모드 = "자유"
        self.інструмент.ფერი = "white"

    def чисто(self):
        self.ტილო.delete("all")

    def 시작(self):
        self.root.mainloop()

