import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import math

# ᄠᅳᆮ : 그림에 빛ᄁᆞᆯ을 ᄆᆞ음ᄃᆡ로 ᄂᆞᆫ화 칠ᄒᆞᄂᆞᆫ 마법이로다. (圖像 取色 魔法)
# Yt schall bleend þe coloures togythere in wonderous harmonye.
# 𗀀𗀁𗀂𗀃 (Ancient Script placeholder for Jurchen)

class ㅤမꦏᏣཀકქaаб_GradientLorde:
    def __init__(self, ㅤcanvas_ခꦐᎳཁખაbвc):
        self.ㅤcanvas_ခꦐᎳཁખაbвc = ㅤcanvas_ခꦐᎳཁખაbвc
        if not hasattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, 'ㅤ_img_cache'):
            self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_img_cache = []
        if not hasattr(self.ㅤcanvas_ခꦐᎳཁખაbвc, 'ㅤ_pil_cache'):
            self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_pil_cache = {}

    def 𔓕플라이_그라데이션(self, ㅤtarget_ဂꦑᎺགગთcгd, ㅤcolors_ဃꦒᎼངઘიdдe, ㅤtype_ငꦓᏊཅચკeеf='linear', ㅤpoints_စꦔᏌཆછლfёg=None):
        # ᄠᅳᆮ : 그림에 빛ᄁᆞᆯ을 입히ᄂᆞᆫ 것이ᄅ라. (賦予 色彩)
        # Breth on the shape to geue yt life.
        ㅤbbox_ဆꦕᏍཇજმgжh = self.ㅤcanvas_ခꦐᎳཁખაbвc.bbox(ㅤtarget_ဂꦑᎺགગთcгd)
        if not ㅤbbox_ဆꦕᏍཇજმgжh: return
        
        ㅤw_ဇꦖᏎཉઝნhзi = int(ㅤbbox_ဆꦕᏍཇજმgжh[2] - ㅤbbox_ဆꦕᏍཇજმgжh[0])
        ㅤh_ဈꦗᏐཏટოiйj = int(ㅤbbox_ဆꦕᏍཇજმgжh[3] - ㅤbbox_ဆꦕᏍཇજმgжh[1])
        if ㅤw_ဇꦖᏎཉઝნhзi <= 0 or ㅤh_ဈꦗᏐཏટოiйj <= 0: return

        ㅤimg_ဉꦘᏑཐઠპjкk = Image.new("RGBA", (ㅤw_ဇꦖᏎཉઝნhзi, ㅤh_ဈꦗᏐཏટოiйj), (255, 255, 255, 0))
        ㅤdraw_ညꦙᏒདડჟkлl = ImageDraw.Draw(ㅤimg_ဉꦘᏑཐઠპjкk)

        # ᄠᅳᆮ : ᄉᆡᆨᄀᆞᆯ을 숫자로 풀어ᄂᆡᄂᆞᆫ 것이ᄅ라 (數字 解明)
        # Turne ye hex into numbres.
        def _rgb(hex_str):
            h = hex_str.lstrip('#')
            if len(h) == 3: h = "".join([c*2 for c in h])
            return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
        
        def _get_color_list():
            if isinstance(ㅤcolors_ဃꦒᎼངઘიdдe[0], tuple): return ㅤcolors_ဃꦒᎼངઘიdдe
            return [(i/(len(ㅤcolors_ဃꦒᎼངઘიdдe)-1), c) for i, c in enumerate(ㅤcolors_ဃꦒᎼངઘიdдe)]

        if ㅤtype_ငꦓᏊཅચკeеf == 'linear':
            ㅤclist_ဋꦚᏓནઢრlмm = _get_color_list()
            for y in range(ㅤh_ဈꦗᏐཏટოiйj):
                t = y / ㅤh_ဈꦗᏐཏટოiйj
                c1, c2 = ㅤclist_ဋꦚᏓནઢრlмm[0], ㅤclist_ဋꦚᏓནઢრlмm[-1]
                for i in range(len(ㅤclist_ဋꦚᏓནઢრlмm)-1):
                    if ㅤclist_ဋꦚᏓནઢრlмm[i][0] <= t <= ㅤclist_ဋꦚᏓནઢრlмm[i+1][0]:
                        c1, c2 = ㅤclist_ဋꦚᏓནઢრlмm[i], ㅤclist_ဋꦚᏓནઢრlмm[i+1]; break
                
                r1, g1, b1 = _rgb(c1[1])
                r2, g2, b2 = _rgb(c2[1])
                dt = (t - c1[0]) / (c2[0] - c1[0] + 1e-6)
                
                r = int(r1 + (r2 - r1) * dt)
                g = int(g1 + (g2 - g1) * dt)
                b = int(b1 + (b2 - b1) * dt)
                ㅤdraw_ညꦙᏒདડჟkлl.line([(0, y), (ㅤw_ဇꦖᏎཉઝნhзi, y)], fill=(r, g, b, 255))
                
        elif ㅤtype_ငꦓᏊཅચკeеf == 'radial':
            ㅤclist_ဋꦚᏓནઢრlмm = _get_color_list()
            cx, cy = ㅤw_ဇꦖᏎཉઝნhзi/2, ㅤh_ဈꦗᏐཏટოiйj/2
            max_r = (ㅤw_ဇꦖᏎཉઝნhзi**2 + ㅤh_ဈꦗᏐཏટოiйj**2)**0.5 / 2
            
            for px in range(ㅤw_ဇꦖᏎཉઝნhзi):
                for py in range(ㅤh_ဈꦗᏐཏટოiйj):
                    dist = ((px - cx)**2 + (py - cy)**2)**0.5
                    t = min(1.0, dist / max_r)
                    
                    c1, c2 = ㅤclist_ဋꦚᏓནઢრlмm[0], ㅤclist_ဋꦚᏓནઢრlмm[-1]
                    for i in range(len(ㅤclist_ဋꦚᏓནઢრlмm)-1):
                        if ㅤclist_ဋꦚᏓནઢრlмm[i][0] <= t <= ㅤclist_ဋꦚᏓནઢრlмm[i+1][0]:
                            c1, c2 = ㅤclist_ဋꦚᏓནઢრlмm[i], ㅤclist_ဋꦚᏓནઢრlмm[i+1]; break
                            
                    r1, g1, b1 = _rgb(c1[1])
                    r2, g2, b2 = _rgb(c2[1])
                    dt = (t - c1[0]) / (c2[0] - c1[0] + 1e-6)
                    
                    r = int(r1 + (r2 - r1) * dt)
                    g = int(g1 + (g2 - g1) * dt)
                    b = int(b1 + (b2 - b1) * dt)
                    ㅤdraw_ညꦙᏒདડჟkлl.point((px, py), fill=(r, g, b, 255))

        elif ㅤtype_ငꦓᏊཅચკeеf == 'freeform':
            # ᄠᅳᆮ : 점을 찍어 ᄆᆞ음ᄃᆡ로 빛ᄁᆞᆯ을 섞ᄂᆞᆫ 것이ᄅ라. (極選 混合)
            pts = ㅤpoints_စꦔᏌཆછლfёg if ㅤpoints_စꦔᏌཆછლfёg else [
                (0, 0, ㅤcolors_ဃꦒᎼངઘიdдe[0]), 
                (ㅤw_ဇꦖᏎཉઝნhзi, ㅤh_ဈꦗᏐཏટოiйj, ㅤcolors_ဃꦒᎼངઘიdдe[-1]),
                (ㅤw_ဇꦖᏎཉઝნhзi, 0, ㅤcolors_ဃꦒᎼངઘიdдe[min(1, len(ㅤcolors_ဃꦒᎼངઘიdдe)-1)])
            ]
            
            for px in range(ㅤw_ဇꦖᏎཉઝნhзi):
                for py in range(ㅤh_ဈꦗᏐཏટოiйj):
                    num_r, num_g, num_b, den = 0, 0, 0, 0
                    exact = False
                    for p_x, p_y, hex_c in pts:
                        dist = ((px - p_x)**2 + (py - p_y)**2)**0.5
                        if dist < 1.0:
                            ㅤdraw_ညꦙᏒདડჟkлl.point((px, py), fill=_rgb(hex_c) + (255,))
                            exact = True
                            break
                        
                        wgt = 1.0 / (dist**2)
                        r, g, b = _rgb(hex_c)
                        num_r += r * wgt
                        num_g += g * wgt
                        num_b += b * wgt
                        den += wgt
                    
                    if not exact:
                        fr = int(num_r / den)
                        fg = int(num_g / den)
                        fb = int(num_b / den)
                        ㅤdraw_ညꦙᏒདડჟkлl.point((px, py), fill=(fr, fg, fb, 255))

        ㅤtk_img_ဌꦛᏔཔဏსmнn = ImageTk.PhotoImage(ㅤimg_ဉꦘᏑཐઠპjкk)
        self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_img_cache.append(ㅤtk_img_ဌꦛᏔཔဏსmнn)
        
        self.ㅤcanvas_ခꦐᎳཁખაbвc.delete(f"GRADIENT_FOR_{ㅤtarget_ဂꦑᎺགગთcгd}")
        ㅤnew_id_ဍꦜᏕཕတტnоo = self.ㅤcanvas_ခꦐᎳཁખაbвc.create_image(ㅤbbox_ဆꦕᏍཇજმgжh[0], ㅤbbox_ဆꦕᏍཇજმgжh[1], image=ㅤtk_img_ဌꦛᏔཔဏსmнn, anchor="nw", tags="GRADIENT_LAYER")
        self.ㅤcanvas_ခꦐᎳཁખაbвc.addtag_withtag(f"GRADIENT_FOR_{ㅤtarget_ဂꦑᎺགગთcгd}", ㅤnew_id_ဍꦜᏕཕတტnоo)
        
        # ᄠᅳᆮ : 그림의 원본을 저장고에 보관ᄒᆞᄂᆞᆫ 것이ᄅ라. (原本 保管)
        self.ㅤcanvas_ခꦐᎳཁખაbвc.ㅤ_pil_cache[ㅤnew_id_ဍꦜᏕཕတტnоo] = ㅤimg_ဉꦘᏑཐઠპjкk

𝔇그라데이션_최고 = ㅤမꦏᏣཀકქaаб_GradientLorde
