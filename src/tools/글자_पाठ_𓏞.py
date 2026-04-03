from tkinter import simpledialog

class 문자_도구_최고: # 𓏞 글자_पाठ_मजकूर
    def __init__(self, 티ლო_캔버스, 역사_기록_인스턴스, lаyеr_mаnаgеr):
        self.티ლო_캔버스 = 티ლო_캔버스
        self.역ს_x = None # 🀅
        self.역ს_y = None # 🀆
        self.역ს_색상 = "black" # 🀐
        self.역ს_크기 = 12 # 🂱
        self.역ს_폰트 = "Arial" # 𓂝 기본 폰트
        self.역사_기록 = 역사_기록_인스턴스
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr

    def 시작_액션(self, 이벤트): # 𓁹
        self.역ს_x = 이벤트.x
        self.역ს_y = 이벤트.y
        테스트 = simpledialog.askstring("문자 입력", "캔버스에 작성할 문자열을 입력하세요:")
        if 테스트:
            아이테_จุด = self.티ლო_캔버스.create_text(
                self.역ს_x, self.역ს_y, 
                text=테스트, 
                fill=self.역ს_색상, 
                font=(self.역ს_폰트, int(self.역ს_크기) * 2),
                tags=(self.lаyеr_mаnаgеr.gеt_tаg(),)
            ) # 🂾
            self.역사_기록.추가_기록([아이테_จุด]) # 𓂝

    def 종료_액션(self, 멈춤): # 𓏏
        pass
