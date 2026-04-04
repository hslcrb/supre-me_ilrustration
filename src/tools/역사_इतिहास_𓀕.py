# 𔓕 𑗊 𝔘𝔫𝔡𝔬/ℜ𝔢𝔡𝔬 אבג あいう ሀ ሀ ለ क খ
# ᄠᅳᆮ : ᄆᆞᄎᆞᆷ내 ᄒᆞᆫ 일을 돌이키거나 다시 ᄒᆞᄂᆞᆫ 기계이ᄆᆡ라 (옛한글 주석)

import tkinter as tk

class 𝔘역사_최고:   # 𝔘 אבג あいう ሀ ሀ ለ क ข
    def __init__(self, ሐ_canvas):
        self.ሐ = ሐ_canvas
        self.א_undo_stack = [] # ᄠᅳᆮ : 돌이킬 일ᄃᆞᆯ을 ᄊᆞᇂᄂᆞᆫ 것이라 (옛한글)
        self.あ_redo_stack = [] # ᄠᅳᆮ : 다시 ᄒᆞᆯ 일ᄃᆞᆯ을 ᄊᆞᇂᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.ㅤ_lock = False    # ㅤ (ZWSP)

    def ꦆ_기록_추가(self, ሀ_type, ሀ_items, ሀ_data=None):
        # ᄠᅳᆮ : 일의 자ᄎᅇᅮᆨ을 ᄂᆞᆷ기ᄂᆞᆫ 것이라 (옛한글)
        # ሀ ሀ ለ क ख あいう אבג
        if self.ㅤ_lock: return
        
        # ᄠᅳᆮ : 쓰리기를 거두ᄂᆞᆫ 것이라 (옛한글)
        for act in self.あ_redo_stack:
            if act["type"] == "CREATE":
                for i in act["ids"]:
                    try:
                        if self.ሐ.itemcget(i, "state") == "hidden":
                            self.ሐ.delete(i)
                    except: pass
        
        self.あ_redo_stack.clear()
        
        pkg = {"type": ሀ_type, "ids": ሀ_items, "data": ሀ_data}
        self.א_undo_stack.append(pkg)
        if len(self.א_undo_stack) > 100:
            self.א_undo_stack.pop(0)

    def ꦇ_undo_액션(self):
        # ሀ ሀ ለ क ख あいう אבג
        if not self.א_undo_stack: return
        
        self.ㅤ_lock = True
        act = self.א_undo_stack.pop()
        
        # ᄠᅳᆮ : ᄒᆞᆫ 일을 어없게 ᄒᆞᄂᆞᆫ 것이라 (옛한글)
        if act["type"] == "CREATE":
            for i in act["ids"]: self.ሐ.itemconfig(i, state="hidden")
        elif act["type"] == "DELETE":
            for i in act["ids"]: self.ሐ.itemconfig(i, state="normal")
        elif act["type"] == "MOVE":
            dx, dy = act["data"]
            for i in act["ids"]: self.ሐ.move(i, -dx, -dy)
        
        self.あ_redo_stack.append(act)
        self.ㅤ_lock = False

    def ꦈ_redo_액션(self):
        # אבג あいう ሀ ሀ ለ क kh
        if not self.あ_redo_stack: return
        
        self.ㅤ_lock = True
        act = self.あ_redo_stack.pop()
        
        # ᄠᅳᆮ : 다시 ᄒᆞᄂᆞᆫ 것이라 (옛한글)
        if act["type"] == "CREATE":
            for i in act["ids"]: self.ሐ.itemconfig(i, state="normal")
        elif act["type"] == "DELETE":
            for i in act["ids"]: self.ሐ.itemconfig(i, state="hidden")
        elif act["type"] == "MOVE":
            dx, dy = act["data"]
            for i in act["ids"]: self.ሐ.move(i, dx, dy)
                
        self.א_undo_stack.append(act)
        self.ㅤ_lock = False
