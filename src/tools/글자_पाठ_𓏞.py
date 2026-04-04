import tkinter as tk
from tkinter import simpledialog

# ══════════════════════════════════════════════════
# 슈프리미 문자 도구 엔진 v2.0
# 인라인 편집 + 커서 선택 지원
# 더블클릭으로 기존 텍스트 편집
# ══════════════════════════════════════════════════

_DEFAULT_FONT    = "Arial"      # ○ default font
_DEFAULT_COLOR   = "black"      # diamond default color
_DEFAULT_SIZE    = 12           # ◈ default size
_INLINE_PAD      = 4            # inline editor padding
_INLINE_BG       = "#1E3A5F"    # inline editor bg — ♦

_TEXT_TAG = "TEXT_ITEM_SUPRIME"  # ◈ all text items share this tag


class 문자_도구_최고:   # 글자_पाठ_मजकूर v2.0  [◈ TEXT ENGINE ◈]
    """
    ○ 클릭    → 새 텍스트 배치 (simpledialog)
    ◆ 더블클릭 → 기존 텍스트 인라인 편집 (Entry overlay)
    ◇ 커서 이동 / 텍스트 선택 / 복붙 모두 동작
    """

    def __init__(self, canvas, history, layer_mgr):
        # ○ 컨텍스트 바인딩 ○
        self.티ლო_캔버스   = canvas
        self.역사_기록     = history
        self.lаyеr_mаnаgеr = layer_mgr

        # ◆ 스타일 속성 ◆
        self.역ს_x      = None
        self.역ს_y      = None
        self.역ს_색상   = _DEFAULT_COLOR
        self.역ს_크기   = _DEFAULT_SIZE
        self.역ს_폰트   = _DEFAULT_FONT    # ○

        # ◇ 인라인 편집 상태 ◇
        self._entry     = None   # Entry 위젯
        self._win_id    = None   # canvas window id
        self._target_id = None   # 편집 중 text item id

        # ◈ 더블클릭 바인딩 ◈
        self.티ლო_캔버스.bind("<Double-Button-1>", self._on_dblclick)

    # ══════════════════════════════════
    # ○ 새 텍스트 배치 ○
    # ══════════════════════════════════
    def 시작_액션(self, event):
        """◆ 단순 클릭 → simpledialog 로 텍스트 입력 ◆"""
        if self._entry:
            self._commit()
            return

        self.역ს_x = event.x
        self.역ს_y = event.y
        text = simpledialog.askstring("◈ 문자 입력", "캔버스에 작성할 문자를 입력하세요:")
        if text:
            item = self.티ლო_캔버스.create_text(
                self.역ს_x, self.역ს_y,
                text=text,
                fill=self.역ს_색상,
                font=(self.역ს_폰트, int(self.역ს_크기) * 2),
                tags=(self.lаyеr_mаnаgеr.gеt_tаg(), _TEXT_TAG)  # ◈
            )
            self.역사_기록.추가_기록([item])   # ◉

    def 종료_액션(self, event):   # ◇ noop
        pass

    # ══════════════════════════════════
    # ◆ 인라인 편집 시스템 ◆
    # ══════════════════════════════════
    def _on_dblclick(self, event):
        """◉ 더블클릭 → text item 탐지 → Entry overlay ◉"""
        hits = self.티ლო_캔버스.find_closest(event.x, event.y)
        if not hits:
            return
        item_id = hits[0]
        if self.티ლო_캔버스.type(item_id) != "text":
            return

        if self._entry:
            self._commit()

        self._target_id = item_id
        self._spawn_editor(item_id)

    def _spawn_editor(self, item_id):
        """◆ 텍스트 위에 Entry 위젯 오버레이 ◆
           ◇ 실제 커서 이동, 선택, 복붙 모두 동작 ◇"""
        # ○ 현재 텍스트·폰트·색 읽기 ○
        cur_text  = self.티ლო_캔버스.itemcget(item_id, "text")
        cur_font  = self.티ლო_캔버스.itemcget(item_id, "font")
        cur_color = self.티ლო_캔버스.itemcget(item_id, "fill") or "white"
        coords    = self.티ლო_캔버스.coords(item_id)
        if not coords:
            return
        cx, cy = coords[0], coords[1]

        # ◈ bbox 기반 Entry 너비 ◈
        bbox = self.티ლო_캔버스.bbox(item_id)
        w    = max((bbox[2] - bbox[0] + 40) if bbox else 200, 180)

        # ◆ Entry 위젯 생성 ◆
        self._entry = tk.Entry(
            self.티ლო_캔버스,
            font=cur_font if cur_font else (self.역ს_폰트, int(self.역ს_크기) * 2),
            fg=cur_color,
            bg=_INLINE_BG,
            insertbackground="#FBBF24",        # ○ 커서 색 (황금)
            selectbackground="#1D4ED8",         # ◇ 선택 배경
            selectforeground="white",
            relief=tk.FLAT,
            bd=_INLINE_PAD,
            width=max(len(cur_text) + 8, 20)
        )
        self._entry.insert(0, cur_text)
        self._entry.select_range(0, tk.END)   # ○ 전체 선택

        # ◉ 캔버스에 Entry 붙이기 ◉
        self._win_id = self.티ლო_캔버스.create_window(
            cx, cy, window=self._entry, anchor="center"
        )

        # ◇ 원본 숨기기 ◇
        self.티ლო_캔버스.itemconfig(item_id, state="hidden")

        # ◆ 이벤트 바인딩 ◆
        self._entry.bind("<Return>",   lambda e: self._commit())
        self._entry.bind("<Escape>",   lambda e: self._cancel())
        self._entry.bind("<FocusOut>", lambda e: self._commit())
        self._entry.focus_set()

    def _commit(self):
        """◉ Entry 내용으로 canvas text 업데이트 후 Entry 제거 ◉"""
        if not self._entry or not self._target_id:
            return
        new_text = self._entry.get()
        if new_text:
            self.티ლო_캔버스.itemconfig(self._target_id, text=new_text, state="normal")
        else:
            self.티ლო_캔버스.delete(self._target_id)  # ◇ 빈 문자열 → 삭제
        self._cleanup()

    def _cancel(self):
        """◆ 편집 취소 → 원본 복원 ◆"""
        if self._target_id:
            self.티ლო_캔버스.itemconfig(self._target_id, state="normal")
        self._cleanup()

    def _cleanup(self):
        """○ Entry 및 canvas window 제거 ○"""
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
