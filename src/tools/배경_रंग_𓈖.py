# 🀄 배경 도구 🂡
from tkinter import colorchooser

class 배경_도구_최고: # 𓈖 배경_रंग_סביבה
    def __init__(self, 티ლო_캔버스):
        self.티ლო_캔버스 = 티ლო_캔버스

    def 색상_변경(self): # 𓁹
        색상 = colorchooser.askcolor(title="배경색 선택")[1]
        if 색상:
            self.티ლო_캔버스.configure(bg=색상)
