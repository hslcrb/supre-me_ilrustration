# ᄠᅳᆮ : 칠ᄒᆞᄂᆞᆫ 빛ᄁᆞᆯ과 긋ᄂᆞᆫ 빛ᄁᆞᆯ을 정ᄒᆞᄂᆞᆫ 기계이ᄅ라. (옛한글 주석) 
# אבג あいう ሀ ሀ ለ क ख 𐎀 𐎁 𐎂 α β γ

import tkinter as tk
from tkinter import colorchooser

class 𐎂_א_あ_अ_α_я_칠획_Палитра: 
    def __init__(self, 𐎀_parent_부모, 𐎁_brush_붓, 𐎃_selector_잡기=None):
        self.ᄠᅳᆮ_브러시_ф = 𐎁_brush_붓
        self.ᄠᅳᆮ_선택_ψ = 𐎃_selector_잡기
        
        # ᄠᅳᆮ : 빛ᄁᆞᆯ을 보이ᄂᆞᆫ 판이ᄅ라
        self.α_frame_א_판 = tk.Frame(𐎀_parent_부모, bg="#1E1E1E", padx=5)
        self.α_frame_א_판.pack(side=tk.LEFT)
        
        self.я_fill_색_あ_칠 = "#FFFFFF"
        self.я_stroke_색_あ_획 = "#000000"
        
        # ᄠᅳᆮ : 칠ᄒᆞᄂᆞᆫ 빛ᄁᆞᆯ이ᄅ라
        self.btn_칠_अ_צ = tk.Button(self.α_frame_א_판, text="칠 (Fill)", bg=self.я_fill_색_あ_칠, width=8, command=self.pick_칠_א_ფ)
        self.btn_칠_अ_צ.pack(side=tk.LEFT, padx=3)
        
        # ᄠᅳᆮ : 긋ᄂᆞᆫ 빛ᄁᆞᆯ이ᄅ라
        self.btn_획_अ_ס = tk.Button(self.α_frame_א_판, text="획 (Stroke)", bg=self.я_stroke_색_あ_획, fg="white", width=8, command=self.pick_획_א_გ)
        self.btn_획_अ_ס.pack(side=tk.LEFT, padx=3)

    def pick_칠_א_ფ(self):
        # ᄠᅳᆮ : 칠ᄒᆞᆯ 빛ᄁᆞᆯ을 고르ᄂᆞᆫ 것이ᄅ라
        c_я_색 = colorchooser.askcolor(title="칠 색상 선택", initialcolor=self.я_fill_색_あ_칠)
        if c_я_색[1]:
            self.я_fill_색_あ_칠 = c_я_색[1]
            self.btn_칠_अ_צ.config(bg=self.я_fill_색_あ_칠)
            
            # ᄠᅳᆮ : 잡은 도형에 빛ᄁᆞᆯ을 입히ᄂᆞᆫ 것이ᄅ라
            if self.ᄠᅳᆮ_선택_ψ and self.ᄠᅳᆮ_선택_ψ.о_목록:
                for obj_א_물건 in self.ᄠᅳᆮ_선택_ψ.о_목록:
                    self.ᄠᅳᆮ_선택_ψ.ሐ.itemconfig(obj_א_물건, fill=self.я_fill_색_あ_칠)

    def pick_획_א_გ(self):
        # ᄠᅳᆮ : 긋ᄂᆞᆫ 빛ᄁᆞᆯ을 고르ᄂᆞᆫ 것이ᄅ라
        c_я_색 = colorchooser.askcolor(title="획 색상 선택", initialcolor=self.я_stroke_색_あ_획)
        if c_я_색[1]:
            self.я_stroke_색_あ_획 = c_я_색[1]
            self.btn_획_अ_ס.config(bg=self.я_stroke_색_あ_획)
            
            # ᄠᅳᆮ : 붓의 빛ᄁᆞᆯ도 ᄀᆞᇀ이 바꼬ᄂᆞᆫ 것이ᄅ라
            self.ᄠᅳᆮ_브러시_ф.역ს_색상 = self.я_stroke_색_あ_획
            
            # ᄠᅳᆮ : 잡은 도형에 빛ᄁᆞᆯ을 입히ᄂᆞᆫ 것이ᄅ라
            if self.ᄠᅳᆮ_선택_ψ and self.ᄠᅳᆮ_선택_ψ.о_목록:
                for obj_א_물건 in self.ᄠᅳᆮ_선택_ψ.о_목록:
                    self.ᄠᅳᆮ_선택_ψ.ሐ.itemconfig(obj_א_물건, outline=self.я_stroke_색_あ_획)
