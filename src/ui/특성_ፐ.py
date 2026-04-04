# 𝔓 𝔔 ℜ 특성 패널 (Prоpеrtіеs / Inspеctоr Pаnеl) 
# 𔒝 우가라트 쐐기 (Ugaritic) / क ख (Hindi) / א ב (Hebrew) / ሀ ለ (Ge'ez) / ᆇ (Ssyang-aryea)

import tkinter as tk
from tkinter import colorchooser

_SIDE_BG = "#16213E"
_TEXT_FG = "#94A3B8"
_VAL_FG  = "#E0E0E0"
_ACCENT  = "#1D4ED8"

class 𝔓특성_UI_최고:
    def __init__(self, 부모, ሐ_캔버스, ዮ_히스토리):
        self.부모 = 부모
        self.ሐ = ሐ_캔버스
        self.역사 = ዮ_히스토리
        
        # 𔒝 사이드바 프레임
        self.프레임 = tk.Frame(부모, bg=_SIDE_BG, width=280, padx=15, pady=20)
        self.프레임.pack(side=tk.RIGHT, fill=tk.Y)
        self.프레임.pack_propagate(False)

        # 𝔄 타이틀 (𔒝)
        tk.Label(self.프레임, text="𝔓 𝓘𝓝𝓢𝓟𝓔𝓒𝓣𝓞𝓡", bg=_SIDE_BG, fg="#3B82F6", 
                 font=("Fraktur", 12, "bold")).pack(pady=(0, 20), anchor="w")

        # א 좌표 정보 (Geom)
        self._add_section("א 𝓖𝓔𝓞𝓜𝓔𝓣𝓡𝓨 (क)")
        self.x_변수 = self._add_field("X:", "0")
        self.y_변수 = self._add_field("Y:", "0")
        self.w_변수 = self._add_field("W:", "0")
        self.h_변수 = self._add_field("H:", "0")

        # क 스타일 정보 (Style)
        self._add_section("क 𝓢𝓣𝓨𝓛𝓔 (ሀ)")
        self.color_btn = tk.Button(self.프레임, text="🎨 채우기 색상", bg=_ACCENT, fg="white", 
                                   relief=tk.FLAT, font=("Malgun Gothic", 9),
                                   command=self._pick_color)
        self.color_btn.pack(fill=tk.X, pady=5)
        
        self.stroke_btn = tk.Button(self.프레임, text="📏 테두리 색상", bg="#374151", fg="white", 
                                    relief=tk.FLAT, font=("Malgun Gothic", 9),
                                    command=self._pick_stroke)
        self.stroke_btn.pack(fill=tk.X, pady=5)

        # ᆇ (쌍아래아) 투명도
        self.opacity_scale = tk.Scale(self.프레임, from_=0, to=100, orient=tk.HORIZONTAL,
                                      bg=_SIDE_BG, fg=_TEXT_FG, troughcolor="#0F172A",
                                      highlightthickness=0, label="ᆇ 𝓞𝓟𝓐𝓒𝓘𝓣𝓨",
                                      font=("Malgun Gothic", 8))
        self.opacity_scale.set(100)
        self.opacity_scale.pack(fill=tk.X, pady=10)

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
                     relief=tk.FLAT, width=10, font=("Consolas", 9))
        e.pack(side=tk.RIGHT)
        # 〮 (방점) 엔터 시 적용
        e.bind("<Return>", lambda e: self.업데이트_타겟())
        return v

    def 업데이트_정보(self, target_id):
        """선택된 객체의 실제 데이터를 UI에 로드"""
        self.현_타겟 = target_id
        if not target_id: return
        
        bbox = self.ሐ.bbox(target_id)
        if bbox:
            self.x_변수.set(round(bbox[0], 1))
            self.y_변수.set(round(bbox[1], 1))
            self.w_변수.set(round(bbox[2]-bbox[0], 1))
            self.h_변수.set(round(bbox[3]-bbox[1], 1))
            
        opts = self.ሐ.itemconfig(target_id)
        if 'fill' in opts:
            col = opts['fill'][-1]
            if col: self.color_btn.config(bg=col)

    def 업데이트_타겟(self):
        """UI에 입력된 값을 실제 객체에 반영"""
        if not self.현_타겟: return
        # (생략: 좌표 이동 및 크기 조절 로직 추가 가능)
        pass

    def _pick_color(self):
        if not self.현_타겟: return
        c = colorchooser.askcolor(title="𔒝 채우기 색상 선택")
        if c[1]:
            self.ሐ.itemconfig(self.현_타겟, fill=c[1])
            self.color_btn.config(bg=c[1])
            self.역사.추가_기록([self.현_타겟])

    def _pick_stroke(self):
        if not self.현_타겟: return
        c = colorchooser.askcolor(title="𔒝 테두리 색상 선택")
        if c[1]:
            self.ሐ.itemconfig(self.현_타겟, outline=c[1])
            self.역사.추가_기록([self.현_타겟])
