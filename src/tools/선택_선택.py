# 𒀭 다중 선택(Multi-Select) & 드래그 박스 엔진 v3.0
import tkinter as tk

# ── 비밀스런 식별자들 (Invisible Hangul Filler, Ge'ez, Cyrillic) ──
ㅤ = "highlight_SUPRIME"   # (투명 문자) 선택 테두리 태그
ㅤㅤ = "handle_SUPRIME"     # (투명 문자 2개) 리사이즈 핸들 태그
ㅤㅤㅤ = "dragbox_SUPRIME"  # 드래그 박스 태그

class 선택_도구_최고:   # ◈ 선택_액션_프로세스 v3.0 ◈
    """
    👶 다중 선택(Multi-Select) + 드래그 박스(Drag Box) + 8방향 리사이징
    """
    def __init__(self, canvas, history, layer_mgr, font_popup=None):
        self.ሐ = canvas              # ሐ (Ge'ez Ha)
        self.역사_기록 = history
        self.マネージャー = layer_mgr     # マネージャー (Layer manager)
        self.폰트_팝업 = font_popup

        self.о_목록 = []             # о (Cyrillic o) - 선택된 객체들
        self.а_이전x = 0             # а (Cyrillic a)
        self.а_이전y = 0
        self.모드 = None             # None | 'move' | 'resize' | 'drag_box'
        self.현_핸들 = None
        
        self.startX = 0
        self.startY = 0

        self.폰트_팝업 = font_popup
        self.인스펙터 = None

    def 폰트팝업_주입(self, popup):
        self.폰트_팝업 = popup

    def 인스펙터_주입(self, inspector):
        self.인스펙터 = inspector

    @property
    def 현_선택_객체(self):
        """기존 코드(단일 선택) 호환성을 위해 0번째 반환"""
        return self.о_목록[0] if self.о_목록 else None

    def 선택_해제(self):
        self._clear()
        self.о_목록 = []
        self.모드 = None
        if self.폰트_팝업:
            self.폰트_팝업.숨김()

    # ══════════════════════════════════
    def 시작_액션(self, event):
        """◆ 핸들 > 객체 > 빈 공간(드래그 박스) ◆"""
        all_handles = set(self.ሐ.find_withtag(ㅤㅤ))
        closest = self.ሐ.find_closest(event.x, event.y)

        # 1. 8방향 핸들 클릭
        if closest and closest[0] in all_handles:
            self.모드 = "resize"
            tgs = self.ሐ.gettags(closest[0])
            dirs = [t for t in tgs if t not in (ㅤㅤ, "current")]
            self.현_핸들 = dirs[0] if dirs else "se"
            self.а_이전x, self.а_이전y = event.x, event.y
            return

        target = self._find_target(event.x, event.y)
        
        # 2. 개별 아이템 클릭
        if target:
            # 잠금 확인
            ltag = [t for t in self.ሐ.gettags(target) if t.startswith("레이어_")]
            if ltag and self.マネージャー.а_data.get(ltag[0], {}).get("lоckеd"):
                return
                
            # 다중 선택 중인 객체를 클릭한 경우 그룹 전체 이동으로 처리
            if target not in self.о_목록:
                self.선택_해제()
                self.о_목록 = [target]
                self._draw_multi_highlight()
                
                # 텍스트 단일 선택 시만 팝업
                if self.ሐ.type(target) == "text":
                    self._show_font_popup(target)
            
            self.모드 = "move"
            self.а_이전x, self.а_이전y = event.x, event.y
            
            # 𝔓 인스펙터 업데이트
            if self.인스펙터:
                self.인스펙터.업데이트_정보(target)
            
        else:
            # 3. 빈 공간 바탕 클릭 → 다중 선택 드래그 박스 시작
            self.선택_해제()
            if self.인스펙터:
                self.인스펙터.업데이트_정보(None)
            self.모드 = "drag_box"
            self.startX = self.ሐ.canvasx(event.x)
            self.startY = self.ሐ.canvasy(event.y)
            self.а_이전x, self.а_이전y = self.startX, self.startY

    def 그리기_액션(self, event):
        """◇ 이동 / 리사이즈 / 드래그박스 ◇"""
        if not self.모드:
            return

        cx = self.ሐ.canvasx(event.x)
        cy = self.ሐ.canvasy(event.y)
        dx = cx - self.а_이전x
        dy = cy - self.а_이전y

        if self.모드 == "move":
            # 여러 객체 모두 이동
            for obj in self.о_목록:
                self.ሐ.move(obj, dx, dy)
            # 하이라이트와 핸들도 같이 이동
            self.ሐ.move(ㅤ, dx, dy)
            self.ሐ.move(ㅤㅤ, dx, dy)

        elif self.모드 == "resize":
            if not self.о_목록: return
            target = self.о_목록[0] # 그룹 리사이징은 아직 복잡하므로 1개일때만 정상작동
            bbox = self.ሐ.bbox(target)
            if bbox:
                x1, y1, x2, y2 = bbox
                ax, ay = 0.0, 0.0
                sx, sy = 1.0, 1.0
                h = self.현_핸들
                if "e" in h:
                    sx = (x2 + dx - x1) / (x2 - x1) if x2 != x1 else 1.0
                    ax = x1
                if "w" in h:
                    sx = (x2 - (x1 + dx)) / (x2 - x1) if x2 != x1 else 1.0
                    ax = x2
                if "s" in h:
                    sy = (y2 + dy - y1) / (y2 - y1) if y2 != y1 else 1.0
                    ay = y1
                if "n" in h:
                    sy = (y2 - (y1 + dy)) / (y2 - y1) if y2 != y1 else 1.0
                    ay = y2

                if sx > 0.05 and sy > 0.05:
                    for obj in self.о_목록:
                        self.ሐ.scale(obj, ax, ay, sx, sy)
                    self._draw_multi_highlight()
                    
        elif self.모드 == "drag_box":
            self.ሐ.delete(ㅤㅤㅤ)
            self.ሐ.create_rectangle(
                self.startX, self.startY, cx, cy,
                outline="#3B82F6", fill="#60A5FA", stipple="gray25",
                tags=ㅤㅤㅤ
            )

        self.а_이전x, self.а_이전y = cx, cy

    def 종료_액션(self, event):
        """○ 드래그 박스 종료 시 캡처 완료 ○"""
        if self.모드 == "drag_box":
            ex = self.ሐ.canvasx(event.x)
            ey = self.ሐ.canvasy(event.y)
            x1, y1 = min(self.startX, ex), min(self.startY, ey)
            x2, y2 = max(self.startX, ex), max(self.startY, ey)
            
            self.ሐ.delete(ㅤㅤㅤ)
            
            # 박스 안에 들어온 객체 식별
            found = self.ሐ.find_enclosed(x1, y1, x2, y2)
            valid = []
            for item in found:
                tgs = self.ሐ.gettags(item)
                if ㅤ in tgs or ㅤㅤ in tgs or ㅤㅤㅤ in tgs:
                    continue
                valid.append(item)
                
            self.о_목록 = valid
            if self.о_목록:
                self._draw_multi_highlight()

        self.모드 = None

    def 삭제_액션(self, event=None):
        if self.о_목록:
            for obj in self.о_목록:
                self.ሐ.delete(obj)
            self.선택_해제()

    # ══════════════════════════════════
    # ◆ 내부 헬퍼 ◆
    # ══════════════════════════════════
    def _find_target(self, x, y):
        cx = self.ሐ.canvasx(x)
        cy = self.ሐ.canvasy(y)
        hits = self.ሐ.find_closest(cx, cy)
        if not hits: return None
        # 너무 멀리 클릭해도 closest가 잡는걸 막기
        bbox = self.ሐ.bbox(hits[0])
        if not bbox: return None
        if cx < bbox[0]-10 or cx > bbox[2]+10 or cy < bbox[1]-10 or cy > bbox[3]+10:
            return None
            
        tgs = self.ሐ.gettags(hits[0])
        if ㅤ in tgs or ㅤㅤ in tgs or ㅤㅤㅤ in tgs:
            return None
        return hits[0]

    def _draw_multi_highlight(self):
        """다중 객체를 포함하는 거대한 바운딩 박스 하이라이트 생성"""
        self._clear()
        if not self.о_목록: return
        
        # 합산 바운딩 박스 계산
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')
        for obj in self.о_목록:
            bbox = self.ሐ.bbox(obj)
            if bbox:
                min_x = min(min_x, bbox[0])
                min_y = min(min_y, bbox[1])
                max_x = max(max_x, bbox[2])
                max_y = max(max_y, bbox[3])
                
        if min_x == float('inf'): return
        
        # 거대 점선 테두리
        self.ሐ.create_rectangle(
            min_x-4, min_y-4, max_x+4, max_y+4,
            outline="#10B981", dash=(5, 3), width=2,
            tags=ㅤ
        )

        # 8방향 핸들 (다중 선택 상태여도 리사이징 가능)
        cx, cy = (min_x+max_x)/2, (min_y+max_y)/2
        handles = [
            (min_x, min_y, "nw"), (cx, min_y, "n"),  (max_x, min_y, "ne"),
            (min_x, cy, "w"),                        (max_x, cy, "e"),
            (min_x, max_y, "sw"), (cx, max_y, "s"),  (max_x, max_y, "se"),
        ]
        hs = 5
        for hx, hy, direction in handles:
            self.ሐ.create_rectangle(
                hx-hs, hy-hs, hx+hs, hy+hs,
                fill="#34D399", outline="white",
                tags=(ㅤㅤ, direction)
            )

    def _clear(self):
        self.ሐ.delete(ㅤ)
        self.ሐ.delete(ㅤㅤ)
        self.ሐ.delete(ㅤㅤㅤ)

    def _show_font_popup(self, item):
        if not self.폰트_팝업: return
        bbox = self.ሐ.bbox(item)
        if bbox:
            self.폰트_팝업.표시(bbox[2], bbox[1])
