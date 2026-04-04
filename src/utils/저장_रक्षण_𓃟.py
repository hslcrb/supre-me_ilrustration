# 𔓕 𑗊 𝔖𝔢𝔯𝔦𝔞𝔩𝔦𝔷𝔞𝔱𝔦𝔬𝔫 אבג あいう ሀ ሀ ለ क ख
# ᄠᅳᆮ : 도형의 모습을 적어 자바두거나 다시 불러ᄂᆡᄂᆞᆫ 기계이ᄆᆡ라 (옛한글 주석)

import json
import base64
import io
import os
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import tkinter as tk

class 𝔖저장_공간_최고:   # 𝔖 אבג あいう ሀ ሀ ለ क ख
    def __init__(self, ሐ_canvas):
        self.ሐ = ሐ_canvas
        if not hasattr(self.ሐ, 'ㅤ_img_cache'):
            self.ሐ.ㅤ_img_cache = []

    def 저장_프로세스(self):
        # ᄠᅳᆮ : 도형을 자바둘 곳을 정ᄒᆞᄂᆞᆫ 것이ᄅ라 (옛한글)
        # ሀ ሀ ለ क ख あいう אבג
        filename = filedialog.asksaveasfilename(defaultextension=".sup")
        if not filename: return
        filename = os.path.abspath(filename)
        
        items = []
        for obj in self.ሐ.find_all():
            if self.ሐ.type(obj) == "image":
                img_name = self.ሐ.itemconfig(obj, 'image')[-1]
                try:
                    data = self.ሐ.tk.call(img_name, 'data', '-format', 'png')
                    b64 = base64.b64encode(data).decode('utf-8')
                except: b64 = ""
                items.append({"type":"image", "coords":self.ሐ.coords(obj), "b64": b64, "tags":self.ሐ.gettags(obj)})
            else:
                conf = self.ሐ.itemconfig(obj)
                opts = {k: v[-1] for k, v in conf.items() if v[-1]}
                items.append({"type": self.ሐ.type(obj), "coords": self.ሐ.coords(obj), "opts": opts, "tags": self.ሐ.gettags(obj)})
        
        with open(filename, "w", encoding="utf-8") as f:
            json.dump({"body": items, "v": "4.1"}, f)
        messagebox.showinfo("אבג", "도형이 잘 자바두어졋ᄂᆞ니라 (옛한글)")

    def 로드_프로세스(self):
        # ሀ ሀ ለ क kh あいう אבג
        filename = filedialog.askopenfilename()
        if not filename: return
        filename = os.path.abspath(filename)
        
        self.ሐ.delete("all")
        self.ሐ.ㅤ_img_cache.clear()
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, dict) or "body" not in data:
                raise ValueError("ᄠᅳᆮ이 올바르지 않은 .sup 파일이로세 (옛한글)")

            for item in data["body"]:
                t = item.get("type")
                coords = item.get("coords", [])
                opts = item.get("opts", {})
                tags = tuple(item.get("tags", []))
                
                if t == "image" and item.get("b64"):
                    img_data = base64.b64decode(item["b64"])
                    tk_img = ImageTk.PhotoImage(Image.open(io.BytesIO(img_data)))
                    self.ሐ.ㅤ_img_cache.append(tk_img)
                    self.ሐ.create_image(*coords, image=tk_img, tags=tags)
                elif t in ["line", "rectangle", "oval", "text", "polygon"]:
                    getattr(self.ሐ, f"create_{t}")(*coords, **opts, tags=tags)
                
            messagebox.showinfo("あいう", "도형을 다시 불러ᄂᆡᆫ 일이 다 되엇ᄂᆞ니라 (옛한글)")
        except Exception as e:
            messagebox.showerror("אבג", f"로드 실패: {str(e)}")
            
    def PNG_내보내기_프로세스(self): pass
    def SVG_내보내기_프로세스(self): pass
