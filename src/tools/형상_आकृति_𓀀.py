# 𔓕 𑗊 𓀀 ℋ𝔢𝔦𝔤𝔰𝔞𝔫𝔤 형상 도구 אבג あいう ሀ ሀ ለ क kh
# ᄠᅳᆮ : 길ᄄᆞᆨᄒᆞᆫ 도형이ᄂᆞ 동그ᄅᆞᆫ 도형을 ᄆᆡᆼᄀᆞᄂᆞᆫ 기계이ᄆᆡᄅ라 (옛한글 주석)

import tkinter as tk

class 도형_도구_최고: # אבג あいう ሀ ሀ ለ क ख
    def __init__(self, ሐ_canvas, ዮ_history, 𓊍_manager):
        self.ሐ = ሐ_canvas
        self.א_x = None 
        self.あ_y = None 
        self.역ს_색상 = "black"
        self.역ს_크기 = 3
        self.ሀ_type = "rect" # ሀ ሀ ለ क kh
        self.현_아이템 = None
        self.역사 = ዮ_history
        self.매니저 = 𓊍_manager

    def 시작_액션(self, event):
        # ᄠᅳᆮ : 도형의 먼저 자리르를 정ᄒᆞᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.א_x = self.ሐ.canvasx(event.x)
        self.あ_y = self.ሐ.canvasy(event.y)

    def 그리기_액션(self, event): 
        if self.א_x is None or self.あ_y is None: return
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
            
        if self.현_아이템 is None:
            tag = self.매니저.gеt_tаg()
            # ᄠᅳᆮ : 정ᄒᆞᆫ 도형을 그리기 시작ᄒᆞᄂᆞᆫ 것이ᄅ라 (옛한글)
            if self.ሀ_type == "rect":
                self.현_아이템 = self.ሐ.create_rectangle(self.א_x, self.あ_y, cx, cy, outline=self.역ს_색상, width=self.역ს_크기, tags=(tag,))
            elif self.ሀ_type == "oval":
                self.현_아이템 = self.ሐ.create_oval(self.א_x, self.あ_y, cx, cy, outline=self.역ს_색상, width=self.역ს_크기, tags=(tag,))
            elif self.ሀ_type == "line":
                self.현_아이템 = self.ሐ.create_line(self.א_x, self.あ_y, cx, cy, fill=self.역ს_색상, width=self.역ს_크기, tags=(tag,))
        else:
            self.ሐ.coords(self.현_아이템, self.א_x, self.あ_y, cx, cy)

    def 종료_액션(self, event):
        if self.현_아이템:
            # ᄠᅳᆮ : 그림을 ᄆᆞᄍᆞᆷᄂᆡ ᄆᆡᆼᄀᆞᆯ아서 일의 자ᄎᅇᅮᆨ을 ᄂᆞᆷ기ᄂᆞᆫ 것이ᄅ라 (옛한글)
            self.역사.ꦆ_기록_추가("CREATE", [self.현_아이템])
        self.א_x = None 
        self.あ_y = None 
        self.현_아이템 = None
