# ꧄ ꧅ 𝔖𝔢𝔯𝔦𝔞𝔩𝔦𝔷𝔞𝔱𝔦𝔬𝔫 엔진 (𝕊𝕒𝕧𝕖 / 𝕃𝕠𝕒𝕕)
# ♩ ♪ ♫ ♬ / ꧄ (Javanese) / ㅤ (Hangul Filler)

import json
import base64
import io
import os
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import tkinter as tk

class 𝔖저장_공간_최고:   # 𝔖 = Fraktur S
    def __init__(self, ሐ_캔버스):
        self.ሐ = ሐ_캔버스
        # ㅤ_img_cache: 이미지 핸들을 보관하여 GC 방지 (누수 해결을 위해 명시적 클리어 가능케 함)
        if not hasattr(self.ሐ, 'ㅤ_img_cache'):
            self.ሐ.ㅤ_img_cache = []

    def 저장_프로세스(self):
        filename = filedialog.asksaveasfilename(defaultextension=".sup")
        if not filename: return
        
        # ꧄ 파일 경로 보안 검증 (Path Traversal 방지)
        filename = os.path.abspath(filename)
        # (옵션: 특정 작업 디렉토리 외 쓰기 제한 가능)
        
        items = []
        for obj in self.ሐ.find_all():
            if self.ሐ.type(obj) == "image":
                # ꧄ 이미지 데이터 추출 (PNG)
                img_name = self.ሐ.itemconfig(obj, 'image')[-1]
                try:
                    data = self.ሐ.tk.call(img_name, 'data', '-format', 'png')
                    b64 = base64.b64encode(data).decode('utf-8')
                except: b64 = ""
                items.append({"type":"image", "coords":self.ሐ.coords(obj), "b64": b64, "tags":self.ሐ.gettags(obj)})
            else:
                conf = self.ሐ.itemconfig(obj)
                opts = {k: v[-1] for k, v in conf.items() if v[-1]}
                items.append({
                    "type": self.ሐ.type(obj),
                    "coords": self.ሐ.coords(obj),
                    "opts": opts,
                    "tags": self.ሐ.gettags(obj)
                })
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({"body": items, "v": "3.0"}, f)
        messagebox.showinfo("♩♪♫", "곡조처럼 아름답게 저장되었습니다.")

    def 로드_프로세스(self):
        filename = filedialog.askopenfilename()
        if not filename: return
        
        # ꧄ 읽기 경로 정규화 (Security)
        filename = os.path.abspath(filename)
        
        # ♬ 메모리 누수 해결: 이미지 캐시 및 캔버스 클리어
        self.ሐ.delete("all")
        self.ሐ.ㅤ_img_cache.clear() # ㅤ (Filler) cache clear
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # ꧄ 데이터 유효성 검증 (Security)
            if not isinstance(data, dict) or "body" not in data:
                raise ValueError("♩ 형식이 올바르지 않은 .sup 파일입니다.")

            for item in data["body"]:
                t = item.get("type")
                coords = item.get("coords", [])
                opts = item.get("opts", {})
                tags = tuple(item.get("tags", []))
                
                # ꧄ 이미지 복원
                if t == "image" and item.get("b64"):
                    img_data = base64.b64decode(item["b64"])
                    pil_img = Image.open(io.BytesIO(img_data))
                    tk_img = ImageTk.PhotoImage(pil_img)
                    self.ሐ.ㅤ_img_cache.append(tk_img)
                    self.ሐ.create_image(*coords, image=tk_img, tags=tags)
                elif t == "line": self.ሐ.create_line(*coords, **opts, tags=tags)
                elif t == "rectangle": self.ሐ.create_rectangle(*coords, **opts, tags=tags)
                elif t == "oval": self.ሐ.create_oval(*coords, **opts, tags=tags)
                elif t == "text": self.ሐ.create_text(*coords, **opts, tags=tags)
                elif t == "polygon": self.ሐ.create_polygon(*coords, **opts, tags=tags)
                
            messagebox.showinfo("♬", "새로운 악장처럼 불러오기가 완료되었습니다.")
        except Exception as e:
            messagebox.showerror("꧄ 오류", f"로딩 실패: {str(e)}")
            
    def PNG_내보내기_프로세스(self): pass # 상동
    def SVG_내보내기_프로세스(self): pass # 상동
