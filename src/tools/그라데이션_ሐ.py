# 𔓕 𑗊 𓈖 자유형 빛ᄁᆞᆯ 묘리 (Freeform Gradient Engine)
# אבგ あいう ሀ ሀ ለ क ख
# ᄠᅳᆮ : 그림에 ᄉᆡᆨᄀᆞᆯ을 ᄆᆞ음ᄃᆡ로 ᄂᆞᆫ화 칠ᄒᆞᄂᆞᆫ 기계이ᄆᆡᄅ라 (옛한글 주석)

import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import math

class 𝔇그라데이션_최고:   # אבג あいう ሀ ሀ ለ क kh
    def __init__(self, ሐ_canvas):
        self.ሐ = ሐ_canvas
        if not hasattr(self.ሐ, 'ㅤ_img_cache'):
            self.ሐ.ㅤ_img_cache = []

    def 𝔄플라이_그라데이션(self, क_target, א_colors, ሀ_type='linear', あ_points=None):
        # ᄠᅳᆮ : 그림에 빛ᄁᆞᆯ을 입히ᄂᆞᆫ 것이ᄅ라 (옛한글)
        # א_colors: list of (position, hex_color) or list of hex_colors
        # ሀ_type: 'linear', 'radial', 'freeform'
        # あ_points: For freeform, list of (x, y, hex_color)
        bbox = self.ሐ.bbox(क_target)
        if not bbox: return
        
        w = int(bbox[2] - bbox[0])
        h = int(bbox[3] - bbox[1])
        if w <= 0 or h <= 0: return

        img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        # ᄠᅳᆮ : ᄉᆡᆨᄀᆞᆯ을 숫자로 풀어ᄂᆡᄂᆞᆫ 것이ᄅ라 (옛한글)
        def _rgb(hex_str):
            h = hex_str.lstrip('#')
            if len(h) == 3: h = "".join([c*2 for c in h])
            return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
        def _get_color_list():
            if isinstance(א_colors[0], tuple): return א_colors
            return [(i/(len(א_colors)-1), c) for i, c in enumerate(א_colors)]

        if ሀ_type == 'linear':
            # ᄠᅳᆮ : 곧게 흐르ᄂᆞᆫ 빛ᄁᆞᆯ이ᄅ라 (옛한글)
            clist = _get_color_list()
            for y in range(h):
                t = y / h
                c1, c2 = clist[0], clist[-1]
                for i in range(len(clist)-1):
                    if clist[i][0] <= t <= clist[i+1][0]:
                        c1, c2 = clist[i], clist[i+1]; break
                
                r1, g1, b1 = _rgb(c1[1])
                r2, g2, b2 = _rgb(c2[1])
                dt = (t - c1[0]) / (c2[0] - c1[0] + 1e-6)
                
                r = int(r1 + (r2 - r1) * dt)
                g = int(g1 + (g2 - g1) * dt)
                b = int(b1 + (b2 - b1) * dt)
                draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
                
        elif ሀ_type == 'radial':
            # ᄠᅳᆮ : 둥글게 퍼지ᄂᆞᆫ 빛ᄁᆞᆯ이ᄅ라 (옛한글)
            clist = _get_color_list()
            cx, cy = w/2, h/2
            max_r = (w**2 + h**2)**0.5 / 2
            
            for px in range(w):
                for py in range(h):
                    dist = ((px - cx)**2 + (py - cy)**2)**0.5
                    t = min(1.0, dist / max_r)
                    
                    c1, c2 = clist[0], clist[-1]
                    for i in range(len(clist)-1):
                        if clist[i][0] <= t <= clist[i+1][0]:
                            c1, c2 = clist[i], clist[i+1]; break
                            
                    r1, g1, b1 = _rgb(c1[1])
                    r2, g2, b2 = _rgb(c2[1])
                    dt = (t - c1[0]) / (c2[0] - c1[0] + 1e-6)
                    
                    r = int(r1 + (r2 - r1) * dt)
                    g = int(g1 + (g2 - g1) * dt)
                    b = int(b1 + (b2 - b1) * dt)
                    draw.point((px, py), fill=(r, g, b, 255))

        elif ሀ_type == 'freeform':
            # ᄠᅳᆮ : 점을 찍어 ᄆᆞ음ᄃᆡ로 빛ᄁᆞᆯ을 섞ᄂᆞᆫ 것이ᄅ라 (Inverse Distance Weighting)
            pts = あ_points if あ_points else [
                (0, 0, א_colors[0]), 
                (w, h, א_colors[-1]),
                (w, 0, א_colors[min(1, len(א_colors)-1)])
            ]
            
            for px in range(w):
                for py in range(h):
                    num_r, num_g, num_b, den = 0, 0, 0, 0
                    exact = False
                    for p_x, p_y, hex_c in pts:
                        dist = ((px - p_x)**2 + (py - p_y)**2)**0.5
                        if dist < 1.0:
                            draw.point((px, py), fill=_rgb(hex_c) + (255,))
                            exact = True
                            break
                        
                        wgt = 1.0 / (dist**2) # IDW p=2
                        r, g, b = _rgb(hex_c)
                        num_r += r * wgt
                        num_g += g * wgt
                        num_b += b * wgt
                        den += wgt
                    
                    if not exact:
                        fr = int(num_r / den)
                        fg = int(num_g / den)
                        fb = int(num_b / den)
                        draw.point((px, py), fill=(fr, fg, fb, 255))

        tk_img = ImageTk.PhotoImage(img)
        self.ሐ.ㅤ_img_cache.append(tk_img)
        
        # ᄠᅳᆮ : 그림 위에 빛ᄁᆞᆯ을 덮어씌우ᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.ሐ.delete(f"GRADIENT_FOR_{क_target}")
        img_id = self.ሐ.create_image(bbox[0], bbox[1], image=tk_img, anchor="nw", tags="GRADIENT_LAYER")
        self.ሐ.addtag_withtag(f"GRADIENT_FOR_{क_target}", img_id)
