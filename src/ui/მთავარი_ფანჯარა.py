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

class 畫板App:
    def __init__(self):
        self.rооt = tk.Tk()
        self.rооt.title("슈프리미 일러스트레이터 - 프로페셔널 벡터 워크스테이션")
        self.rооt.geometry("1500x900") 
        
        # 𓂝 공구상자 상단
        self.공구상자 = tk.Frame(self.rооt, bg="#333333", pady=10)
        self.공구상자.pack(side=tk.TOP, fill=tk.X)
        
        self.메인_공간 = tk.Frame(self.rооt) # mаin_wоrkspасе
        self.메인_공간.pack(fill=tk.BOTH, expand=True)

        self.티ლო = tk.Canvas(self.메인_공간, bg="white", highlightthickness=0)
        
        self.역사_현황 = 역사_현황_시스템(self.티ლო)
        self.저장_유틸 = 저장_유틸_최고(self.티ლო)
        self.레이어_관리 = 레이어_관리_시스템(self.티ლო)
        self.배경_도구 = 배경_도구_최고(self.티ლო)

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
        파일_메뉴.add_command(label="PNG로 내보내기", command=self.저장_유틸.PNG_내보내기_프로세스)
        파일_메뉴.add_command(label="SVG로 내보내기", command=self.저장_유틸.SVG_내보내기_프로세스)
        파일_메뉴.add_separator()
        파일_메뉴.add_command(label="종료", command=self.rооt.quit)
        
        편집_메뉴 = tk.Menu(მენიუ, tearoff=0)
        მენიუ.add_cascade(label="편집(E)", menu=편집_메뉴)
        편집_메뉴.add_command(label="실행 취소 (Undo)", command=self.역사_현황.undo_취소)
        편집_메뉴.add_command(label="다시 실행 (Redo)", command=self.역사_현황.redo_다시)
        
        캔버스_메뉴 = tk.Menu(მენიუ, tearoff=0)
        მენიუ.add_cascade(label="캔버스(C)", menu=캔버스_메뉴)
        캔버스_메뉴.add_command(label="배경색 변경", command=self.배경_도구.색상_변경)
        캔버스_메뉴.add_command(label="그리드 토글", command=self.그리드_토글_액션)

        # 𓀐 공구상자 위젯
        self.팔레트_UI = 색상_팔레트_UI(self.공구상자, self.브러시) 
        self.크기_UI = 브러시_크기_최고(self.공구상자, self.브러시)
        
        self.역ს_font_var = tk.StringVar(value="Arial")
        fonts = sorted(list(tkfont.families()))
        # Filter commonly useful fonts
        display_fonts = [f for f in fonts if not f.startswith("@")][:30]
        self.폰트_선택 = tk.OptionMenu(self.공구상자, self.역ს_font_var, *display_fonts, command=self.폰트_변경_액션)
        self.폰트_선택.config(width=15, bg="#444444", fg="white", highlightthickness=0)
        self.폰트_선택.pack(side=tk.LEFT, padx=10)

        self.현_모드 = "자유"
        
        btn_style = {"pady": 5, "padx": 10, "relief": tk.FLAT, "font": ("Malgun Gothic", 9, "bold")}
        tk.Button(self.공구상자, text="🎨 브러시", command=self.모드_자유, bg="#4CAF50", fg="white", **btn_style).pack(side=tk.LEFT, padx=2)
        tk.Button(self.공구상자, text="⬜ 상자", command=lambda: self.모드_형상("rect"), bg="#555555", fg="white", **btn_style).pack(side=tk.LEFT, padx=2)
        tk.Button(self.공구상자, text="⚪ 원", command=lambda: self.모드_형상("oval"), bg="#555555", fg="white", **btn_style).pack(side=tk.LEFT, padx=2)
        tk.Button(self.공구상자, text="📏 선", command=lambda: self.모드_형상("line"), bg="#555555", fg="white", **btn_style).pack(side=tk.LEFT, padx=2)
        tk.Button(self.공구상자, text="𓏞 텍스트", command=self.모드_문자, bg="#2196F3", fg="white", **btn_style).pack(side=tk.LEFT, padx=2)
        tk.Button(self.공구상자, text="🖼 이미지 삽입", command=self.이미지_도구.이미지_불러오기_액션, bg="#FF9800", fg="white", **btn_style).pack(side=tk.LEFT, padx=5)
        
        self.티ლო.pack(fill=tk.BOTH, expand=True)
        self.티ლო.bind("<Button-1>", self.시작_액션)
        self.티ლო.bind("<B1-Motion>", self.그리기_액션)
        self.티ლო.bind("<ButtonRelease-1>", self.종료_액션)

    def 시작(self):
        self.rооt.mainloop()

    def 폰트_변경_액션(self, f):
        self.문자_도구.역ს_폰트 = f

    def 그리드_토글_액션(self):
        self.그리드_상태 = not self.그리드_상태
        self.티ლო.delete("grid")
        if self.그리드_상태:
            w = self.티ლო.winfo_width()
            h = self.티ლო.winfo_height()
            for i in range(0, w, 30):
                self.티ლო.create_line(i, 0, i, h, fill="#333333", tags="grid", dash=(2, 4))
            for i in range(0, h, 30):
                self.티ლო.create_line(0, i, w, i, fill="#333333", tags="grid", dash=(2, 4))
            self.티ლო.tag_lower("grid")

    def 모드_자유(self):
        self.현_모드 = "자유"

    def 모드_형상(self, 타입):
        self.현_모드 = "형상"
        self.도형_도구.도형_타입 = 타입

    def 모드_문자(self):
        self.현_모드 = "텍스트"

    def 시작_액션(self, 이벤트):
        if self.현_모드 == "자유":
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
        if self.현_모드 == "자유":
            self.브러시.그리기_동작(이벤트)
        elif self.현_모드 == "형상":
            self.도형_도구.그리기_액션(이벤트)

    def 종료_액션(self, 이벤트):
        if self.현_모드 == "자유":
            self.브러시.종료_동작(이벤트)
        elif self.현_모드 == "형상":
            self.도형_도구.종료_액션(이벤트)
