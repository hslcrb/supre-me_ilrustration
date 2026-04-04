import tkinter as tk
from tkinter import ttk

# ══════════════════════════════════════════════════
# 슈프리미 문자 도구 엔진 v4.0
# ◈ 완전 인라인 — 투명 박스 + 폰트 크기 조절 ◈
# ○ 클릭    → 캔버스 위 투명 Entry 즉시 생성
# ◆ 더블클릭 → 기존 텍스트 인라인 편집
# ◇ 옆에 폰트 크기 스핀박스 함께 표시
# ══════════════════════════════════════════════════

_DEFAULT_FONT  = "Arial"
_DEFAULT_COLOR = "black"
_DEFAULT_SIZE  = 24        # ○ 기본 폰트 크기 (px, 직접)
_TEXT_TAG      = "TEXT_ITEM_SUPRIME"   # ◈ 공통 태그


class 문자_도구_최고:   # ◈ 글자 도구 v4.0 — 투명 인라인

    def __init__(self, canvas, history, layer_mgr):
        self.티ლო_캔버스   = canvas
        self.역사_기록     = history
        self.lаyеr_mаnаgеr = layer_mgr

        # ◆ 스타일 속성 ◆
        self.역ს_x      = None
        self.역ს_y      = None
        self.역ს_색상   = _DEFAULT_COLOR
        self.역ს_크기   = _DEFAULT_SIZE    # ○ 실제 px 크기 (×2 없음)
        self.역ს_폰트   = _DEFAULT_FONT

        # ◇ 인라인 편집 상태 ◇
        self._entry      = None    # ○ Entry 위젯
        self._win_id     = None    # ○ canvas window id (entry)
        self._ctrl_win   = None    # ◆ canvas window id (size control)
        self._ctrl_frame = None    # ◆ 크기 조절 Frame
        self._size_var   = None    # ◈ 폰트 크기 IntVar
        self._target_id  = None    # ◆ 편집 중인 기존 text item

        # ◆ 더블클릭 바인딩 ◆
        self.티ლო_캔버스.bind("<Double-Button-1>", self._on_dblclick)

    # ══════════════════════════════════
    # ◉ 신규 텍스트 — 클릭 즉시 인라인
    # ══════════════════════════════════
    def 시작_액션(self, event):
        """○ 캔버스 클릭 → 투명 Entry 즉시 생성 ○"""
        if self._entry:
            self._commit()
            return
        self.역ს_x = event.x
        self.역ს_y = event.y
        self._target_id = None
        self._spawn(event.x, event.y, "", self.역ს_색상, self.역ს_크기, self.역ს_폰트)

    def 종료_액션(self, event):
        pass

    # ══════════════════════════════════
    # ◆ 기존 텍스트 편집 — 더블클릭
    # ══════════════════════════════════
    def _on_dblclick(self, event):
        hits = self.티ლო_캔버스.find_closest(event.x, event.y)
        if not hits:
            return
        item_id = hits[0]
        if self.티ლო_캔버스.type(item_id) != "text":
            return

        if self._entry:
            self._commit()

        self._target_id = item_id
        cur_text  = self.티ლო_캔버스.itemcget(item_id, "text")
        cur_fill  = self.티ლო_캔버스.itemcget(item_id, "fill") or _DEFAULT_COLOR
        raw_font  = self.티ლო_캔버스.itemcget(item_id, "font")
        cur_font, cur_size = self._parse_font(raw_font)

        coords = self.티ლო_캔버스.coords(item_id)
        if not coords:
            return
        self.역ს_x, self.역ს_y = coords[0], coords[1]

        self.티ლო_캔버스.itemconfig(item_id, state="hidden")
        self._spawn(coords[0], coords[1], cur_text, cur_fill, cur_size, cur_font)

    # ══════════════════════════════════
    # ◈ Entry + 크기 컨트롤 생성 (공통)
    # ══════════════════════════════════
    def _spawn(self, cx, cy, init_text: str, color: str, size: int, font: str):
        """◉ 투명 Entry 오버레이 + 우측에 폰트 크기 컨트롤 ◉"""

        # ━━━ 폰트 크기 IntVar ━━━
        self._size_var = tk.IntVar(value=size)

        # ━━━ 투명 Entry ━━━
        # ◇ bg = 캔버스 배경 → 시각적 투명 효과
        canvas_bg = self.티ლო_캔버스.cget("bg")   # ○ "white"

        self._entry = tk.Entry(
            self.티ლო_캔버스,
            font=(font, size),
            fg=color,
            bg=canvas_bg,               # ◈ 캔버스 배경과 동일 → 투명 효과
            insertbackground=color,     # ○ 커서 색 = 텍스트 색
            selectbackground="#FBBF24", # ◆ 선택 배경 (황금)
            selectforeground="black",
            relief=tk.FLAT,
            bd=0,                       # ◇ 테두리 없음
            highlightthickness=1,       # ◉ 얇은 포커스 테두리만
            highlightcolor="#FBBF24",   # ◉ 황금 포커스 테두리
            highlightbackground=canvas_bg,
            width=max(len(init_text) + 10, 20)
        )

        if init_text:
            self._entry.insert(0, init_text)
            self._entry.select_range(0, tk.END)

        self._win_id = self.티ლო_캔버스.create_window(
            cx, cy, window=self._entry, anchor="center"
        )

        # ━━━ 크기 컨트롤 Frame ━━━
        self._ctrl_frame = tk.Frame(
            self.티ლო_캔버스,
            bg="#1F2937",         # ◆ 다크 컨트롤 배경
            padx=4, pady=2
        )

        # ○ 레이블 ○
        tk.Label(self._ctrl_frame, text="크기",
                 bg="#1F2937", fg="#9CA3AF",
                 font=("Malgun Gothic", 7)).pack(side=tk.LEFT, padx=(2, 0))

        # ◆ − 버튼 ◆
        tk.Button(
            self._ctrl_frame, text="−",
            command=self._size_down,
            bg="#374151", fg="white",
            relief=tk.FLAT, width=2, font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=1)

        # ◈ 크기 스핀박스 ◈
        spin = tk.Spinbox(
            self._ctrl_frame,
            from_=6, to=200,
            textvariable=self._size_var,
            width=4, font=("Arial", 9),
            bg="#374151", fg="white",
            buttonbackground="#374151",
            relief=tk.FLAT,
            command=self._on_size_change
        )
        spin.pack(side=tk.LEFT, padx=1)
        spin.bind("<Return>",    lambda e: self._on_size_change())
        spin.bind("<FocusOut>",  lambda e: self._on_size_change())

        # ◆ + 버튼 ◆
        tk.Button(
            self._ctrl_frame, text="+",
            command=self._size_up,
            bg="#374151", fg="white",
            relief=tk.FLAT, width=2, font=("Arial", 9, "bold"),
            cursor="hand2"
        ).pack(side=tk.LEFT, padx=1)

        # ◉ 캔버스에 컨트롤 배치 (Entry 바로 위쪽)
        self._ctrl_win = self.티ლო_캔버스.create_window(
            cx, cy - size - 18,   # ◇ Entry 위쪽에 배치
            window=self._ctrl_frame, anchor="center"
        )

        # ━━━ 이벤트 바인딩 ━━━
        self._entry.bind("<Return>",   lambda e: self._commit())
        self._entry.bind("<Escape>",   lambda e: self._cancel())
        self._entry.bind("<FocusOut>", self._on_entry_focusout)
        self._entry.focus_set()

    # ══════════════════════════════════
    # ◆ 크기 조절 로직
    # ══════════════════════════════════
    def _on_size_change(self):
        """◈ 스핀박스 변경 → Entry 폰트 실시간 업데이트 ◈"""
        if not self._entry or not self._size_var:
            return
        try:
            new_size = max(6, min(200, self._size_var.get()))
            self._size_var.set(new_size)
        except (tk.TclError, ValueError):
            new_size = _DEFAULT_SIZE
            self._size_var.set(new_size)

        cur_font = self._entry.cget("font")
        fname = self._parse_font(str(cur_font))[0]
        self._entry.config(font=(fname, new_size))
        self.역ს_크기 = new_size   # ◆ 전역 크기 업데이트

        # ◇ 컨트롤 위치 재조정 ◇
        if self._win_id and self._ctrl_win:
            coords = self.티ლო_캔버스.coords(self._win_id)
            if coords:
                self.티ლო_캔버스.coords(self._ctrl_win,
                                        coords[0], coords[1] - new_size - 18)

    def _size_up(self):
        """○ + 버튼 → 크기 +2 ○"""
        if self._size_var:
            self._size_var.set(min(200, self._size_var.get() + 2))
            self._on_size_change()

    def _size_down(self):
        """○ − 버튼 → 크기 −2 ○"""
        if self._size_var:
            self._size_var.set(max(6, self._size_var.get() - 2))
            self._on_size_change()

    # ══════════════════════════════════
    # ◉ 확정 / 취소 / 정리
    # ══════════════════════════════════
    def _on_entry_focusout(self, event):
        """◇ FocusOut — 컨트롤로 이동 시 닫기 방지 ◇"""
        try:
            focused = str(self.티ლო_캔버스.winfo_toplevel().focus_get())
            # ◆ 크기 컨트롤 위젯으로 이동한 경우 닫지 않음 ◆
            if self._ctrl_frame and focused.startswith(str(self._ctrl_frame)):
                return
        except Exception:
            pass
        self._commit()

    def _commit(self):
        """◉ 확정 → canvas text 생성/업데이트 ◉"""
        if not self._entry:
            return

        text = self._entry.get()
        size = self._size_var.get() if self._size_var else self.역ს_크기
        cur_font = self._parse_font(str(self._entry.cget("font")))[0]

        if self._target_id:
            # ◆ 기존 아이템 업데이트 ◆
            if text:
                self.티ლო_캔버스.itemconfig(
                    self._target_id,
                    text=text,
                    font=(cur_font, size),
                    state="normal"
                )
            else:
                self.티ლო_캔버스.delete(self._target_id)
        else:
            # ○ 신규 아이템 생성 ○
            if text:
                item = self.티ლო_캔버스.create_text(
                    self.역ს_x, self.역ს_y,
                    text=text,
                    fill=self.역ს_색상,
                    font=(cur_font, size),
                    tags=(self.lаyеr_mаnаgеr.gеt_tаg(), _TEXT_TAG)
                )
                self.역사_기록.ꦆ_기록_추가("CREATE", [item])
                self.역ს_크기 = size   # ◈ 크기 기억

        self._cleanup()

    def _cancel(self):
        """◇ 취소 → 기존 아이템 복원 ◇"""
        if self._target_id:
            self.티ლო_캔버스.itemconfig(self._target_id, state="normal")
        self._cleanup()

    def _cleanup(self):
        """○ Entry + 컨트롤 완전 제거 ○"""
        for win_id in [self._win_id, self._ctrl_win]:
            try:
                if win_id:
                    self.티ლო_캔버스.delete(win_id)
            except Exception:
                pass
        for widget in [self._entry, self._ctrl_frame]:
            try:
                if widget:
                    widget.destroy()
            except Exception:
                pass
        self._entry      = None
        self._win_id     = None
        self._ctrl_win   = None
        self._ctrl_frame = None
        self._size_var   = None
        self._target_id  = None

    def is_editing(self) -> bool:
        return self._entry is not None

    # ══════════════════════════════════
    # ◇ 유틸리티
    # ══════════════════════════════════
    @staticmethod
    def _parse_font(raw: str) -> tuple:
        """◆ 폰트 문자열 → (font_name, size) 튜플 ◆
           ◇ 예: 'Arial 24' → ('Arial', 24) ◇"""
        try:
            parts = raw.strip().split()
            # ○ Tkinter 반환 형식: '{Font Name} size' or 'FontName size'
            if raw.startswith('{'):
                end = raw.index('}')
                fname = raw[1:end]
                rest = raw[end+1:].strip().split()
                size = int(rest[0]) if rest else _DEFAULT_SIZE
            else:
                size = int(parts[-1]) if parts[-1].isdigit() else _DEFAULT_SIZE
                fname = " ".join(p for p in parts[:-1] if not p.lstrip('-').isdigit()) or _DEFAULT_FONT
            return fname, size
        except Exception:
            return _DEFAULT_FONT, _DEFAULT_SIZE
