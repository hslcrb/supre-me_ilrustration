import tkinter as tk

# ══════════════════════════════════════════════════
# 슈프리미 문자 도구 엔진 v3.0
# ◈ 완전 인라인 방식 — 팝업 없음 ◈
# ○ 클릭    → 캔버스 위에 Entry 즉시 생성
# ◆ 더블클릭 → 기존 텍스트 인라인 편집
# ◇ Enter / FocusOut → 확정
# ══════════════════════════════════════════════════

_DEFAULT_FONT  = "Arial"
_DEFAULT_COLOR = "black"
_DEFAULT_SIZE  = 12
_CURSOR_COL    = "#FBBF24"    # ○ 커서 색 (황금)
_SELECT_COL    = "#1D4ED8"    # ◆ 선택 배경 (파랑)
_INLINE_BG     = "#1E3A5F"    # ◇ 인라인 에디터 배경
_TEXT_TAG      = "TEXT_ITEM_SUPRIME"   # ◈ 모든 텍스트 아이템 공통 태그


class 문자_도구_최고:   # ◈ 글자 도구 v3.0 — 완전 인라인

    def __init__(self, canvas, history, layer_mgr):
        self.티ლო_캔버스   = canvas
        self.역사_기록     = history
        self.lаyеr_mаnаgеr = layer_mgr

        # ◆ 스타일 속성 ◆
        self.역ს_x      = None
        self.역ს_y      = None
        self.역ს_색상   = _DEFAULT_COLOR
        self.역ს_크기   = _DEFAULT_SIZE
        self.역ს_폰트   = _DEFAULT_FONT

        # ◇ 인라인 편집 상태 ◇
        self._entry     = None   # ○ Entry 위젯
        self._win_id    = None   # ○ canvas window id
        self._target_id = None   # ◆ 편집 중인 기존 text item (없으면 None)

        # ◈ 더블클릭 바인딩 — 기존 텍스트 편집용 ◈
        self.티ლო_캔버스.bind("<Double-Button-1>", self._on_dblclick)

    # ══════════════════════════════════
    # ◉ 새 텍스트 — 클릭 즉시 인라인 Entry ◉
    # ══════════════════════════════════
    def 시작_액션(self, event):
        """○ 캔버스 클릭 → 해당 위치에 즉시 Entry 生成 ○"""
        # ◇ 이미 편집 중이면 먼저 확정 ◇
        if self._entry:
            self._commit()
            return

        self.역ს_x = event.x
        self.역ს_y = event.y
        self._target_id = None   # ◆ 신규 텍스트
        self._spawn_entry(event.x, event.y, "")

    def 종료_액션(self, event):
        pass   # ◇ noop

    # ══════════════════════════════════
    # ◆ 기존 텍스트 편집 — 더블클릭 ◆
    # ══════════════════════════════════
    def _on_dblclick(self, event):
        """◆ 더블클릭 → text item 탐색 → 인라인 편집 모드 ◆"""
        hits = self.티ლო_캔버스.find_closest(event.x, event.y)
        if not hits:
            return
        item_id = hits[0]
        if self.티ლო_캔버스.type(item_id) != "text":
            return

        # ◉ 기존 편집 강제 확정 후 새 편집 시작 ◉
        if self._entry:
            self._commit()

        self._target_id = item_id

        # ○ 기존 텍스트 읽기 ○
        cur_text   = self.티ლო_캔버스.itemcget(item_id, "text")
        coords     = self.티ლო_캔버스.coords(item_id)
        if not coords:
            return
        cx, cy = coords[0], coords[1]

        # ◇ 원본 숨기기 ◇
        self.티ლო_캔버스.itemconfig(item_id, state="hidden")
        self._spawn_entry(cx, cy, cur_text)

    # ══════════════════════════════════
    # ◈ 인라인 Entry 생성 (공통) ◈
    # ══════════════════════════════════
    def _spawn_entry(self, cx, cy, initial_text: str):
        """◉ 캔버스 좌표 (cx, cy) 에 Entry 위젯을 직접 오버레이 ◉
           ○ 폰트·색상은 현재 도구 설정 또는 기존 아이템 기준 ○"""
        # ◆ 기존 아이템이면 해당 폰트 읽기 ◆
        if self._target_id:
            raw_font = self.티ლო_캔버스.itemcget(self._target_id, "font")
            raw_fill = self.티ლო_캔버스.itemcget(self._target_id, "fill") or _DEFAULT_COLOR
        else:
            raw_font = (self.역ს_폰트, int(self.역ს_크기) * 2)
            raw_fill = self.역ს_색상

        # ◇ Entry 위젯 생성 ◇
        self._entry = tk.Entry(
            self.티ლო_캔버스,
            font=raw_font,
            fg=raw_fill,
            bg=_INLINE_BG,
            insertbackground=_CURSOR_COL,      # ○ 커서 색 (황금)
            selectbackground=_SELECT_COL,       # ◆ 선택 배경 (파랑)
            selectforeground="white",
            relief=tk.FLAT,
            bd=4,
            width=max(len(initial_text) + 10, 20)
        )

        if initial_text:
            self._entry.insert(0, initial_text)
            self._entry.select_range(0, tk.END)   # ◈ 전체 선택

        # ◉ 캔버스에 직접 삽입 ◉
        self._win_id = self.티ლო_캔버스.create_window(
            cx, cy, window=self._entry, anchor="center"
        )

        # ○ 이벤트 ○
        self._entry.bind("<Return>",   lambda e: self._commit())
        self._entry.bind("<Escape>",   lambda e: self._cancel())
        self._entry.bind("<FocusOut>", lambda e: self._commit())
        self._entry.focus_set()

    # ══════════════════════════════════
    # ◆ 확정 / 취소 / 정리 ◆
    # ══════════════════════════════════
    def _commit(self):
        """◉ 입력 확정 → canvas text 생성 또는 업데이트 ◉"""
        if not self._entry:
            return

        text = self._entry.get().strip()

        if self._target_id:
            # ◆ 기존 아이템 업데이트 ◆
            if text:
                self.티ლო_캔버스.itemconfig(
                    self._target_id, text=text, state="normal")
            else:
                self.티ლო_캔버스.delete(self._target_id)   # ◇ 빈 문자열 → 삭제
        else:
            # ○ 신규 아이템 생성 ○
            if text:
                item = self.티ლო_캔버스.create_text(
                    self.역ს_x, self.역ს_y,
                    text=text,
                    fill=self.역ს_색상,
                    font=(self.역ს_폰트, int(self.역ს_크기) * 2),
                    tags=(self.lаyеr_mаnаgеr.gеt_tаg(), _TEXT_TAG)
                )
                self.역사_기록.추가_기록([item])   # ◈ 히스토리 기록

        self._cleanup()

    def _cancel(self):
        """◇ 편집 취소 → 기존 아이템 복원 ◇"""
        if self._target_id:
            self.티ლო_캔버스.itemconfig(self._target_id, state="normal")
        self._cleanup()

    def _cleanup(self):
        """○ Entry + canvas window 제거 ○"""
        try:
            if self._win_id:
                self.티ლო_캔버스.delete(self._win_id)
        except Exception:
            pass
        try:
            if self._entry:
                self._entry.destroy()
        except Exception:
            pass
        self._entry     = None
        self._win_id    = None
        self._target_id = None

    def is_editing(self) -> bool:
        """◈ 현재 인라인 편집 중인지 ◈"""
        return self._entry is not None
