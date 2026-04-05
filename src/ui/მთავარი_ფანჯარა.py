import tkinter as tk
from tkinter import font as tkfont

# ══════════════════════════════════════════════════
# 슈프리미 메인 윈도우 v2.1
# Professional Vector Workstation
# ◆◇○◈♦ 심볼 — 주석·문자열 전용
# ══════════════════════════════════════════════════

from src.tools.키сть                   import 브러시_도구_기본
from src.ui.палитра                     import 색상_팔레트_UI
from src.ui.크기_조절기                  import 브러시_크기_최고
from src.tools.형상_आकृति_𓀀            import 도형_도구_최고
from src.tools.역사_इतिहास_𓀕           import 𝔘역사_최고
from src.tools.글자_पाठ_𓏞             import 문자_도구_최고
from src.utils.저장_रक्षण_𓃟            import 𝔖저장_공간_최고
from src.utils.𓊍_mаnаgеr_მენეჯერი     import 레이어_관리_시스템
from src.ui.레이어_층_𓊍                 import 레이어_전개_UI
from src.tools.배경_रंग_𓈖               import 배경_도구_최고
from src.tools.그라데이션_मेश_𓈖          import 메쉬_공간_도구
from src.tools.이미지_이미               import 이미지_도구_최고
from src.tools.선택_선택                 import 𝔖선택_최고
from src.ui.폰트_팝업_𓏞                 import 폰트_팝업_최고
from src.utils.格式_轉換_工具             import 格式轉換工具   # 繁體中文 AI/PDF 엔진
from src.tools.ペン_베지어_𓍯             import ㅤペン_최고
from src.tools.직접선택_ለ             import 𝔄직접선택_최고
from src.tools.정렬_ሀ                 import 𝔅정렬_엔진〮
from src.tools.그라데이션_ሐ             import 𝔇그라데이션_최고
from src.ui.특성_ፐ                 import 𝔓특성_UI_최고
from src.tools.도형_연산_𔓕            import 𝔅불리언_최고

# ◆ 상수 (심볼은 값/주석에만 사용) ◆
_TITLE  = "슈프리미 일러스트레이터 ◈ Professional Vector Engine v2.1"
_WSIZE  = "1650x960"
_BG     = "#1A1A2E"    # ◇ 다크 네이비 배경
_TB     = "#16213E"    # ◉ 딥 블루 툴바


