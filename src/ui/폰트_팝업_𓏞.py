import tkinter as tk
from tkinter import font as tkfont

# ══════════════════════════════════════════════════
# 슈프리미 폰트 팝업 엔진
# ◈ 각 폰트 이름이 실제 해당 폰트로 렌더링됨 ◈
# ○ 텍스트 객체 선택 시 bbox 우측에 자동 표시 ○
# ══════════════════════════════════════════════════

# ◆◇○◈♦ 심볼 — 문자열·주석 전용 (식별자 아님)
_POPUP_W    = 240         # ○ popup width
_POPUP_H    = 360         # ◆ popup height
_MAX_RENDER = 300         # ◉ max fonts rendered at once
_BG         = "#111827"   # ◇ popup background
_HDR_BG     = "#1F2937"   # ○ header background
_ACCENT     = "#FBBF24"   # ♦ gold accent
_ENTRY_BG   = "#374151"   # ◆ search entry background
_ITEM_BG    = "#111827"   # ◈ item background
_ITEM_HOVER = "#1D4ED8"   # ◇ item hover background


class 폰트_팝업_최고:   # ◈ Font-Hover-Popup-Master ◈
    """
    ◉ 텍스트 객체 선택 시 나타나는 폰트 선택 팝업
    ◆ 각 항목이 실제 해당 폰트로 렌더링됨 (미리보기)
    ○ 검색 기능 포함 — 실시간 필터링
    ◇ 선택 즉시 콜백 호출 후 팝업 닫힘
    """

    def __init__(self, root, canvas, font_select_cb):
        # ○ 바인딩 ○
        self.root     = root
        self.canvas   = canvas
        self.on_pick  = font_select_cb   # ◇ fn(font_name: str) → None
        self.popup    = None             # ○ Toplevel 참조
        self._search  = None            # ◆ StringVar
        self._fc      = None            # ◈ inner canvas (scroll)
        self._inner   = None            # ◇ inner frame
        self._fc_win  = None            # ○ canvas window id
        self._fonts   = []              # ♦ 전체 폰트 목록

        self._load_fonts()

    # ══════════════════════════════════
    # ◆ 초기화 ◆
    # ══════════════════════════════════
    def _load_fonts(self):
        """◉ 시스템 폰트 전체 스캔 + 정규화 ◉"""
        raw = sorted(set(tkfont.families()))
        self._fonts = [
            f for f in raw
            if not f.startswith('@') and not f.startswith('_') and f
        ]

    # ══════════════════════════════════
    # ◈ 공개 API ◈
    # ══════════════════════════════════
    def 표시(self, canvas_bx, canvas_by):
        """◆ 팝업 표시 — canvas bbox 좌표 기준 ◆"""
        self.숨김()   # ○ 기존 팝업 제거

        # ◉ 캔버스 → 화면 절대 좌표 변환 ◉
        rx = self.canvas.winfo_rootx() + int(canvas_bx) + 18
        ry = self.canvas.winfo_rooty() + int(canvas_by)

        # ◇ 화면 경계 클램핑 ◇
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        rx = min(rx, sw - _POPUP_W - 10)
        ry = min(ry, sh - _POPUP_H - 10)

        # ━━━ Toplevel 생성 ━━━
        self.popup = tk.Toplevel(self.root)
        self.popup.overrideredirect(True)        # ○ 타이틀바 없음
        self.popup.attributes('-topmost', True)
        self.popup.geometry(f"{_POPUP_W}x{_POPUP_H}+{rx}+{ry}")
        self.popup.configure(bg=_BG)

        # ◈ 헤더 ◈
        hdr = tk.Frame(self.popup, bg=_HDR_BG, pady=5)
        hdr.pack(fill=tk.X)
        tk.Label(hdr, text="◈ 폰트 미리보기 ◈",
                 bg=_HDR_BG, fg=_ACCENT,
                 font=("Malgun Gothic", 9, "bold")).pack()
        tk.Label(hdr, text="○ 이름이 해당 폰트로 표시됨 ○",
                 bg=_HDR_BG, fg="#6B7280",
                 font=("Arial", 7)).pack()

        # ◇ 검색 엔트리 ◇
        self._search = tk.StringVar()
        entry = tk.Entry(self.popup, textvariable=self._search,
                         bg=_ENTRY_BG, fg="white",
                         insertbackground=_ACCENT,
                         relief=tk.FLAT, font=("Arial", 10), bd=4)
        entry.pack(fill=tk.X, padx=8, pady=(4, 2))
        entry.insert(0, "폰트 검색...")
        entry.bind("<FocusIn>",  lambda e: entry.delete(0, tk.END))

        self._search.trace("w", lambda *_: self._filter())

        # ◆ 스크롤 리스트 ◆
        list_fr = tk.Frame(self.popup, bg=_BG)
        list_fr.pack(fill=tk.BOTH, expand=True, padx=4, pady=(0, 4))

        sb = tk.Scrollbar(list_fr, orient=tk.VERTICAL,
                          bg="#374151", troughcolor=_BG,
                          activebackground=_ACCENT)
        self._fc = tk.Canvas(list_fr, bg=_BG,
                             yscrollcommand=sb.set,
                             highlightthickness=0)
        sb.config(command=self._fc.yview)
        sb.pack(side=tk.RIGHT, fill=tk.Y)
        self._fc.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self._inner = tk.Frame(self._fc, bg=_BG)
        self._fc_win = self._fc.create_window(
            (0, 0), window=self._inner, anchor="nw"
        )

        self._inner.bind("<Configure>",
            lambda e: self._fc.configure(
                scrollregion=self._fc.bbox("all")))
        self._fc.bind("<Configure>",
            lambda e: self._fc.itemconfig(self._fc_win, width=e.width))
        self._fc.bind("<MouseWheel>",
            lambda e: self._fc.yview_scroll(
                int(-1 * (e.delta / 120)), "units"))

        # ◉ 첫 렌더링 ◉
        self._render(self._fonts[:_MAX_RENDER])

        # ○ 외부 클릭 감지 ○
        self.popup.bind("<FocusOut>", self._on_focus_out)
        self.popup.after(120, lambda: entry.focus_set())

    def 숨김(self):
        """○ 팝업 안전 제거 ○"""
        if self.popup:
            try:
                self.popup.destroy()
            except Exception:
                pass
            self.popup = None

    # ══════════════════════════════════
    # ◆ 내부 렌더링 ◆
    # ══════════════════════════════════
    def _render(self, fonts):
        """◆ 각 폰트를 해당 폰트 자체로 렌더링 ◆
           ◇ 렌더링 실패 폰트는 조용히 스킵 ◇"""
        for w in self._inner.winfo_children():
            w.destroy()

        for fname in fonts:
            try:
                fr = tk.Frame(self._inner, bg=_BG)
                fr.pack(fill=tk.X, pady=1, padx=2)

                # ◈ 폰트 이름 → 실제 해당 폰트로 렌더링 ◈
                lbl = tk.Label(
                    fr,
                    text=fname,
                    font=(fname, 12),      # ◉ 핵심: 폰트 자신으로 렌더링
                    bg=_ITEM_BG, fg="#E5E7EB",
                    anchor="w", padx=8, pady=3,
                    cursor="hand2"
                )
                lbl.pack(fill=tk.X)
                lbl.bind("<Enter>",
                    lambda e, l=lbl: l.config(bg=_ITEM_HOVER, fg=_ACCENT))
                lbl.bind("<Leave>",
                    lambda e, l=lbl: l.config(bg=_ITEM_BG, fg="#E5E7EB"))
                lbl.bind("<Button-1>",
                    lambda e, fn=fname: self._select(fn))

            except Exception:
                pass   # ◇ 렌더 불가 폰트 스킵

    def _filter(self):
        """◇ 실시간 검색 필터링 ◇"""
        kw = self._search.get().lower()
        if kw in ("", "폰트 검색..."):
            result = self._fonts[:_MAX_RENDER]
        else:
            result = [f for f in self._fonts if kw in f.lower()]
        self._render(result)

    def _select(self, fname):
        """◉ 폰트 선택 완료 → 콜백 실행 후 팝업 닫기 ◉"""
        self.on_pick(fname)
        self.숨김()

    def _on_focus_out(self, event):
        """○ 포커스 이탈 → 지연 후 닫기 ○"""
        try:
            if self.popup:
                focused = str(self.root.focus_get())
                if self.popup and not focused.startswith(str(self.popup)):
                    self.root.after(180, self._delayed_close)
        except Exception:
            pass

    def _delayed_close(self):
        """◆ 팝업 내부에 포커스 없으면 닫기 ◆"""
        try:
            if self.popup and self.root.focus_get():
                focused = str(self.root.focus_get())
                if not focused.startswith(str(self.popup)):
                    self.숨김()
        except Exception:
            self.숨김()
