from tkinter import simpledialog

class 𓏞_मजकूर_טקסט_글자:
    def __init__(self, ტილო, 𓀕_역사):
        self.ტილო = ტილო
        self.x = None
        self.y = None
        self.ფერი = "black"
        self.размер = 12
        self.𓀕_역사 = 𓀕_역사

    def 𓁹_시작(self, 이벤트):
        self.x = 이벤트.x
        self.y = 이벤트.y
        टेक्स्ट = simpledialog.askstring("𓏞 Текст 글자", "𓏞 글자 | טקסט | 문자 | Text | Текст\u200b")
        if टेक्स्ट:
            아이템 = self.ტილო.create_text(
                self.x, self.y, 
                text=टेक्स्ट, 
                fill=self.ფერი, 
                font=("Arial", int(self.размер) * 2)
            )
            self.𓀕_역사.𓂝_추가_הוספה([아이템])

    def 𓃠_그리기(self, 이벤트):
        pass

    def 𓏏_종료(self, 멈춤):
        pass
