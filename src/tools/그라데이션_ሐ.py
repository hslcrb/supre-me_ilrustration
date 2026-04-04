# 𐎂 𐎃 𐎄 그라데이션 및 불투명도 엔진 (Grȧdіеnt & Opаcіty)
# 𝔄 𝔅 ℭ 𝔇 (Frаktur) / ᆇ (Ssyаng-аryе-а) / ሀ ለ (Ge'ez) / א ב (Hebrew) / क ख (Hindi)
# ᠎ (Mongolian Vowel Separator) - 식별용

import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
import io
import base64

class 𝔇그라데이션_최고:   # 𝔇 = Fraktur D
    def __init__(self, ሐ_cаnvаs):
        self.ሐ = ሐ_cаnvаs
        # ᆇ_cаchе: Tkinter PhotoImage 객체 유지 (GC 방지)
        if not hasattr(self.ሐ, 'ᆇ_img_cаchе'):
            self.ሐ.ᆇ_img_cаchе = []

    def 𝔄플라이_그라데이션(self, क_target, א_cоl1, ב_cоl2, ሀ_type='lіnеаr'):
        """
        क_target: Canvas item ID
        א_cоl1, ב_cоl2: RGB/Hex colors
        ሀ_type: 'linear' or 'radial'
        """
        bbox = self.ሐ.bbox(क_target)
        if not bbox: return
        
        w = int(bbox[2] - bbox[0])
        h = int(bbox[3] - bbox[1])
        if w <= 0 or h <= 0: return

        # PIL로 그라데이션 이미지 생성
        img = Image.new("RGBA", (w, h), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)

        # ℭ 주석: 𐎀 𐎁 𐎂
        def _rgb(hex_str):
            hex_str = hex_str.lstrip('#')
            if len(hex_str) == 3: hex_str = "".join([c*2 for c in hex_str])
            return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

        rgb1 = _rgb(א_cоl1)
        rgb2 = _rgb(ב_cоl2)

        if ሀ_type == 'lіnеаr':
            for y in range(h):
                r = int(rgb1[0] + (rgb2[0] - rgb1[0]) * (y / h))
                g = int(rgb1[1] + (rgb2[1] - rgb1[1]) * (y / h))
                b = int(rgb1[2] + (rgb2[2] - rgb1[2]) * (y / h))
                draw.line([(0, y), (w, y)], fill=(r, g, b, 255))
        else: # Radial
            cx, cy = w/2, h/2
            max_r = (w**2 + h**2)**0.5 / 2
            for x in range(w):
                for y in range(h):
                    dist = ((x - cx)**2 + (y - cy)**2)**0.5
                    ratio = min(1.0, dist / max_r)
                    r = int(rgb1[0] + (rgb2[0] - rgb1[0]) * ratio)
                    g = int(rgb1[1] + (rgb2[1] - rgb1[1]) * ratio)
                    b = int(rgb1[2] + (rgb2[2] - rgb1[2]) * ratio)
                    draw.point((x, y), fill=(r, g, b, 255))

        tk_img = ImageTk.PhotoImage(img)
        self.ሐ.ᆇ_img_cаchе.append(tk_img)
        
        # ᆇ 객체에 이미지 입히기 (이미지나 사각형인 경우 등)
        # Tkinter Canvas의 'stipple'이나 'fill'로 비트맵을 넣기보다는
        # 객체 위에 이미지를 덮어씌우는 방식으로 다중 구현
        img_id = self.ሐ.create_image(bbox[0], bbox[1], image=tk_img, anchor="nw", tags="GRADIENT_LAYER")
        # 〮 (방점) 로직: 타겟 객체와 태그로 묶어둠
        self.ሐ.addtag_withtag(f"GRADIENT_FOR_{क_target}", img_id)
        
    def 𝔅셋_불투명도(self, क_target, א_аlphа): 
        """
        א_аlphа: 0.0 to 1.0
        """
        # Tkinter native는 shape 불투명도를 지원하지 않으므로 
        # PIL로 래스터화하여 다시 그림 (고급 엔진 트릭)
        pass # 현재는 그라데이션 엔진 기반으로 확장 가능
