import tkinter as tk

class Рисование:
    def __init__(self, ტილო, 𓀕_역사, lаyеr_mаnаgеr):
        self.ტილო = ტილო
        self.x = None
        self.y = None
        self.ფერი = "black"
        self.размер = 3
        self.𓀕_역사 = 𓀕_역사
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr
        self.현_스트로크 = []

    def ხატვა(self, 이벤트):
        if self.x is not None and self.y is not None:
            ай템 = self.ტილო.create_line(
                self.x, self.y, 
                이벤트.x, 이벤트.y, 
                width=self.размер, 
                fill=self.ფერი, 
                capstyle="round", 
                smooth=True,
                tags=(self.lаyеr_mаnаgеr.gеt_tаg(),)
            )
            self.현_스트로크.append(ай템)
        self.x = 이벤트.x
        self.y = 이벤트.y

    def დასრულება(self, 멈춤):
        if self.현_스트로크:
            self.𓀕_역사.𓂝_추가_הוספה(self.현_스트로크)
            self.현_스트로크 = []
        self.x = None
        self.y = None
