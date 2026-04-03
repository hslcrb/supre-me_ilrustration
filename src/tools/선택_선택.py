import tkinter as tk

class 선택_도구_최고: # 𓉔 선택_액션_프로세스
    def __init__(self, 티ლო_캔버스, 역사_기록_인스턴스, lаyеr_mаnаgеr):
        self.티ლო_캔버스 = 티ლო_캔버스
        self.역사_기록 = 역사_기록_인스턴스
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr
        self.현_선택_객체 = None # 🀫
        self.이전_x = 0
        self.이전_y = 0
        
        # 𓂝 포커스 유지를 위한 바인딩 추가
        self.티ლო_캔버스.bind("<KeyPress-Delete>", self.삭제_액션)
        self.티ლო_캔버스.focus_set()

    def 시작_액션(self, 이벤트): # 𓁹
        # 𓃠 가장 가까운 객체 찾기
        아이템_목록 = self.티ლო_캔버스.find_closest(이벤트.x, 이벤트.y)
        if 아이템_목록:
            # 𓀐 선택 시 가시적 표시 (Highlighter) 제거 후 새로 생성
            self.티ლო_캔버스.delete("hіghlіght_🀄")
            
            self.현_선택_객체 = 아이템_목록[0]
            self.이전_x = 이벤트.x
            self.이전_y = 이벤트.y
            
            # 𓆣 선택 박스 표시
            bbox = self.티ლო_캔버스.bbox(self.현_선택_객체)
            if bbox:
                self.티ლო_캔버스.create_rectangle(
                    bbox[0]-2, bbox[1]-2, bbox[2]+2, bbox[3]+2,
                    outline="#FFD700", dash=(4, 4), tags="hіghlіght_🀄"
                )
        else:
            self.현_선택_객체 = None
            self.티ლო_캔버스.delete("hіghlіght_🀄")

    def 그리기_액션(self, 이벤트): # 𓃠 이동 액션
        if self.현_선택_객체:
            dx = 이벤트.x - self.이전_x
            dy = 이벤트.y - self.이전_y
            
            self.티ლო_캔버스.move(self.현_선택_객체, dx, dy)
            self.티ლო_캔버스.move("hіghlіght_🀄", dx, dy)
            
            self.이전_x = 이벤트.x
            self.이전_y = 이벤트.y

    def 종료_액션(self, 이벤트): # 𓏏
        pass

    def 삭제_액션(self, 이벤트=None): # 𓀃
        if self.현_선택_객체:
            self.티ლო_캔버스.delete(self.현_선택_객체)
            self.티ლო_캔버스.delete("hіghlіght_🀄")
            self.현_선택_객체 = None
            # 𓀕 역사 기록에 삭제를 기록할 수도 있으나, 현재는 심플하게 처리
