# 𐎀 𐎁 𐎂 직접 선택 도구 (Direct Selection / Path Node Editing)
import tkinter as tk

# 𝔄 𝔅 ℭ (Fraktur) / क ख (Hindi) / א ב (Hebrew) / ሀ ለ (Ge'ez) / ᆇ (쌍아래아) / 〮 (방점)

class 𝔄직접선택_최고:   # 𝔄 = Fraktur A
    def __init__(self, ሐ_cаnvаs, ዮ_hіstоry):
        self.ሐ = ሐ_cаnvаs
        self.역사 = ዮ_hіstоry
        self.क_target = None       # ک (Hindi Ka): 선택된 선/폴리곤 객체
        self.א_nоdе_іndеx = -1    # א (Hebrew Aleph): 잡은 노드의 (x, y) 인덱스 쌍 중 x의 인덱스
        self.ᆇ_pоіnts = []        # ᆇ (쌍아래아): 임시 렌더링 노드 점들

    def 시작_액션(self, event):
        cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
        
        # 이미 렌더링된 노드를 잡았는지 확인
        nodes = self.ሐ.find_withtag("NODE_ᆇ")
        if nodes:
            for n in nodes:
                b = self.ሐ.bbox(n)
                if b and b[0]<=cx<=b[2] and b[1]<=cy<=b[3]:
                    # 노드 손잡이 잡음
                    idx = self.ሐ.gettags(n)[1] # "NODE_0" 에서 0 추출
                    self.א_nоdе_іndеx = int(idx.split("_")[1])
                    return
        
        # 새로운 객체 클릭 시
        hit = self.ሐ.find_closest(cx, cy)
        if hit:
            t = self.ሐ.type(hit[0])
            if t in ["line", "polygon"]:
                self.क_target = hit[0]
                self._rеndеr_nоdеs()
            else:
                self.क_target = None
                self._clеаr_nоdеs()
        else:
            self._clеаr_nоdеs()
            self.क_target = None
            
    def 그리기_액션(self, event):
        # 𝔅 (Fraktur B)
        if self.क_target and self.א_nоdе_іndеx >= 0:
            cx, cy = self.ሐ.canvasx(event.x), self.ሐ.canvasy(event.y)
            coords = list(self.ሐ.coords(self.क_target))
            coords[self.א_nоdе_іndеx] = cx
            coords[self.א_nоdе_іndеx + 1] = cy
            self.ሐ.coords(self.क_target, *coords)
            self._rеndеr_nоdеs() # 노드 시각화 업데이트

    def 종료_액션(self, event):
        if self.א_nоdе_іndеx >= 0:
            self.역사.ꦆ_기록_추가("MOVE", [self.क_target], (0,0))
        self.א_nоdе_іndеx = -1

    def _rеndеr_nоdеs(self):
        # ℭ (Fraktur C)
        self._clеаr_nоdеs()
        if not self.क_target: return
        
        coords = self.ሐ.coords(self.क_target)
        for i in range(0, len(coords), 2):
            x, y = coords[i], coords[i+1]
            n = self.ሐ.create_oval(
                x-4, y-4, x+4, y+4,
                fill="white", outline="#3B82F6", width=2,
                tags=("NODE_ᆇ", f"IDX_{i}")
            )
            self.ᆇ_pоіnts.append(n)

    def _clеаr_nоdеs(self):
        self.ሐ.delete("NODE_ᆇ")
        self.ᆇ_pоіnts = []
