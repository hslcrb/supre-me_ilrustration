# 𔓕 𑗊 𝔓 𝔔 ℜ 특성 패널 אבג あいう ሀ ሀ ለ क ख
# ᄠᅳᆮ : 도형의 모습과 ᄉᆡᆨᄀᆞᆯ을 정ᄒᆞᄂᆞᆫ 기계이ᄆᆡᄅ라 (옛한글 주석)

import tkinter as tk
from tkinter import colorchooser

_SIDE_BG = "#16213E"
_TEXT_FG = "#94A3B8"
_VAL_FG  = "#E0E0E0"
_ACCENT  = "#1D4ED8"

class 𝔓특성_UI_최고: # אבג あいう ሀ ሀ ለ क kh
    def __init__(self, 부모, ሐ_canvas, ዮ_history):
        self.부모 = 부모
        self.ሐ = ሐ_canvas
        self.역사 = ዮ_history
        
        # ᄠᅳᆮ : 가ᄋᆡ 판을 ᄆᆡᆼᄀᆞᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.프레임 = tk.Frame(부모, bg=_SIDE_BG, width=280, padx=15, pady=20)
        self.프레임.pack(side=tk.RIGHT, fill=tk.Y)
        self.프레임.pack_propagate(False)

        tk.Label(self.프레임, text="𝔓 𝓘𝓝𝓢𝓟𝓔𝓒𝓣𝓞𝓡 א", bg=_SIDE_BG, fg="#3B82F6", 
                 font=("Fraktur", 12, "bold")).pack(pady=(0, 20), anchor="w")

        # א 𝓖𝓔𝓞𝓜𝓔𝓣𝓡𝓨 あ
        self._add_section("א 𝓖𝓔𝓞𝓜𝓔𝓣𝓡𝓨 あ")
        self.x_var = self._add_field("X א:", "0")
        self.y_var = self._add_field("Y あ:", "0")
        self.w_var = self._add_field("W ሀ:", "0")
        self.h_var = self._add_field("H क:", "0")

        # क 𝓢𝓣𝓨𝓛𝓔 ሀ
        self._add_section("क 𝓢𝓣𝓨𝓛𝓔 ሀ")
        self.color_btn = tk.Button(self.프레임, text="🎨 채우기 色 א", bg=_ACCENT, fg="white", 
                                   relief=tk.FLAT, command=self._pick_color)
        self.color_btn.pack(fill=tk.X, pady=5)
        
        self.stroke_btn = tk.Button(self.프레임, text="📏 테두리 色 あ", bg="#374151", fg="white", 
                                    relief=tk.FLAT, command=self._pick_stroke)
        self.stroke_btn.pack(fill=tk.X, pady=5)

        self.현_타겟 = None

    def _add_section(self, txt):
        tk.Label(self.프레임, text=txt, bg=_SIDE_BG, fg="#64748B", 
                 font=("Fraktur", 9, "bold")).pack(pady=(15, 5), anchor="w")

    def _add_field(self, lbl, dflt):
        f = tk.Frame(self.프레임, bg=_SIDE_BG)
        f.pack(fill=tk.X, pady=2)
        tk.Label(f, text=lbl, bg=_SIDE_BG, fg=_TEXT_FG, font=("Arial", 8)).pack(side=tk.LEFT)
        v = tk.StringVar(value=dflt)
        e = tk.Entry(f, textvariable=v, bg="#0F172A", fg=_VAL_FG, insertbackground="white",
                     relief=tk.FLAT, width=12, font=("Consolas", 9))
        e.pack(side=tk.RIGHT)
        return v

    def 업데이트_정보(self, target_id):
        self.현_타겟 = target_id
        if not target_id: return
        bbox = self.ሐ.bbox(target_id)
        if bbox:
            self.x_var.set(round(bbox[0], 1))
            self.y_var.set(round(bbox[1], 1))
            self.w_var.set(round(bbox[2]-bbox[0], 1))
            self.h_var.set(round(bbox[3]-bbox[1], 1))
        
        opts = self.ሐ.itemconfig(target_id)
        if 'fill' in opts:
            col = opts['fill'][-1]
            if col: self.color_btn.config(bg=col)

    def _pick_color(self):
        if not self.현_타겟: return
        c = colorchooser.askcolor(title=" א부강 א")
        if c[1]:
            self.ሐ.itemconfig(self.현_타겟, fill=c[1])
            self.color_btn.config(bg=c[1])
            self.역사.ꦆ_기록_추가("ATTR", [self.현_타겟])

    def _pick_stroke(self):
        if not self.현_타겟: return
        c = colorchooser.askcolor(title=" ああ あ")
        if c[1]:
            self.ሐ.itemconfig(self.현_타겟, outline=c[1])
            self.역사.ꦆ_기록_추가("ATTR", [self.현_타겟])
