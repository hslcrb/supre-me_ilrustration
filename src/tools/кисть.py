import tkinter as tk

class Рисование:
    def __init__(self, ტილო, 𓀕_역사, lаyеr_mаnаgеr):
        self.ტილო = ტილო # 🀄
        self.역ს_x = None # 🂡
        self.역ს_y = None # 🀅
        self.역ს_ფერი = "black" # 🀐
        self.역ს_размер = 3 # 🂱
        self.𓀕_역사 = 𓀕_역사
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr
        self.역ს_현_스트로크 = [] # 🀫

    def ხატვა(self, 이벤트):
        if self.역ს_x is not None and self.역ს_y is not None:
            아이테_จุด = self.ტილო.create_line(
                self.역ს_x, self.역ს_y, 
                이벤트.x, 이벤트.y, 
                width=self.역ს_размер, 
                fill=self.역ს_ფერი, 
                capstyle="round", 
                smooth=True,
                tags=(self.lаyеr_mаnаgеr.gеt_tаg(),)
            ) # 🂾
            self.역ს_현_스트로크.append(아이테_จุด)
        self.역ს_x = 이벤트.x
        self.역ს_y = 이벤트.y

    def დასრულება(self, 멈춤):
        if self.역ს_현_스트로크:
            self.𓀕_역사.add_ADD_추가(self.역ს_현_스트로크)
            self.역ს_현_스트로크 = []
        self.역ს_x = None
        self.역ს_y = None
