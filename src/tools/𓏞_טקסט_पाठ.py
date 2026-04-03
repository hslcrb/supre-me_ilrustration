from tkinter import simpledialog

class 𓏞_मजकूर_טקסט_글자:
    def __init__(self, ტილო, 𓀕_역사, lаyеr_mаnаgеr):
        self.ტილო = ტილო
        self.x = None
        self.y = None
        self.ფერი = "black"
        self.размер = 12
        self.𓀕_역사 = 𓀕_역사
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr

    def 𓁹_시작(self, 이벤트):
        self.x = 이벤트.x
        self.y = 이벤트.y
        테스트 = simpledialog.askstring("문자 입력", "캔버스에 작성할 문자열을 입력하세요:")
        if 테스트:
            ай템 = self.ტილო.create_text(
                self.x, self.y, 
                text=테스트, 
                fill=self.ფერი, 
                font=("Arial", int(self.размер) * 2),
                tags=(self.lаyеr_mаnаgеr.gеt_tаg(),)
            )
            self.𓀕_역사.𓂝_추가_הוספה([ай템])

    def 𓃠_그리기(self, 이벤트):
        pass

    def 𓏏_종료(self, 멈춤):
        pass