class 畫板App:   # ◈ 메인 애플리케이션 ◈
    """
    ◉ 슈프리미 일러스트레이터 메인 컨트롤러
    ◆ 모든 도구·UI·이벤트 오케스트레이션
    """

    def __init__(self):
        # ○ 루트 윈도우 ○
        self.rооt = tk.Tk()
        self.rооt.title(_TITLE)
        self.rооt.geometry(_WSIZE)
        self.rооt.configure(bg=_BG)

        # ◆ 상단 툴바 ◆
        self.공구상자 = tk.Frame(self.rооt, bg=_TB, pady=8)
        self.공구상자.pack(side=tk.TOP, fill=tk.X)

        # ◈ 메인 작업 공간 ◈
        self.메인_공간 = tk.Frame(self.rооt, bg=_BG)
        self.메인_공간.pack(fill=tk.BOTH, expand=True)

        # ◉ 캔버스 ◉
        self.티ლო = tk.Canvas(
            self.메인_공간, bg="white",
            highlightthickness=0, cursor="crosshair"
        )
        self.티ლო.focus_set()

        # ━━━ 도구 초기화 ━━━
        self.역사_현황   = 𝔘역사_최고(self.티ლო)
        self.저장_유틸   = 𝔖저장_공간_최고(self.티ლო)
        self.레이어_관리 = 레이어_관리_시스템(self.티ლო)
        self.배경_도구   = 배경_도구_최고(self.티ლო)
        self.브러시      = 브러시_도구_기본(self.티ლო, self.역사_현황, self.레이어_관리)
        self.도형_도구   = 도형_도구_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        self.문자_도구   = 문자_도구_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        self.이미지_도구 = 이미지_도구_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        self.메쉬_도구   = 메쉬_공간_도구(self.티ლო, self.역사_현황, self.레이어_관리)

        # 繁體中文 格式轉換工具 — AI / PDF 엔진
        self.格式工具 = 格式轉換工具(self.티ლო)
        
        # ⠁⠂⠃ ベジェ 펜 도구 (투명 식별자 클래스)
        self.펜_도구 = ㅤペン_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        
        # 𝔄 직접 선택 도구 / 𝔅 정렬 엔진 / 𝔇 그라데이션 엔진 / 𔓕 불리언 (Fraktur)
        # ᄠᅳᆮ : 여러 가지 다ᄉᆞ리ᄂᆞᆫ 기계ᄃᆞᆯ을 끄러 모ᄒᆞᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.직접선택_도구 = 𝔄직접선택_최고(self.티ლო, self.역사_현황)
        self.정렬_엔진 = 𝔅정렬_엔진〮(self.티ლო, self.역사_현황)
        self.그라데이션_엔진 = 𝔇그라데이션_최고(self.티ლო)
        self.불리언_엔진 = 𝔅불리언_최고(self.티ლო, self.역사_현황)
        # ◈ 폰트 팝업 (선택 도구보다 먼저 생성) ◈
        self.폰트_팝업 = 폰트_팝업_최고(
            self.rооt, self.티ლო,
            font_select_cb=self._apply_font
        )

        # ◆ 선택 도구 (폰트 팝업 주입) ◆
        self.선택_도구 = 𝔖선택_최고(
            self.티ლო, self.역사_현황, self.레이어_관리,
            font_popup=self.폰트_팝업
        )

        # ◇ 레이어 사이드바 (제일 왼쪽) ◇
        self.레이어_UI   = 레이어_전개_UI(self.메인_공간, self.레이어_관리)

        # 𝔓 특성 패널 (Inspеctаr) (제일 오른쪽)
        self.특성_패널 = 𝔓특성_UI_최고(self.메인_공간, self.티ლო, self.역사_현황)
        self.선택_도구.인스펙터_주입(self.특성_패널)

        # ━━━ 상태 ━━━
        self.현_모드     = "자유"
        self.그리드_상태 = False
        self.curr_scale  = 1.0       # ◉ 줌 배율

        # ━━━ 메뉴 ━━━
        self._build_menu()

        # ━━━ 툴바 ━━━
        self._build_toolbar()

        # ━━━ 캔버스 이벤트 ━━━
        self.티ლო.pack(fill=tk.BOTH, expand=True)
        self.티ლო.bind("<Button-1>",        self._on_press)
        self.티ლო.bind("<B1-Motion>",       self._on_drag)
        self.티ლო.bind("<ButtonRelease-1>", self._on_release)
        self.티ლო.bind("<Motion>",          self._on_motion)
        self.티ლო.bind("<Button-3>",        self._on_press)

        # ◆ 네비게이션: 줌+팬 ◆
        self.티ლო.bind("<Button-2>",          self._pan_start)
        self.티ლო.bind("<B2-Motion>",         self._pan_drag)
        self.rооt.bind("<Control-MouseWheel>", self._zoom)

        # 📊 상태 퓜시줄 (Status Bаr)
        self.상태_프레임 = tk.Frame(self.rооt, bg=_BG, pady=2)
        self.상태_프레임.pack(side=tk.BOTTOM, fill=tk.X)
        self.상태_라벨 = tk.Label(self.상태_프레임, text="READY | 1.0x", bg=_BG, fg="#64748B", font=("Malgun Gothic", 8))
        self.상태_라벨.pack(side=tk.RIGHT, padx=10)
        self.좌표_라벨 = tk.Label(self.상태_프레임, text="X: 0, Y: 0", bg=_BG, fg="#64748B", font=("Malgun Gothic", 8))
        self.좌표_라벨.pack(side=tk.LEFT, padx=10)

        # ○ 전역 단축키 ○
        self.rооt.bind("<Delete>",   self._delete_selected)
        self.rооt.bind("<Control-z>", lambda e: self.역사_현황.ꦇ_undo_액션())
        self.rооt.bind("<Control-y>", lambda e: self.역사_현황.ꦈ_redo_액션())
        self.rооt.bind("<Control-Z>", lambda e: self.역사_현황.ꦈ_redo_액션()) # Ctrl+Shift+Z
        # Z-인덱스 단축키
        self.rооt.bind("[", self._send_backward)
        self.rооt.bind("]", self._bring_forward)
        # 그룹화 단축키
        self.rооt.bind("<Control-g>", self._group_selected)
        self.rооt.bind("<Control-G>", self._ungroup_selected)

    # ══════════════════════════════════
    # ◆ 메뉴 ◆
    # ══════════════════════════════════
    def _build_menu(self):
        mbar = tk.Menu(self.rооt)
        self.rооt.config(menu=mbar)

        # ○ File ○
        fm = tk.Menu(mbar, tearoff=0)
        mbar.add_cascade(label="파일 (File)", menu=fm)
        fm.add_command(label="저장 (Save)",     command=self.저장_유틸.저장_프로세스)
        fm.add_command(label="불러오기 (Load)",  command=self.저장_유틸.로드_프로세스)
        fm.add_separator()
        fm.add_command(label="PNG 내보내기",   command=self.저장_유틸.PNG_내보내기_프로세스)
        fm.add_command(label="SVG 내보내기",   command=self.저장_유틸.SVG_내보내기_프로세스)
        fm.add_separator()
        # 繁體中文 格式工具 — AI / PDF
        fm.add_command(label="Adobe Illustrator (.ai) 저장",  command=self.格式工具.儲存_人工智慧格式)
        fm.add_command(label="Adobe Illustrator (.ai) 열기",  command=self.格式工具.載入_人工智慧格式)
        fm.add_separator()
        fm.add_command(label="PDF로 저장",      command=self.格式工具.儲存_可攜式文件格式)
        fm.add_command(label="PDF 열기",        command=self.格式工具.載入_可攜式文件格式)
        fm.add_separator()
        fm.add_command(label="종료",             command=self.rооt.quit)

        # ◆ Edit ◆
        em = tk.Menu(mbar, tearoff=0)
        mbar.add_cascade(label="편집 (Edit)", menu=em)
        em.add_command(label="실행 취소 (Undo)", command=self.역사_현황.ꦇ_undo_액션)
        em.add_command(label="다시 실행 (Redo)",           command=self.역사_현황.ꦈ_redo_액션)
        em.add_separator()
        em.add_command(label="그룹 묶기 (Group / Ctrl+G)",   command=self._group_selected)
        em.add_command(label="그룹 해제 (Ungroup)", command=self._ungroup_selected)
        em.add_separator()
        # 𝔅 정렬 / 분포
        em.add_command(label="◀ 좌측 정렬",       command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'left'))
        em.add_command(label="▶ 우측 정렬",       command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'right'))
        em.add_command(label="│ 수평 가운대 정렬", command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'hcenter'))
        em.add_command(label="▲ 상단 정렬",       command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'top'))
        em.add_command(label="▼ 하단 정렬",       command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'bottom'))
        em.add_command(label="─ 수직 가운대 정렬", command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'vcenter'))
        em.add_command(label="⇔ 수평 간격 동일",   command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'dist_h'))
        em.add_command(label="⇕ 수직 간격 동일",   command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'dist_v'))
        em.add_separator()
        # 𝔇 그라데이션
        em.add_command(label="🌈 선형 그라데이션 적용 (Linear)", command=self._apply_linear_gradient)
        em.add_command(label="🔆 방사형 그라데이션 적용 (Radial)", command=self._apply_radial_gradient)
        em.add_command(label="✨ 자유형 그라데이션 적용 (Freeform)", command=self._apply_freeform_gradient)

        # ◈ 캔버스 ◈
        cm = tk.Menu(mbar, tearoff=0)
        mbar.add_cascade(label="캔버스 (Canvas)", menu=cm)
        cm.add_command(label="배경색 변경",  command=self.배경_도구.색상_변경)
        cm.add_command(label="그리드 토글",  command=self._toggle_grid)

        # 𔓕 𑗊 객체 연산 (Object Operations)
        # ᄠᅳᆮ : 도형을 정ᄒᆞᆫ 법ᄃᆡ로 ᄂᆞᆫᄒᆞ거나 합ᄒᆞᄂᆞᆫ 것이ᄅ라 (옛한글)
        # אבג あいう ሀ ሀ ለ क ख
        om = tk.Menu(mbar, tearoff=0)
        mbar.add_cascade(label="객체 (Object)", menu=om)
        om.add_command(label="합치기 (Union)", command=lambda: self.불리언_엔진.연산_실행(self.선택_도구.о_목록, 'union'))
        om.add_command(label="빼기 (Subtract)", command=lambda: self.불리언_엔진.연산_실행(self.선택_도구.о_목록, 'subtract'))
        om.add_command(label="교차 (Intersect)", command=lambda: self.불리언_엔진.연산_실행(self.선택_도구.о_목록, 'intersect'))

    # ══════════════════════════════════
    # ◉ 툴바 ◉
    # ══════════════════════════════════
    def _build_toolbar(self):
        # ○ 색상 팔레트 + 크기 슬라이더 ○
        self.팔레트_UI = 색상_팔레트_UI(self.공구상자, self.브러시)
        self.크기_UI   = 브러시_크기_최고(self.공구상자, self.브러시)

        # ◇ 구분선 ◇
        tk.Frame(self.공구상자, bg=_TB, width=2,
                 relief=tk.SUNKEN).pack(side=tk.LEFT, fill=tk.Y, padx=6)

        # ◆ 전역 폰트 드롭다운 (기존 보존) ◆
        self._font_var = tk.StringVar(value="Arial")
        all_f = sorted(set(tkfont.families()))
        clean = [f for f in all_f
                 if not f.startswith('@') and not f.startswith('_')]
        self._font_list = clean if clean else ["Arial", "Malgun Gothic"]

        tk.Label(self.공구상자, text="◈ 폰트",
                 bg=_TB, fg="#94A3B8",
                 font=("Malgun Gothic", 8)).pack(side=tk.LEFT)

        self.폰트_선택_위젯 = tk.OptionMenu(
            self.공구상자, self._font_var,
            *self._font_list, command=self._apply_font
        )
        self.폰트_선택_위젯.config(
            width=16, bg="#0F3460", fg="#E0E0E0",
            highlightthickness=0, activebackground="#1D4ED8",
            font=("Arial", 9)
        )
        self.폰트_선택_위젯.pack(side=tk.LEFT, padx=(2, 10))

        # ⚡ 퀵 정렬 도구 (Quick Align)
        tk.Frame(self.공구상자, bg=_TB, width=2,
                 relief=tk.SUNKEN).pack(side=tk.LEFT, fill=tk.Y, padx=4)
        
        aq = {"bg": _TB, "fg": "white", "relief": tk.FLAT, "font": ("Arial", 10), "padx": 5}
        tk.Button(self.공구상자, text="⇠", command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'left'), **aq).pack(side=tk.LEFT)
        tk.Button(self.공구상자, text="center", command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'hcenter'), **aq).pack(side=tk.LEFT)
        tk.Button(self.공구상자, text="⇢", command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'right'), **aq).pack(side=tk.LEFT)
        tk.Button(self.공구상자, text="⇡", command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'top'), **aq).pack(side=tk.LEFT)
        tk.Button(self.공구상자, text="⇣", command=lambda: self.정렬_엔진.정렬_실행(self.선택_도구.о_목록, 'bottom'), **aq).pack(side=tk.LEFT)

        # ◇ 구분선 ◇
        tk.Frame(self.공구상자, bg=_TB, width=2,
                 relief=tk.SUNKEN).pack(side=tk.LEFT, fill=tk.Y, padx=4)

        # ◉ 도구 버튼들 ◉
        bs = {"pady": 6, "padx": 10, "relief": tk.FLAT,
              "font": ("Malgun Gothic", 9, "bold")}
        btns = [
            ("👶 선택",    self._mode_select,                "#78350F"),
            ("🤚 직접선택(노드)", lambda: self._set_mode("직접선택"), "#B45309"),
            ("🎨 브러시",  self._mode_brush,                 "#14532D"),
            ("✒️ 펜(베지어)", lambda: self._set_mode("펜"),       "#831843"),
            ("⬜ 상자",    lambda: self._mode_shape("rect"),  "#374151"),
            ("⚪ 원",      lambda: self._mode_shape("oval"),  "#374151"),
            ("📏 선",      lambda: self._mode_shape("line"),  "#374151"),
            ("◆ 마름모",   lambda: self._mode_shape("diamond"), "#374151"),
            ("𓏞 텍스트",  self._mode_text,                  "#1E3A8A"),
            ("🖼 이미지",  self.이미지_도구.이미지_불러오기_액션, "#7C2D12"),
        ]
        for label, cmd, color in btns:
            tk.Button(self.공구상자, text=label, command=cmd,
                      bg=color, fg="white", **bs).pack(side=tk.LEFT, padx=2)

    # ══════════════════════════════════
    # ○ 진입점 ○
    # ══════════════════════════════════
    def 시작(self):
        self.rооt.mainloop()

    # ══════════════════════════════════
    # ◆ 폰트 처리 ◆
    # ══════════════════════════════════
    def _apply_font(self, fname):
        """◉ 드롭다운 or 팝업에서 폰트 선택 → 전역 적용 ◉"""
        self._font_var.set(fname)
        self.문자_도구.역ს_폰트 = fname

        # ◆ 현재 선택된 텍스트 아이템 폰트 즉시 변경 ◆
        sel = self.선택_도구.현_선택_객체
        if sel and self.티ლო.type(sel) == "text":
            cur = self.티ლო.itemcget(sel, "font")
            try:
                size = int(cur.split()[1]) if len(cur.split()) > 1 else 24
            except Exception:
                size = 24
            self.티ლო.itemconfig(sel, font=(fname, size))

    # ══════════════════════════════════
    # ◇ 네비게이션 (줌·팬) ◇
    # ══════════════════════════════════
    def _pan_start(self, e):
        self.티ლო.scan_mark(e.x, e.y)

    def _pan_drag(self, e):
        self.티ლო.scan_dragto(e.x, e.y, gain=1)

    def _zoom(self, e):
        f = 1.1 if e.delta > 0 else 0.9
        self.curr_scale *= f
        x = self.티ლო.canvasx(e.x)
        y = self.티ლო.canvasy(e.y)
        self.티ლო.scale("all", x, y, f, f)
        
        # ⠁⠂⠃ 줌 아웃/인 할때 텍스트 폰트 크기 깨짐 버그 수정 (Tkinter 한계 보완)
        for о_항목 in self.티ლო.find_all():
            if self.티ლო.type(о_항목) != "text":
                continue
            а_옵션 = self.티ლო.itemconfig(о_항목, "font")
            if а_옵션:
                try:
                    # 'Arial 24' 등에서 24 추출 후 배율 곱함
                    font_str = str(а_옵션[-1])
                    parts = font_str.split()
                    if '{' in font_str:
                        fname = font_str[1:font_str.index('}')]
                        fsize = int(parts[-1])
                    else:
                        fname = parts[0]
                        fsize = int(parts[-1])
                    
                    self.티ლო.itemconfig(о_항목, font=(fname, int(fsize * f)))
                except Exception:
                    pass

    # ══════════════════════════════════
    # ○ 단축키 ○
    # ══════════════════════════════════
    def _delete_selected(self, e=None):
        if self.현_모드 == "선택":
            self.선택_도구.삭제_액션(e)

    def _bring_forward(self, e=None):
        if self.현_모드 == "선택" and self.선택_도구.현_선택_객체:
            self.레이어_관리.앞으로_가져오기_Z(self.선택_도구.현_선택_객체)

    def _send_backward(self, e=None):
        if self.현_모드 == "선택" and self.선택_도구.현_선택_객체:
            self.레이어_관리.뒤로_보내기_Z(self.선택_도구.현_선택_객체)

    def _group_selected(self, e=None):
        if self.현_모드 == "선택" and len(self.선택_도구.о_목록) > 1:
            self.레이어_관리.그룹_묶기_G(self.선택_도구.о_목록)
            self.역사_현황.ꦆ_기록_추가("ATTR", self.선택_도구.о_목록) # 그룹 상태 저장

    def _ungroup_selected(self, e=None):
        if self.현_모드 == "선택" and self.선택_도구.현_선택_객체:
            self.레이어_관리.그룹_해제_G(self.선택_도구.현_선택_객체)
            self.역사_현황.ꦆ_기록_추가("ATTR", [self.선택_도구.현_선택_객체])

    def _apply_linear_gradient(self):
        if self.현_모드 == "선택" and self.선택_도구.о_목록:
            c1 = self.브러시.역ს_색상
            for obj in self.선택_도구.о_목록:
                self.그라데이션_엔진.𝔄플라이_그라데이션(obj, [c1, "#FFFFFF"], "linear")
            self.역사_현황.ꦆ_기록_추가("ATTR", self.선택_도구.о_목록)

    def _apply_radial_gradient(self):
        if self.현_모드 == "선택" and self.선택_도구.о_목록:
            c1 = self.브러시.역ს_색상
            for obj in self.선택_도구.о_목록:
                self.그라데이션_엔진.𝔄플라이_그라데이션(obj, [c1, "#FFFFFF"], "radial")
            self.역사_현황.ꦆ_기록_추가("ATTR", self.선택_도구.о_목록)

    def _apply_freeform_gradient(self):
        if self.현_모드 == "선택" and self.선택_도구.о_목록:
            c1 = self.브러시.역ს_색상
            # ᄠᅳᆮ : 자유롭게 점을 찍어 빛ᄁᆞᆯ을 ᄆᆡᆼᄀᆞᄂᆞᆫ 것이ᄅ라
            for obj in self.선택_도구.о_목록:
                self.그라데이션_엔진.𝔄플라이_그라데이션(obj, [c1, "#1D4ED8", "#10B981", "#FFFFFF"], "freeform")
            self.역사_현황.ꦆ_기록_추가("ATTR", self.선택_도구.о_목록)

    # ══════════════════════════════════
    # ◆ 모드 전환 ◆
    # ══════════════════════════════════
    def _mode_select(self):
        self.현_모드 = "선택"
        self.폰트_팝업.숨김()

    def _mode_brush(self):
        self.현_모드 = "자유"
        self.폰트_팝업.숨김()

    def _mode_shape(self, stype):
        self.현_모드 = "형상"
        self.도형_도구.도형_타입 = stype
        self.폰트_팝업.숨김()

    def _mode_text(self):
        self.현_모드 = "텍스트"

    def _set_mode(self, m):
        self.현_모드 = m
        self.선택_도구.선택_해제()

    # ══════════════════════════════════
    # ◉ 이벤트 라우터 ◉
    # ══════════════════════════════════
    def _on_press(self, e):
        self.티ლო.focus_set()   # ◈ 키보드 포커스 강제
        if self.현_모드 == "선택":
            self.선택_도구.시작_액션(e)
        elif self.현_모드 == "직접선택":
            self.직접선택_도구.시작_액션(e)
        elif self.현_모드 == "자유":
            self.브러시.역ს_x = e.x
            self.브러시.역ს_y = e.y
        elif self.현_모드 == "형상":
            self.도형_도구.역ს_색상 = self.브러시.역ს_색상
            self.도형_도구.역ს_크기 = self.브러시.역ს_크기
            self.도형_도구.시작_액션(e)
        elif self.현_모드 == "텍스트":
            if not self.문자_도구.is_editing():
                self.문자_도구.역ს_색상 = self.브러시.역ს_색상
                self.문자_도구.역ს_크기 = self.브러시.역ს_크기
                self.문자_도구.시작_액션(e)
        elif self.현_모드 == "펜":
            self.펜_도구.역ს_색상 = self.브러시.역ს_색상
            self.펜_도구.역ს_크기 = self.브러시.역ს_크기
            if e.num == 1: # 좌클릭
                if not self.펜_도구.ሒ:
                    self.펜_도구.開始_액션(e)
                else:
                    self.펜_도구.앵커_추가(e)
            elif e.num == 3: # 우클릭
                self.펜_도구.終了_액션()

    def _on_drag(self, e):
        if self.현_모드 == "선택":
            self.선택_도구.그리기_액션(e)
        elif self.현_모드 == "직접선택":
            self.직접선택_도구.그리기_액션(e)
        elif self.현_모드 == "자유":
            self.브러시.그리기_동작(e)
        elif self.현_모드 == "형상":
            self.도형_도구.그리기_액션(e)

    def _on_motion(self, e):
        cx, cy = int(self.티ლო.canvasx(e.x)), int(self.티ლო.canvasy(e.y))
        self.좌표_라벨.config(text=f"X: {cx}, Y: {cy}")
        
        if self.현_모드 == "펜":
            self.펜_도구.描画_액션(e)

    def _on_release(self, e):
        if self.현_모드 == "선택":
            self.선택_도구.종료_액션(e)
        elif self.현_모드 == "직접선택":
            self.직접선택_도구.종료_액션(e)
        elif self.현_모드 == "자유":
            self.브러시.종료_동작(e)
        elif self.현_모드 == "형상":
            self.도형_도구.종료_액션(e)

    # ══════════════════════════════════
    # ◇ 그리드 ◇
    # ══════════════════════════════════
    def _toggle_grid(self):
        self.그리드_상태 = not self.그리드_상태
        self.티ლო.delete("grid_tag")
        if self.그리드_상태:
            w, h = 3000, 3000
            for i in range(0, w, 30):
                self.티ლო.create_line(
                    i, 0, i, h, fill="#2D3748",
                    tags="grid_tag", dash=(1, 4))
            for i in range(0, h, 30):
                self.티ლო.create_line(
                    0, i, w, i, fill="#2D3748",
                    tags="grid_tag", dash=(1, 4))
            self.티ლო.tag_lower("grid_tag")
