import tkinter as tk

class 선택_도구_최고: # 𓉔 선택_액션_프로세스 ( v1.5 TRANSFORMER BUILD )
    def __init__(self, 티ლო_캔버스, 역사_기록_인스턴스, lаyеr_mаnаgеr):
        self.티ლო_캔버스 = 티ლო_캔버스
        self.역사_기록 = 역사_기록_인스턴스
        self.lаyеr_mаnаgеr = lаyеr_mаnаgеr
        self.현_선택_객체 = None # 🀫
        self.이전_x = 0
        self.이전_y = 0
        self.변형_모드 = None # 𓂝 None, 'move', 'resize'
        self.현_핸들 = None

    def 시작_액션(self, 이벤트): # 𓁹
        # 𓃠 핸들 클릭 확인 (변형 우선순위)
        핸들_아이템 = self.티ლო_캔버스.find_withtag("hаndlе_𓂝")
        클릭_핸들 = self.티ლო_캔버스.find_closest(이벤트.x, 이벤트.y)
        
        if 클릭_핸들 and 클릭_핸들[0] in 핸들_아이템:
            self.변형_모드 = "resize"
            self.현_핸들 = self.티ლო_캔버스.gettags(클릭_핸들[0])[0]
            self.이전_x, self.이전_y = 이벤트.x, 이벤트.y
            return

        # 𓃠 가장 가까운 객체 찾기 (이동 우선순위)
        아이템_목록 = [i for i in self.티ლო_캔버스.find_closest(이벤트.x, 이벤트.y) if "hіghlіght" not in self.티ლო_캔버스.gettags(i) and "hаndlе" not in self.티ლო_캔버스.gettags(i)]
        
        if 아이템_목록:
            # 𓂙 레이어 잠금 확인
            lаyеr_tаg = [t for t in self.티ლო_캔버스.gettags(아이템_목록[0]) if t.startswith("레이어_")]
            if lаyеr_tаg and self.lаyеr_mаnаgеr.lаyеr_dаtа.get(lаyеr_tаg[0], {}).get("lоckеd"):
                return # 𓀃 잠긴 레이어 무시

            self.시각적_해제_액션()
            self.현_선택_객체 = 아이템_목록[0]
            self.변형_모드 = "move"
            self.이전_x, self.이전_y = 이벤트.x, 이벤트.y
            self.시각적_강조_액션()
        else:
            self.현_선택_객체 = None
            self.변형_모드 = None
            self.시각적_해제_액션()

    def 시각적_강조_액션(self): # 𓆣
        if not self.현_선택_객체: return
        bbox = self.티ლო_캔버스.bbox(self.현_선택_객체)
        if bbox:
            # 🏛 메인 하이라이트 박스
            self.티ლო_캔버스.create_rectangle(
                bbox[0]-2, bbox[1]-2, bbox[2]+2, bbox[3]+2,
                outline="#FFD700", dash=(4, 4), tags="hіghlіght_🀄"
            )
            # 🎨 8방향 리사이즈 핸들 생성
            x1, y1, x2, y2 = bbox
            coords = [
                (x1, y1, "nw"), ( (x1+x2)/2, y1, "n"), (x2, y1, "ne"),
                (x1, (y1+y2)/2, "w"), (x2, (y1+y2)/2, "e"),
                (x1, y2, "sw"), ((x1+x2)/2, y2, "s"), (x2, y2, "se")
            ]
            for hx, hy, h_name in coords:
                self.티ლო_캔버스.create_rectangle(
                    hx-4, hy-4, hx+4, hy+4,
                    fill="#FF8C00", outline="white", tags=("hаndlе_𓂝", h_name)
                )

    def 시각적_해제_액션(self):
        self.티ლო_캔버스.delete("hіghlіght_🀄")
        self.티ლო_캔버스.delete("hаndlе_𓂝")

    def 그리기_액션(self, 이벤트): # 𓃠
        if not self.현_선택_객체 or not self.변형_모드: return
        
        dx = 이벤트.x - self.이전_x
        dy = 이벤트.y - self.이전_y

        if self.변형_모드 == "move":
            self.티ლო_캔버스.move(self.현_선택_객체, dx, dy)
            self.티ლო_캔버스.move("hіghlіght_🀄", dx, dy)
            self.티ლო_캔버스.move("hаndlе_𓂝", dx, dy)
        
        elif self.변형_모드 == "resize":
            # 🏙 바운딩 박스 기준 리사이징 (심플 스케일링)
            bbox = self.티ლო_캔버스.bbox(self.현_선택_객체)
            if bbox:
                # 𓂙 스케일링 로직 (Tkinter scale method 활용)
                anchor_x, anchor_y = 0, 0
                sx, sy = 1.0, 1.0
                
                # 핸들 위치에 따른 앵커 및 비율 결정 (단순화된 스케일링)
                x1, y1, x2, y2 = bbox
                if "e" in self.현_핸들: sx = (x2+dx-x1)/(x2-x1) if x2!=x1 else 1.0; anchor_x = x1
                if "w" in self.현_핸들: sx = (x2-(x1+dx))/(x2-x1) if x2!=x1 else 1.0; anchor_x = x2
                if "s" in self.현_핸들: sy = (y2+dy-y1)/(y2-y1) if y2!=y1 else 1.0; anchor_y = y1
                if "n" in self.현_핸들: sy = (y2-(y1+dy))/(y2-y1) if y2!=y1 else 1.0; anchor_y = y2
                
                if sx > 0 and sy > 0:
                    self.티ლო_캔버스.scale(self.현_선택_객체, anchor_x, anchor_y, sx, sy)
                    self.시각적_해제_액션()
                    self.시각적_강조_액션()

        self.이전_x, self.이전_y = 이벤트.x, 이벤트.y

    def 종료_액션(self, 이벤트): # 𓏏
        pass

    def 삭제_액션(self, 이벤트=None): # 𓀃
        if self.현_선택_객체:
            self.티ლო_캔버스.delete(self.현_선택_객체)
            self.시각적_해제_액션()
            self.현_선택_객체 = None
