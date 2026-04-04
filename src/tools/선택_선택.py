import tkinter as tk

# ══════════════════════════════════════════════════
# 슈프리미 선택·변형 도구 엔진 v2.0
# 이동 + 8방향 리사이징 + 폰트팝업 연동
# ══════════════════════════════════════════════════

# ◆◇○◈♦ 심볼은 문자열·주석 전용 (식별자 아님) ◆◇○◈♦
_HL_TAG     = "highlight_SUPRIME"   # ○ selection border tag
_HANDLE_TAG = "handle_SUPRIME"      # ♦ resize handle tag
_HANDLE_SZ  = 5                     # ○ handle half-size px
_HANDLE_COL = "#FF8C00"             # ◇ handle fill — orange diamond
_HL_COL     = "#FFD700"             # ◉ selection border — gold


class 선택_도구_최고:   # ◈ 선택_액션_프로세스 v2.0 Transformer ◈
    """
    ○ 클릭    → 객체 선택 + 황금 하이라이트
    ◆ 드래그  → 이동
    ◇ 핸들    → 8방향 리사이즈
    ♦ 텍스트  → 폰트 팝업 자동 표시
    """

    def __init__(self, canvas, history, layer_mgr, font_popup=None):
        # ○ 컨텍스트 ○
        self.티ლო_캔버스   = canvas
        self.역사_기록     = history
        self.lаyеr_mаnаgеr = layer_mgr
        self.폰트_팝업     = font_popup   # ◈ 나중에 주입 가능

        # ◆ 상태 변수 ◆
        self.현_선택_객체 = None   # ◆ 선택된 canvas item id
        self.이전_x      = 0       # ◇ 드래그 시작점 x
        self.이전_y      = 0       # ◇ 드래그 시작점 y
        self.변형_모드   = None    # ○ None | 'move' | 'resize'
        self.현_핸들     = None    # ◈ 활성 핸들 방향 ('nw','n','ne',…)

    # ══════════════════════════════════
    # ◈ 폰트 팝업 외부 주입 ◈
    # ══════════════════════════════════
    def 폰트팝업_주입(self, popup):
        self.폰트_팝업 = popup

    # ══════════════════════════════════
    # ○ 마우스 이벤트 핸들러 ○
    # ══════════════════════════════════
    def 시작_액션(self, event):
        """◆ 클릭 우선순위: 핸들 > 객체 > 빈공간 ◆"""
        # ◈ 1순위: 핸들 클릭 감지 ◈
        all_handles = set(self.티ლო_캔버스.find_withtag(_HANDLE_TAG))
        closest     = self.티ლო_캔버스.find_closest(event.x, event.y)

        if closest and closest[0] in all_handles:
            self.변형_모드 = "resize"
            tgs = self.티ლო_캔버스.gettags(closest[0])
            # ◇ 방향 태그 추출 (handle_SUPRIME 외 첫 번째)
            dirs = [t for t in tgs if t not in (_HANDLE_TAG, "current")]
            self.현_핸들 = dirs[0] if dirs else "se"
            self.이전_x, self.이전_y = event.x, event.y
            return

        # ○ 2순위: 일반 객체 클릭 ○
        target = self._find_target(event.x, event.y)

        if target:
            # ◆ 레이어 잠금 확인 ◆
            ltag = [t for t in self.티ლო_캔버스.gettags(target)
                    if t.startswith("레이어_")]
            if (ltag and
                    self.lаyеr_mаnаgеr.lаyеr_dаtа.get(ltag[0], {}).get("lоckеd")):
                return   # ◈ 잠금 레이어 무시

            self._clear()
            self.현_선택_객체 = target
            self.변형_모드    = "move"
            self.이전_x, self.이전_y = event.x, event.y
            self._highlight(target)

            # ♦ 텍스트 아이템이면 폰트 팝업 표시 ♦
            if self.티ლო_캔버스.type(target) == "text":
                self._show_font_popup(target)

        else:
            # ○ 빈 공간 → 선택 해제 ○
            self._clear()
            self.현_선택_객체 = None
            self.변형_모드    = None
            if self.폰트_팝업:
                self.폰트_팝업.숨김()

    def 그리기_액션(self, event):
        """◇ 이동 또는 리사이즈 처리 ◇"""
        if not self.현_선택_객체 or not self.변형_모드:
            return

        dx = event.x - self.이전_x
        dy = event.y - self.이전_y

        if self.변형_모드 == "move":
            # ○ 객체 + 하이라이트 + 핸들 일괄 이동 ○
            self.티ლო_캔버스.move(self.현_선택_객체, dx, dy)
            self.티ლო_캔버스.move(_HL_TAG, dx, dy)
            self.티ლო_캔버스.move(_HANDLE_TAG, dx, dy)

        elif self.변형_모드 == "resize":
            bbox = self.티ლო_캔버스.bbox(self.현_선택_객체)
            if bbox:
                x1, y1, x2, y2 = bbox
                ax, ay = 0.0, 0.0
                sx, sy = 1.0, 1.0
                # ◈ 8방향 핸들별 앵커·스케일 ◈
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

                if sx > 0.05 and sy > 0.05:   # ◇ 최소 크기 가드
                    self.티ლო_캔버스.scale(self.현_선택_객체, ax, ay, sx, sy)
                    self._clear_visual()
                    self._highlight(self.현_선택_객체)

        self.이전_x, self.이전_y = event.x, event.y

    def 종료_액션(self, event):
        """○ ButtonRelease — noop ○"""
        pass

    def 삭제_액션(self, event=None):
        """♦ Delete key → 선택 객체 삭제 ♦"""
        if self.현_선택_객체:
            self.티ლო_캔버스.delete(self.현_선택_객체)
            self._clear()
            self.현_선택_객체 = None
            if self.폰트_팝업:
                self.폰트_팝업.숨김()

    # ══════════════════════════════════
    # ◆ 내부 헬퍼 ◆
    # ══════════════════════════════════
    def _find_target(self, x, y):
        """◇ 하이라이트·핸들 제외한 가장 가까운 아이템 ◇"""
        hits = self.티ლო_캔버스.find_closest(x, y)
        if not hits:
            return None
        tgs = self.티ლო_캔버스.gettags(hits[0])
        if _HL_TAG in tgs or _HANDLE_TAG in tgs:
            return None
        return hits[0]

    def _highlight(self, item):
        """◉ 선택 하이라이트 + 8방향 핸들 렌더링 ◉"""
        bbox = self.티ლო_캔버스.bbox(item)
        if not bbox:
            return
        x1, y1, x2, y2 = bbox

        # ○ 선택 테두리 (황금 점선) ○
        self.티ლო_캔버스.create_rectangle(
            x1-2, y1-2, x2+2, y2+2,
            outline=_HL_COL, dash=(5, 3),
            tags=_HL_TAG
        )

        # ◆ 8방향 핸들 (주황 사각형) ◆
        cx, cy = (x1+x2)/2, (y1+y2)/2
        handles = [
            (x1, y1, "nw"), (cx, y1, "n"),  (x2, y1, "ne"),
            (x1, cy, "w"),                   (x2, cy, "e"),
            (x1, y2, "sw"), (cx, y2, "s"),  (x2, y2, "se"),
        ]
        hs = _HANDLE_SZ
        for hx, hy, direction in handles:
            self.티ლო_캔버스.create_rectangle(
                hx-hs, hy-hs, hx+hs, hy+hs,
                fill=_HANDLE_COL, outline="white",
                tags=(_HANDLE_TAG, direction)
            )

    def _clear(self):
        """○ 하이라이트 + 핸들 전체 제거 ○"""
        self.티ლო_캔버스.delete(_HL_TAG)
        self.티ლო_캔버스.delete(_HANDLE_TAG)

    def _clear_visual(self):
        self._clear()

    def _show_font_popup(self, item):
        """◈ 텍스트 아이템 bbox 우측에 팝업 표시 ◈"""
        if not self.폰트_팝업:
            return
        bbox = self.티ლო_캔버스.bbox(item)
        if bbox:
            self.폰트_팝업.표시(bbox[2], bbox[1])   # ◉ 우측 상단 기준
