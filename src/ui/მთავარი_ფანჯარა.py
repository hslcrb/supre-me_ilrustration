import tkinter as tk
from src.tools.кисть import Рисование
from src.ui.палитра import ფერების_პალიტრა
from src.ui.크기_조절기 import РазмерКисти
from src.tools.𓀀_𒀀_מדי_लेखन import 𓀀_आकृति_צורה_𒀀
from src.tools.𓀕_მეხსიერება_מצב import 𓀕_상태_מצב_स्थिति
from src.tools.𓏞_טקסט_पाठ import 𓏞_मजकूर_טקסט_글자
from src.utils.𓃟_შენახვა_שמור_रक्षण import 𓃟_저장_שמירה

class 畫板App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Supre-me 슈프리미 Супре-ми სუპრე-მი 秀普里米 𓀀 𒀀 चित्र צורה")
        self.root.geometry("1100x800")
        
        self.ტილო = tk.Canvas(self.root, bg="white")
        
        self.𓀕_역사 = 𓀕_상태_מצב_स्थिति(self.ტილო)
        self.𓃟_저장_도구 = 𓃟_저장_שמירה(self.ტილო)

        self.інструмент = Рисование(self.ტილო, self.𓀕_역사)
        self.ආକୃති_도구 = 𓀀_आकृति_צורה_𒀀(self.ტილო, self.𓀕_역사)
        self.𓏞_텍스트_도구 = 𓏞_मजकूर_טקסט_글자(self.ტილო, self.𓀕_역사)
        
        მენიუ = tk.Menu(self.root)
        self.root.config(menu=მენიუ)
        
        ფაილი_菜單 = tk.Menu(მენიუ, tearoff=0)
        მენიუ.add_cascade(label="Файл | 파일 | 𓃟 | फ़ाइल", menu=ფაილი_菜單)
        ფაილი_菜單.add_command(label="შენახვა | 저장 | 𓉔 | שמור", command=self.𓃟_저장_도구.𓉔_파일저장_שמור)
        ფაილი_菜單.add_command(label="Выход | 離開 | ❌", command=self.root.quit)
        
        რედაქტირება_菜單 = tk.Menu(მენიუ, tearoff=0)
        მენიუ.add_cascade(label="Правка | 편집 | 𓃍 | עריכה", menu=რედაქტირება_菜單)
        რედაქტირება_菜單.add_command(label="취소 | Отменить | 𓃍 | ביטול", command=self.𓀕_역사.𓃍_실행취소_ביטול)
        რედაქტირება_菜單.add_command(label="다시 | Повторить | 𓆣 | שוב", command=self.𓀕_역사.𓆣_다시실행_שוב)

        self.공구상자 = tk.Frame(self.root, bg="#f0f0f0", pady=10)
        self.공구상자.pack(side=tk.TOP, fill=tk.X)
        
        self.палитра = ფერების_პალიტრა(self.공구상자, self.інструмент) 
        self.სრიალი = РазмерКисти(self.공구상자, self.інструмент) 
        
        self.현_모드 = "자유" 
        
        self.형상_패널 = tk.Frame(self.공구상자, bg="#f0f0f0")
        self.형상_패널.pack(side=tk.LEFT, padx=10)
        
        tk.Button(self.형상_패널, text="🖌️ Карандаш | ​붓 | 𓏟 | लेखन", command=self.선택_붓).pack(side=tk.LEFT)
        tk.Button(self.형상_패널, text="⬛ Четырёхугольник | 네​모 | 𓄹 | चतुर्भुज", command=lambda: self.선택_형상("rect")).pack(side=tk.LEFT)
        tk.Button(self.형상_패널, text="🟡 Эллипс | 타​원 | 𒀀 | दीर्घवृत्त", command=lambda: self.선택_형상("oval")).pack(side=tk.LEFT)
        tk.Button(self.형상_패널, text="➖ Линия | 직​선 | 𓐮 | रेखा", command=lambda: self.선택_형상("line")).pack(side=tk.LEFT)
        tk.Button(self.형상_패널, text="𓏞 טקסט | 문자 | 𓀚 | 글 | T", command=self.선택_글자).pack(side=tk.LEFT)
        
        self.지우개_버튼 = tk.Button(self.형상_패널, text="𓀁 საშლელი", command=self.사용_지우개)
        self.지우개_버튼.pack(side=tk.LEFT, padx=5)

        self.지우기_버튼 = tk.Button(self.형상_패널, text="מחק הכל | 𓀃 𒀀 𓃠", command=self.чисто)
        self.지우기_버튼.pack(side=tk.LEFT, padx=5)
        
        self.ტილო.pack(fill=tk.BOTH, expand=True)
        
        self.ტილო.bind("<Button-1>", self.시작_액션)
        self.ტილო.bind("<B1-Motion>", self.이동_액션)
        self.ტილო.bind("<ButtonRelease-1>", self.종료_액션)

    def 선택_붓(self):
        self.현_모드 = "자유"

    def 선택_형상(self, תבנית):
        self.현_모드 = "형상"
        self.ආକୃති_도구.प्रकार = תבנית

    def 선택_글자(self):
        self.현_모드 = "텍스트"

    def 시작_액션(self, 이벤트):
        if self.현_모드 == "자유":
            self.інструмент.x = 이벤트.x
            self.інструмент.y = 이벤트.y
        elif self.현_모드 == "형상":
            self.ආକୃති_도구.ֆერი = self.інструмент.ფერი
            self.ආକୃති_도구.גודל = self.інструмент.размер 
            self.ආକୃති_도구.𓁹_시작(이벤트)
        elif self.현_모드 == "텍스트":
            self.𓏞_텍스트_도구.ფერი = self.інструмент.ფერი
            self.𓏞_텍스트_도구.размер = self.інструмент.размер
            self.𓏞_텍스트_도구.𓁹_시작(이벤트)

    def 이동_액션(self, 이벤트):
        if self.현_모드 == "자유":
            self.інструмент.ხატვა(이벤트)
        elif self.현_모드 == "형상":
            self.ආକୃති_도구.𓃠_그리기(이벤트)

    def 종료_액션(self, 이벤트):
        if self.현_모드 == "자유":
            self.інструмент.დასრულება(이벤트)
        elif self.현_모드 == "형상":
            self.ආକୃති_도구.𓏏_종료(이벤트)

    def 사용_지우개(self):
        self.현_모드 = "자유"
        self.інструмент.ფერი = "white"

    def чисто(self):
        self.ტილო.delete("all")

    def 시작(self):
        self.root.mainloop()

