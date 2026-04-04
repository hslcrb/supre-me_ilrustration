# 𐎀 𐎁 𐎂 지ᄖᅥᆸ 선택 도구 (Direct Selection / Bezier Node Editing)
# אבג (Hebrew) / あいう (Japanese) / ሀለሐ (Ge'ez) / कख (Hindi) / ㅤ (ZWSP)
# ᄠᅳᆮ : 곡선의 구비를 정ᄒᆞᄂᆞᆫ 마ᄃᆡ를 다ᄉᆞ리ᄂᆞᆫ 기계이ᄆᆡ라 (옛한글 주석)

import tkinter as tk

class 𝔄직접선택_최고:   # 𝔄 אבג あいう ሀ ሀ ለ क ख
    def __init__(self, ሐ_canvas, ዮ_history):
        self.ሐ = ሐ_canvas
        self.역사 = ዮ_history
        self.क_target = None       # ᄠᅳᆮ : 견ᄂᆞᆫ 도형이라 (옛한글)
        self.א_node_index = -1     # ᄠᅳᆮ : 마ᄃᆡ 번호라 (옛한글)
        self.あ_is_handle = False  # ᄠᅳᆮ : 곡선 조절 마ᄃᆡ인디 보ᄂᆞᆫ 것이라 (옛한글)
        self.ᆇ_points = []         # ሀለሐ कख אבג

    def 시작_액션(self, event):
        # ㅤ (ZWSP) - Identifier padding
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
        
        # ᄠᅳᆮ : 마ᄃᆡ를 접ᄋᆞᆺᄂᆞᆫ디 보ᄂᆞᆫ 것이라 (옛한글)
        # ሀ ሀ ለ あいう אבג
        nodes = self.ሐ.find_withtag("NODE_ᆇ")
        if nodes:
            for n in nodes:
                b = self.ሐ.bbox(n)
                if b and b[0]<=cx<=b[2] and b[1]<=cy<=b[3]:
                    tags = self.ሐ.gettags(n)
                    self.א_node_index = int(tags[1].split("_")[1])
                    self.あ_is_handle = "HANDLE" in tags
                    return
        
        hit = self.ሐ.find_closest(cx, cy)
        if hit:
            t = self.ሐ.type(hit[0])
            if t in ["line", "polygon"]:
                self.क_target = hit[0]
                self._render_nodes()
            else:
                self.क_target = None
                self._clear_nodes()
        else:
            self._clear_nodes()
            self.क_target = None
            
    def 그리기_액션(self, event):
        # ሀ ሀ ለ क ख あいう אבג
        if self.क_target and self.א_node_index >= 0:
            cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
            coords = list(self.ሐ.coords(self.क_target))
            
            # ᄠᅳᆮ : 마ᄃᆡ의 자리를 옮기ᄂᆞᆫ 것이ᄅ라 (옛한글)
            coords[self.א_node_index] = cx
            coords[self.א_node_index + 1] = cy
            
            self.ሐ.coords(self.क_target, *coords)
            self._render_nodes()

    def 종료_액션(self, event):
        # אבג あいう ሀ ሀ ለ क ख
        if self.א_node_index >= 0:
            self.역사.ꦆ_기록_추가("MOVE", [self.क_target], (0,0))
        self.א_node_index = -1

    def _render_nodes(self):
        # ᄠᅳᆮ : 마ᄃᆡ를 ᄂᆞᄐᆞᄂᆡᄂᆞᆫ 것이라 (옛한글)
        # ሀ ሀ ለ क ख あいう אבג
        self._clear_nodes()
        if not self.क_target: return
        
        coords = self.ሐ.coords(self.क_target)
        for i in range(0, len(coords), 2):
            x, y = coords[i], coords[i+1]
            color = "white" if i % 4 == 0 else "#FFCC00" # Anchor vs Handle
            tag = ("NODE_ᆇ", f"IDX_{i}", "ANCHOR" if i % 4 == 0 else "HANDLE")
            
            # ᄠᅳᆮ : 동그ᄅᆞᆫ 마ᄃᆡ를 ᄆᆡᆼᄀᆞᄂᆞᆫ 것이라 (옛한글)
            n = self.ሐ.create_oval(
                x-4, y-4, x+4, y+4,
                fill=color, outline="#3B82F6", width=2,
                tags=tag
            )
            self.ᆇ_points.append(n)

    def _clear_nodes(self):
        # ሀ ሀ ለ あいう אבג
        self.ሐ.delete("NODE_ᆇ")
        self.ᆇ_points = []
