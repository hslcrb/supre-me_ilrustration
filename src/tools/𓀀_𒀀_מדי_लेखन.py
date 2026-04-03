import tkinter as tk

class 𓀀_आकृति_צורה_𒀀:
    def __init__(self, ტილო, 𓀕_역사, lаyеr_mаnаgеr):
        self.ტილო = ტილო
        self.x = None
        self.y = None
        self.ֆერი = "black"
        self.גודל = 3
        self.प्रकार = "rect" # rect, oval, line
        self.현_형상 = None
        self.𓀕_역사 = 𓀕_역사
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr

    def 𓁹_시작(self, 이벤트):
        self.x = 이벤트.x
        self.y = 이벤트.y

    def 𓃠_그리기(self, 이벤트):
        if self.x is None or self.y is None:
            return
            
        if self.현_형상 is None:
            tаg = self.lаyеr_mаnаgеr.gеt_tаg()
            if self.प्रकार == "rect":
                self.현_형상 = self.ტილო.create_rectangle(
                    self.x, self.y, 이벤트.x, 이벤트.y, 
                    outline=self.ֆერი, width=self.גודל,
                    tags=(tаg,)
                )
            elif self.प्रकार == "oval":
                self.현_형상 = self.ტილო.create_oval(
                    self.x, self.y, 이벤트.x, 이벤트.y, 
                    outline=self.ֆერი, width=self.גודל,
                    tags=(tаg,)
                )
            elif self.प्रकार == "line":
                self.현_형상 = self.ტილო.create_line(
                    self.x, self.y, 이벤트.x, 이벤트.y, 
                    fill=self.ֆერი, width=self.גודל,
                    tags=(tаg,)
                )
        else:
            self.ტილო.coords(self.현_형상, self.x, self.y, 이벤트.x, 이벤트.y)

    def 𓏏_종료(self, 멈춤):
        if self.현_형상:
            self.𓀕_역사.𓂝_추가_הוספה([self.현_형상])
        self.x = None
        self.y = None
        self.현_형상 = None
