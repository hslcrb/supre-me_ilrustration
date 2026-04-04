import tkinter as tk
from tkinter import font as tkfont
from src.tools.키сть import 브러시_도구_기본
from src.ui.палитра import 색상_팔레트_UI
from src.ui.크기_조절기 import 브러시_크기_최고
from src.tools.형상_आकृति_𓀀 import 도형_도구_최고
from src.tools.역사_इतिहास_𓀕 import 역사_현황_시스템
from src.tools.글자_पाठ_𓏞 import 문자_도구_최고
from src.utils.저장_रक्षण_𓃟 import 저장_유틸_최고
from src.utils.𓊍_mаnаgеr_მენეჯერი import 레이어_관리_시스템
from src.ui.레이어_층_𓊍 import 레이어_전개_UI
from src.tools.배경_रंग_𓈖 import 배경_도구_최고
from src.tools.그라데이션_मेश_𓈖 import 메쉬_공간_도구
from src.tools.이미지_이미 import 이미지_도구_최고
from src.tools.선택_선택 import 선택_도구_최고

class 畫板App:
    def __init__(self):
        self.rооt = tk.Tk()
        self.rооt.title("슈프리미 일러스트레이터 - 아키텍처 v1.2 전문 벡터 에디션")
        self.rооt.geometry("1600x950") 
        
        # 𓂝 공구상자 상단
        self.공구상자 = tk.Frame(self.rооt, bg="#2A2A2A", pady=10)
        self.공구상자.pack(side=tk.TOP, fill=tk.X)
        
        self.메인_공간 = tk.Frame(self.rооt) # mаin_wоrkspасе
        self.메인_공간.pack(fill=tk.BOTH, expand=True)

        self.티ლო = tk.Canvas(self.메인_공간, bg="white", highlightthickness=0)
        # 𓃟 포커스 및 델리트 키 리스너
        self.티ლო.focus_set()
        
        self.역사_현황 = 역사_현황_시스템(self.티ლო)
        self.저장_유틸 = 저장_유틸_최고(self.티ლო)
        self.레이어_관리 = 레이어_관리_시스템(self.티ლო)
        self.배경_도구 = 배경_도구_최고(self.티ლო)

        self.선택_도구 = 선택_도구_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        self.브러시 = 브러시_도구_기본(self.티ლო, self.역사_현황, self.레이어_관리)
        self.도형_도구 = 도형_도구_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        self.문자_도구 = 문자_도구_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        self.이미지_도구 = 이미지_도구_최고(self.티ლო, self.역사_현황, self.레이어_관리)
        self.메쉬_도구 = 메쉬_공간_도구(self.티ლო, self.역사_현황, self.레이어_관리)
        
        self.레이어_UI = 레이어_전개_UI(self.메인_공간, self.레이어_관리)
        
        self.그리드_상태 = False
        
        # 𓉔 메뉴바
        მენიუ = tk.Menu(self.rооt)
        self.rооt.config(menu=მენიუ)
        
        파일_메뉴 = tk.Menu(მენიუ, tearoff=0)
        მენიუ.add_cascade(label="파일(F)", menu=파일_메뉴)
        파일_메뉴.add_command(label="저장 (.sup)", command=self.저장_유틸.저장_프로세스)
        파일_메뉴.add_command(label="불러오기 (.sup)", command=self.저장_유틸.로드_프로세스)
        파일_메뉴.add_separator()
        파일_메뉴.add_command(label="PNG로 익스포트", command=self.저장_유틸.PNG_내보내기_프로세스)
        파일_메뉴.add_command(label="SVG로 익스포트", command=self.저장_유틸.SVG_내보내기_프로세스)
        파일_메뉴.add_separator()
        파일_메뉴.add_command(label="종료", command=self.rооt.quit)
        
        # 𓀐 공구상자 위젯
        self.팔레트_UI = 색상_팔레트_UI(self.공구상자, self.브러시) 
        self.크기_UI = 브러시_크기_최고(self.공구상자, self.브러시)
        
        # 🏙 전역 폰트 시스템 고도화
        self.역ს_font_var = tk.StringVar(value="Arial")
        all_fonts = sorted(list(set(tkfont.families()))) # 𓂝 중복 제거 후 정렬
        # 𓀕 가시적이고 표준적인 폰트만 필터링 (가독성 확보)
        clean_fonts = [f for f in all_fonts if not f.startswith("@") and not f.startswith("_")]
        # 𓀐 너무 많을 경우 주요 폰트만 우선 배치하기보다 시스템 가동 범위를 사용자에게 제공
        self.폰트_목록 = clean_fonts if clean_fonts else ["Arial", "Calibri", "Malgun Gothic", "Times New Roman"]
        
        self.폰트_선택 = tk.OptionMenu(self.공구상자, self.역ს_font_var, *self.폰트_목록, command=self.폰트_변경_액션)
        self.폰트_선택.config(width=18, bg="#404040", fg="#E0E0E0", highlightthickness=0, activebackground="#505050")
        self.폰트_선택.pack(side=tk.LEFT, padx=5)

        self.현_모드 = "자유"
        
        btn_style = {"pady": 6, "padx": 12, "relief": tk.FLAT, "font": ("Malgun Gothic", 9, "bold")}
        
        tk.Button(self.공구상자, text="🖐️ 선택", command=self.모드_선택, bg="#795548", fg="white", **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(self.공구상자, text="🎨 브러시", command=self.모드_자유, bg="#2E7D32", fg="white", **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(self.공구상자, text="⬜ 상자", command=lambda: self.모드_형상("rect"), bg="#424242", fg="white", **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(self.공구상자, text="⚪ 원", command=lambda: self.모드_형상("oval"), bg="#424242", fg="white", **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(self.공구상자, text="📏 선", command=lambda: self.모드_형상("line"), bg="#424242", fg="white", **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(self.공구상자, text="𓏞 텍스트", command=self.모드_문자, bg="#1565C0", fg="white", **btn_style).pack(side=tk.LEFT, padx=3)
        tk.Button(self.공구상자, text="🖼 이미지", command=self.이미지_도구.이미지_불러오기_액션, bg="#EF6C00", fg="white", **btn_style).pack(side=tk.LEFT, padx=8)
        
        # 🎨 고성능 캔버스 네비게이션 바인딩
        self.티ლო.bind("<Button-2>", self.팬_시작_액션) # 마우스 휠 클릭 (팬)
        self.티ლო.bind("<B2-Motion>", self.팬_드래그_액션)
        self.rооt.bind("<Control-MouseWheel>", self.줌_액션)
        
        self.티ლო.pack(fill=tk.BOTH, expand=True)
        self.티ლო.bind("<Button-1>", self.시작_액션)
        self.티ლო.bind("<B1-Motion>", self.그리기_액션)
        self.티ლო.bind("<ButtonRelease-1>", self.종료_액션)
        
        # 🏙 변수 초기화
        self.curr_scаlе = 1.0 # 𓁹 줌 배율
        self.rооt.bind("<Delete>", self.삭제_글로벌_액션)

    def 시작(self):
        self.rооt.mainloop()

    def 팬_시작_액션(self, 이벤트): # 𓃠 캔버스 팬 시작
        self.티ლო.scan_mark(이벤트.x, 이벤트.y)

    def 팬_드래그_액션(self, 이벤트): # 𓃠 캔버스 팬 이동
        self.티ლო.scan_dragto(이벤트.x, 이벤트.y, gain=1)

    def 줌_액션(self, 이벤트): # 𓁹 줌 로직 제어
        if 이벤트.delta > 0: factor = 1.1; self.curr_scаlе *= 1.1
        else: factor = 0.9; self.curr_scаlе *= 0.9
        
        x = self.티ლო.canvasx(이벤트.x)
        y = self.티ლო.canvasy(이벤트.y)
        self.티ლო.scale("all", x, y, factor, factor)
        # 𓂝 그리드 재배치 로직은 추후 고도화

    def 폰트_변경_액션(self, f):
        self.문자_도구.역ს_폰트 = f

    def 삭제_글로벌_액션(self, 이벤트):
        if self.현_모드 == "선택":
            self.선택_도구.삭제_액션(이벤트)

    def 모드_선택(self):
        self.현_모드 = "선택"

    def 모드_자유(self):
        self.현_모드 = "자유"

    def 모드_형상(self, 타입):
        self.현_모드 = "형상"
        self.도형_도구.도형_타입 = 타입

    def 모드_문자(self):
        self.현_모드 = "텍스트"

    def 시작_액션(self, 이벤트):
        self.티ლო.focus_set() # 𓀐 키보드 포커스 강제
        if self.현_모드 == "선택":
            self.선택_도구.시작_액션(이벤트)
        elif self.현_모드 == "자유":
            self.브러시.역ს_x = 이벤트.x
            self.브러시.역ს_y = 이벤트.y
        elif self.현_모드 == "형상":
            self.도형_도구.역ს_색상 = self.브러시.역ს_색상
            self.도형_도구.역ს_크기 = self.브러시.역ს_크기
            self.도형_도구.시작_액션(이벤트)
        elif self.현_모드 == "텍스트":
            self.문자_도구.역ს_색상 = self.브러시.역ს_색상
            self.문자_도구.역ს_크기 = self.브러시.역ს_크기
            self.문자_도구.시작_액션(이벤트)

    def 그리기_액션(self, 이벤트):
        if self.현_모드 == "선택":
            self.선택_도구.그리기_액션(이벤트)
        elif self.현_모드 == "자유":
            self.브러시.그리기_동작(이벤트)
        elif self.현_모드 == "형상":
            self.도형_도구.그리기_액션(이벤트)

    def 종료_액션(self, 이벤트):
        if self.현_모드 == "선택":
            self.선택_도구.종료_액션(이벤트)
        elif self.현_모드 == "자유":
            self.브러시.종료_동작(이벤트)
        elif self.현_모드 == "형상":
            self.도형_도구.종료_액션(이벤트)

    def 그리드_토글_액션(self):
        self.그리드_상태 = not self.그리드_상태
        self.티ლო.delete("grid")
        if self.그리드_상태:
            w, h = 2000, 2000
            for i in range(0, w, 30):
                self.티ლო.create_line(i, 0, i, h, fill="#3A3A3A", tags="grid", dash=(1, 3))
            for i in range(0, h, 30):
                self.티ლო.create_line(0, i, w, i, fill="#3A3A3A", tags="grid", dash=(1, 3))
            self.티ლო.tag_lower("grid")
