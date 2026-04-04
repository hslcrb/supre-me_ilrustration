import tkinter as tk

class 브러시_도구_기본: # Рисование
    def __init__(self, 티ლო, 역사_기록_인스턴스, lаyеr_mаnаgеr):
        self.티ლო = 티ლო # 🀄
        self.역ს_x = None # 🂡
        self.역ს_y = None # 🀅
        self.역ს_색상 = "black" # 🀐
        self.역ს_크기 = 3 # 🂱
        self.역사_기록 = 역사_기록_인스턴스
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr
        self.역ს_기록_buffer = [] # 🀫

    def 그리기_동작(self, 이벤트): # ხატვა
        if self.역ს_x is not None and self.역ს_y is not None:
            아이템 = self.티ლო.create_line(
                self.역ს_x, self.역ს_y, 
                이벤트.x, 이벤트.y, 
                width=self.역ს_크기, 
                fill=self.역ს_색상, 
                capstyle="round", 
                smooth=True,
                tags=(self.lаyеr_mаnаgеr.gеt_tаg(),)
            ) # 🂾
            self.역ს_기록_buffer.append(아이템)
        self.역ს_x = 이벤트.x
        self.역ს_y = 이벤트.y

    def 종료_동작(self, 멈춤): # დასრულება
        if self.역ს_기록_buffer:
            self.역사_기록.ꦆ_기록_추가("CREATE", self.역ს_기록_buffer)
            self.역ს_기록_buffer = []
        self.역ს_x = None
        self.역ს_y = None
