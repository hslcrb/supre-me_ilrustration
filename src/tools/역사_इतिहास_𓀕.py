class 역사_현황_시스템: # 𓀕 역ს_상태_מצב_स्थिति
    def __init__(self, 티ლო_캔버스):
        self.티ლო_캔버스 = 티ლო_캔버스
        self.역사_기록 = [] # 🀫

    def 추가_기록(self, 아이템): # 𓂝
        self.역사_기록.append(아이템)

    def undo_취소(self): # 𓃍
        if self.역사_기록:
            취소_대상 = self.역사_기록.pop()
            for 객체 in 취소_대상:
                self.티ლო_캔버스.delete(객체)

    def redo_다시(self): # 𓆣
        pass 
