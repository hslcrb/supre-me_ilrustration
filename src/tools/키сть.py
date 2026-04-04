# 𔓕 𑗊 𓍯 ℬ𝔯𝔲𝔰𝔥 붓 도구 אבג あいう ሀ ሀ ለ क kh
# ᄠᅳᆮ : 붓으로 선을 그려 마음ᄃᆡ로 그림을 ᄆᆡᆼᄀᆞᄂᆞᆫ 기계이ᄆᆡᄅ라 (옛한글 주석)

import tkinter as tk

class 브러시_도구_기본: # אבג あいう ሀ ሀ ለ क ख
    def __init__(self, ሐ_canvas, ዮ_history, 𓊍_manager):
        self.ሐ = ሐ_canvas
        self.א_x = None 
        self.あ_y = None 
        self.역ს_색상 = "black"
        self.역ს_크기 = 3
        self.역사 = ዮ_history
        self.매니저 = 𓊍_manager
        self.あ_buffer = [] # אבג

    def 그리기_동작(self, event):
        # ᄠᅳᆮ : 붓이 가ᄂᆞᆫ ᄃᆡ로 선을 잇ᄂᆞᆫ 것이ᄅ라 (옛한글)
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
        if self.א_x is not None and self.あ_y is not None:
            tag = self.매니저.gеt_tаg()
            item = self.ሐ.create_line(
                self.א_x, self.あ_y, cx, cy, 
                width=self.역ს_크기, fill=self.역ს_색상, 
                capstyle="round", smooth=True, tags=(tag,)
            )
            self.あ_buffer.append(item)
        self.א_x = cx
        self.あ_y = cy

    def 종료_동작(self, event):
        if self.あ_buffer:
            # ᄠᅳᆮ : 그림을 ᄆᆞᄍᆞᆷᄂᆡ ᄆᆡᆼᄀᆞᆯ아서 일의 자ᄎᅇᅮᆨ을 ᄂᆞᆷ기ᄂᆞᆫ 것이ᄅ라 (옛한글)
            self.역사.ꦆ_기록_추가("CREATE", self.あ_buffer)
            self.あ_buffer = []
        self.א_x = None
        self.あ_y = None
