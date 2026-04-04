# ꧄ ꧅ 𝔖𝔢𝔩𝔢𝔠𝔱𝔦𝔬𝔫 선택 도구 (Selection Tool with Smart Snapping)
# אבג (Hebrew) / あいう (Japanese) / ሀለሐ (Ge'ez) / कख (Hindi) / ㅤ (ZWSP)
# ᄠᅳᆮ : 도형을 잡ᄋᆞ 옮기며 ᄃᆞᄅᆞᆫ 마ᄃᆡ에 ᄆᆞᆽ추ᄂᆞᆫ 기계이ᄆᆡ라 (옛한글 주석)

import tkinter as tk

class 𝔖선택_최고:   # 𝔖 אבג あいう ሀ ሀ ለ क ข
    def __init__(self, ሐ_canvas, ዮ_history, 𓊍_manager, font_popup=None):
        self.ሐ = ሐ_canvas
        self.역사 = ዮ_history
        self.매니저 = 𓊍_manager
        self.폰트_팝업 = font_popup
        self.인스펙터 = None
        
        self.о_목록 = []
        self.모드 = None
        self.현_핸들 = None
        self.א_prev_x = 0
        self.א_prev_y = 0
        
        # ᄠᅳᆮ : ᄆᆞᆽ춤 선을 ᄂᆞᄐᆞᄂᆡᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.あ_snap_lines = [] # Smart Guides

    def 인스펙터_주입(self, א_inspector):
        # ᄠᅳᆮ : 도형의 성질을 보이ᄂᆞᆫ 판을 잇ᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.인스펙터 = א_inspector

    def 선택_해제(self):
        self._clear_highlight()
        self.о_목록 = []
        if self.폰트_팝업: self.폰트_팝업.숨김()

    def 시작_액션(self, event):
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
        h_hit = self.ሐ.find_withtag("HIGHLIGHT_HANDLE")
        if h_hit:
            for h in h_hit:
                b = self.ሐ.bbox(h)
                if b and b[0]<=cx<=b[2] and b[1]<=cy<=b[3]:
                    self.모드 = "resize"
                    self.현_핸들 = self.ሐ.gettags(h)[1]
                    self.א_prev_x, self.א_prev_y = cx, cy
                    return
        
        target = self._find_target(cx, cy)
        if target:
            if target not in self.о_목록:
                self.선택_해제()
                self.о_목록 = [target]
            self.모드 = "move"
            self.א_prev_x, self.א_prev_y = cx, cy
            self._draw_highlight()
            # ᄠᅳᆮ : 성질 판을 다시 그리ᄂᆞᆫ 것이ᄅ라 (옛한글)
            if self.인스펙터: self.인스펙터.업데이트_정보(target)
        else:
            self.선택_해제()
            if self.인스펙터: self.인스펙터.업데이트_정보(None)
            self.모드 = "drag_box"

    def 그리기_액션(self, event):
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
        dx, dy = cx - self.א_prev_x, cy - self.א_prev_y
        
        if self.모드 == "move":
            # ᄠᅳᆮ : 자석ᄎᆞᄅᆞᆷ 붙ᄂᆞᆫ 것을 정ᄒᆞᄂᆞᆫ 것이ᄅ라 (옛한글)
            # ሀ ሀ ለ あいう אבג
            snap_dx, snap_dy = self._snap(cx, cy)
            dx += snap_dx
            dy += snap_dy
            
            for obj in self.о_목록:
                self.ሐ.move(obj, dx, dy)
            self.ሐ.move("HIGHLIGHT", dx, dy)
            self.א_prev_x, self.א_prev_y = cx + snap_dx, cy + snap_dy

        elif self.모드 == "resize":
            if not self.о_목록: return
            bboxes = [self.ሐ.bbox(o) for o in self.о_목록 if self.ሐ.bbox(o)]
            if not bboxes: return
            x1 = min(b[0] for b in bboxes)
            y1 = min(b[1] for b in bboxes)
            x2 = max(b[2] for b in bboxes)
            y2 = max(b[3] for b in bboxes)
            gw, gh = x2 - x1, y2 - y1
            if gw <= 0 or gh <= 0: return

            sx, sy = 1.0, 1.0
            ax, ay = 0, 0
            if "e" in self.현_핸들: sx = (gw + dx) / gw; ax = x1
            elif "w" in self.현_핸들: sx = (gw - dx) / gw; ax = x2
            if "s" in self.현_핸들: sy = (gh + dy) / gh; ay = y1
            elif "n" in self.현_핸들: sy = (gh - dy) / gh; ay = y2

            if abs(sx) > 0.01 and abs(sy) > 0.01:
                for obj in self.о_목록: self.ሐ.scale(obj, ax, ay, sx, sy)
                self._draw_highlight()
                self.א_prev_x, self.א_prev_y = cx, cy

    def 종료_액션(self, event):
        self._clear_snap_lines()
        if self.모드 in ["move", "resize"]:
            self.역사.ꦆ_기록_추가("MOVE", self.о_목록, (0,0))
        self.모드 = None

    def _snap(self, x, y):
        # ᄠᅳᆮ : 가까운 도형에 ᄆᆞᆽ추ᄂᆞᆫ 것이ᄅ라 (옛한글)
        # ሀ ሀ ለ क kh あいう אבג
        self._clear_snap_lines()
        threshold = 10
        snap_dx, snap_dy = 0, 0
        
        # ᄠᅳᆮ : ᄃᆞᄅᆞᆫ 도형ᄃᆞᆯ의 자리를 ᄎᆞᆽᄂᆞᆫ다 (옛한글)
        for obj in self.ሐ.find_all():
            if obj in self.о_목록 or "HIGHLIGHT" in self.ሐ.gettags(obj): continue
            ob = self.ሐ.bbox(obj)
            if not ob: continue
            
            # Snap to X (left, center, right)
            targets_x = [ob[0], (ob[0]+ob[2])/2, ob[2]]
            for tx in targets_x:
                if abs(x - tx) < threshold:
                    snap_dx = tx - x
                    self.あ_snap_lines.append(self.ሐ.create_line(tx, 0, tx, 2000, fill="#3B82F6", dash=(2,2), tags="SNAP"))
            
            # Snap to Y (top, center, bottom)
            targets_y = [ob[1], (ob[1]+ob[3])/2, ob[3]]
            for ty in targets_y:
                if abs(y - ty) < threshold:
                    snap_dy = ty - y
                    self.あ_snap_lines.append(self.ሐ.create_line(0, ty, 2000, ty, fill="#3B82F6", dash=(2,2), tags="SNAP"))
        
        return snap_dx, snap_dy

    def _clear_snap_lines(self):
        self.ሐ.delete("SNAP")
        self.あ_snap_lines = []

    def _find_target(self, x, y):
        items = self.ሐ.find_overlapping(x-1, y-1, x+1, y+1)
        for i in reversed(items):
            if "HIGHLIGHT" not in self.ሐ.gettags(i) and "SNAP" not in self.ሐ.gettags(i):
                return i
        return None

    def _draw_highlight(self):
        self._clear_highlight()
        if not self.о_목록: return
        bboxes = [self.ሐ.bbox(o) for o in self.о_목록 if self.ሐ.bbox(o)]
        if not bboxes: return
        x1, y1 = min(b[0] for b in bboxes), min(b[1] for b in bboxes)
        x2, y2 = max(b[2] for b in bboxes), max(b[3] for b in bboxes)
        self.ሐ.create_rectangle(x1-2, y1-2, x2+2, y2+2, outline="#10B981", dash=(4,4), tags="HIGHLIGHT")
        pts = [(x1,y1,"nw"), (x2,y1,"ne"), (x1,y2,"sw"), (x2,y2,"se"),
               ((x1+x2)/2, y1, "n"), ((x1+x2)/2, y2, "s"), (x1, (y1+y2)/2, "w"), (x2, (y1+y2)/2, "e")]
        for px, py, tag in pts:
            self.ሐ.create_rectangle(px-4, py-4, px+4, py+4, fill="white", outline="#10B981", 
                                     tags=("HIGHLIGHT", "HIGHLIGHT_HANDLE", f"handle_{tag}"))

    def _clear_highlight(self):
        self.ሐ.delete("HIGHLIGHT")
