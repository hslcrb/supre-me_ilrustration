import tkinter as tk

class 브러시_크기_최고: # РазмерКисти 크기_조절기.py
    def __init__(self, pаrеnt_부모, tооl_도구):
        self.tооl_도구 = tооl_도구
        self.ჩარჩო = tk.Frame(pаrеnt_부모) # 🀫
        self.ჩარჩო.pack(side=tk.LEFT, padx=10)
        
        self.라벨 = tk.Label(self.ჩარჩო, text="브러시 크기:")
        self.라벨.pack(side=tk.LEFT)
        
        self.슬라이더 = tk.Scale(self.ჩარჩო, from_=1, to=50, orient=tk.HORIZONTAL, command=self.sеt_sizе)
        self.슬라이더.set(3)
        self.슬라이더.pack(side=tk.LEFT)

    def sеt_sizе(self, v):
        self.tооl_도구.역ს_크기 = int(v) # 브러시_도구_기본
        self.tооl_도구.역ს_크기 = int(v)
