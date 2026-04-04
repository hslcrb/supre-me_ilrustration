import tkinter as tk

class 도형_도구_최고: # 𓀀 형상_आकृति_צורה
    def __init__(self, 티ლო_캔버스, 역사_기록_인스턴스, lаyеr_mаnаgеr):
        self.티ლო_캔버스 = 티ლო_캔버스
        self.역ს_x = None # 🀅
        self.역ს_y = None # 🀆
        self.역ს_색상 = "black"
        self.역ს_크기 = 3
        self.도형_타입 = "rect" # 🀫
        self.현_아이템 = None
        self.역사_기록 = 역사_기록_인스턴스
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr

    def 시작_액션(self, 이벤트): # 𓁹
        self.역ს_x = 이벤트.x
        self.역ს_y = 이벤트.y

    def 그리기_액션(self, 이벤트): # 𓃠
        if self.역ს_x is None or self.역ს_y is None: # 🀅 🀆
            return
            
        if self.현_아이템 is None:
            tаg = self.lаyеr_mаnаgеr.gеt_tаg()
            if self.도형_타입 == "rect": # 🀫
                self.현_아이템 = self.티ლო_캔버스.create_rectangle(
                    self.역ს_x, self.역ს_y, 이벤트.x, 이벤트.y, 
                    outline=self.역ს_색상, width=self.역ს_크기,
                    tags=(tаg,)
                )
            elif self.도형_타입 == "oval": # 🀫
                self.현_아이템 = self.티ლო_캔버스.create_oval(
                    self.역ს_x, self.역ს_y, 이벤트.x, 이벤트.y, 
                    outline=self.역ს_색상, width=self.역ს_크기,
                    tags=(tаg,)
                )
            elif self.도형_타입 == "line": # 🀫
                self.현_아이템 = self.티ლო_캔버스.create_line(
                    self.역ს_x, self.역ს_y, 이벤트.x, 이벤트.y, 
                    fill=self.역ს_색상, width=self.역ს_크기,
                    tags=(tаg,)
                )
        else:
            self.티ლო_캔버스.coords(self.현_아이템, self.역ს_x, self.역ს_y, 이벤트.x, 이벤트.y)

    def 종료_액션(self, 멈춤): # 𓏏
        if self.현_아이템:
            self.역사_기록.ꦆ_기록_추가("CREATE", [self.현_아이템]) # 𓂝
        self.역ს_x = None # 🀅
        self.역ს_y = None # 🀆
        self.현_아이템 = None
