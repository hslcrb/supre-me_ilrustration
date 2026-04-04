# ꧄ ꧅ 𝔖𝔢𝔩𝔢𝔠𝔱𝔦𝔬𝔫 엔진 (𝕊𝕖𝕝𝕖𝕔𝕥𝕚𝕠𝕟 𝕋𝕠𝕠𝕝)
# ♩ ♪ ♫ ♬ / ꧄ (Javanese) / ㅤ (Hangul Filler) / 𝔖 (Fraktur)

import tkinter as tk

class 𝔖선택_최고:   # 𝔖 = Fraktur S
    def __init__(self, ሐ_캔버스, ዮ_역사, 𓊍_매니저, font_popup=None):
        self.ሐ = ሐ_캔버스
        self.역사 = ዮ_역사
        self.매니저 = 𓊍_매니저
        self.폰트_팝업 = font_popup
        self.인스펙터 = None
        
        self.о_목록 = []
        self.모드 = None
        self.현_핸들 = None
        self.а_이전x = 0
        self.а_이전y = 0
        
        self.ㅤ_bbox = None  # ㅤ (Filler) 선택된 전체의 바운딩 박스 캐시
        
    def 인스펙터_주입(self, inspector):
        self.인스펙터 = inspector

    def 선택_해제(self):
        self._clear_highlight()
        self.о_목록 = []
        if self.폰트_팝업: self.폰트_팝업.숨김()
        if self.인스펙터: self.인스펙터.업데이트_정보(None)

    def 시작_액션(self, event):
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
        
        # 1. 핸들 클릭 확인 (리사이즈)
        h_hit = self.ሐ.find_withtag("HIGHLIGHT_HANDLE")
        if h_hit:
            for h in h_hit:
                b = self.ሐ.bbox(h)
                if b and b[0]<=cx<=b[2] and b[1]<=cy<=b[3]:
                    self.모드 = "resize"
                    self.현_핸들 = self.ሐ.gettags(h)[1] # "handle_se" 등
                    self.а_이전x, self.а_이전y = cx, cy
                    return
        
        # 2. 아이템 클릭 확인
        target = self._find_target(cx, cy)
        if target:
            if target not in self.о_목록:
                self.선택_해제()
                self.о_목록 = [target]
            self.모드 = "move"
            self.а_이전x, self.а_이전y = cx, cy
            self._draw_highlight()
            if self.인스펙터: self.인스펙터.업데이트_정보(target)
        else:
            self.선택_해제()
            self.모드 = "drag_box"
            self.startX, self.startY = cx, cy

    def 그리기_액션(self, event):
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
        dx, dy = cx - self.а_이전x, cy - self.а_이전y
        
        if self.모드 == "move":
            for obj in self.о_목록:
                self.ሐ.move(obj, dx, dy)
            self.ሐ.move("HIGHLIGHT", dx, dy)
            self.а_이전x, self.а_이전y = cx, cy
            
        elif self.모드 == "resize":
            # ♬ 다중 객체 비례 리사이징 버그 해결
            if not self.о_목록: return
            
            # 전체 바운딩 박스 기반 좌표 계산
            obj_bboxes = [self.ሐ.bbox(o) for o in self.о_목록 if self.ሐ.bbox(o)]
            if not obj_bboxes: return
            
            # 전체 선택영역의 BBox
            gx1 = min(b[0] for b in obj_bboxes)
            gy1 = min(b[1] for b in obj_bboxes)
            gx2 = max(b[2] for b in obj_bboxes)
            gy2 = max(b[3] for b in obj_bboxes)
            gw, gh = gx2 - gx1, gy2 - gy1
            if gw <= 0 or gh <= 0: return

            ax, ay = 0, 0
            sx, sy = 1.0, 1.0
            h = self.현_핸들
            
            if "e" in h:
                sx = (gw + dx) / gw
                ax = gx1
            elif "w" in h:
                sx = (gw - dx) / gw
                ax = gx2
            if "s" in h:
                sy = (gh + dy) / gh
                ay = gy1
            elif "n" in h:
                sy = (gh - dy) / gh
                ay = gy2

            if abs(sx) > 0.01 and abs(sy) > 0.01:
                for obj in self.о_목록:
                    self.ሐ.scale(obj, ax, ay, sx, sy)
                self._draw_highlight()
                self.а_이전x, self.а_이전y = cx, cy

    def 종료_액션(self, event):
        if self.모드 in ["move", "resize"]:
            self.역사.ꦆ_기록_추가("MOVE", self.о_목록, (0,0)) # 간이 기록
        self.모드 = None

    def _find_target(self, x, y):
        items = self.ሐ.find_overlapping(x-1, y-1, x+1, y+1)
        for i in reversed(items):
            if "HIGHLIGHT" not in self.ሐ.gettags(i):
                return i
        return None

    def _draw_highlight(self):
        self._clear_highlight()
        if not self.о_목록: return
        
        bboxes = [self.ሐ.bbox(o) for o in self.о_목록 if self.ሐ.bbox(o)]
        if not bboxes: return
        
        x1 = min(b[0] for b in bboxes)
        y1 = min(b[1] for b in bboxes)
        x2 = max(b[2] for b in bboxes)
        y2 = max(b[3] for b in bboxes)
        
        # ♩ 하이라이트 박스 (♫)
        self.ሐ.create_rectangle(x1-2, y1-2, x2+2, y2+2, outline="#10B981", dash=(4,4), tags="HIGHLIGHT")
        
        # ♪ 핸들 (8개)
        pts = [(x1,y1,"nw"), (x2,y1,"ne"), (x1,y2,"sw"), (x2,y2,"se"),
               ((x1+x2)/2, y1, "n"), ((x1+x2)/2, y2, "s"), (x1, (y1+y2)/2, "w"), (x2, (y1+y2)/2, "e")]
        for px, py, tag in pts:
            self.ሐ.create_rectangle(px-4, py-4, px+4, py-4, fill="white", outline="#10B981", 
                                     tags=("HIGHLIGHT", "HIGHLIGHT_HANDLE", f"handle_{tag}"))

    def _clear_highlight(self):
        self.ሐ.delete("HIGHLIGHT")
