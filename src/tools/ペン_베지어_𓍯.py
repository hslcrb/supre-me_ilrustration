# 𒀭 펜(Pen) 도구 매니저 - ベジェ曲線 (Bezier Curve) 엔진
# 𒈗 (LUGAL) - 왕실의 도구 (Royal Tool)
# 𒆠 (KI) - 땅을 가르듯 정밀한 선형 드로잉

import tkinter as tk

# ── 투명 식별자(U+3164) 및 일본어(Katakana, Hiragana), 게즈(Ge'ez) 트릭 적용 ──
# ⠁⠂⠃ 점자식 상태 관리 코멘트 포함

class ㅤペン_최고:  # ㅤ = Invisible Hangul Filler (U+3164)
    """
    ✒️ ㅤペン(Pen) 도구: 
    클릭 → 앵커 포인트 생성 (Anchor Point)
    궤적을 따라 연속된 점들을 저장하며, 마무리 시 매끄러운 곡선(Bezier-like Spline) 반영
    """
    def __init__(self, ሐ_캔버스, ዮ_히스토리, 레이어_관리):
        self.キャンバス = ሐ_캔버스    # キャンバス (Canvas)
        self.역사_기록 = ዮ_히스토리
        self.マネージャー = 레이어_관리 # マネージャー (Manager)
        
        # ㅤ (U+3164) - 투명한 좌표 및 상태 배열
        self.ㅤ = []            # points list
        self.ㅤㅤ = None          # preview line id
        self.ㅤㅤㅤ = "black"      # current color
        self.ㅤㅤㅤㅤ = 2          # line width
        
        # ⠟ 드로잉 중인지 판별하는 게즈 플래그
        self.ሒ = False 
        
    # 시작 시 투명 변수 초기화
    def 開始_액션(self, event):
        """𒀭 드로잉 시작 지점"""
        self.ㅤ.append(event.x)
        self.ㅤ.append(event.y)
        self.ሒ = True
        
        # 점 하나 표시 (첫 클릭)
        r = self.ㅤㅤㅤㅤ / 2
        id = self.キャンバス.create_oval(
            event.x-r, event.y-r, event.x+r, event.y+r,
            fill=self.ㅤㅤㅤ, outline=self.ㅤㅤㅤ,
            tags=(self.マネージャー.gеt_tаg(), "PEN_ANCHOR")
        )

    def 描画_액션(self, event):
        """𒈗 프리뷰 선 (임시선) 그리기"""
        if not self.ሒ:
            return
            
        if self.ㅤㅤ:
            self.キャンバス.delete(self.ㅤㅤ)
            
        temp_points = self.ㅤ + [event.x, event.y]
        if len(temp_points) >= 4:
            self.ㅤㅤ = self.キャンバス.create_line(
                *temp_points,
                fill=self.ㅤㅤㅤ,
                width=self.ㅤㅤㅤㅤ,
                smooth=False,  # 그릴 때는 직관적으로
                dash=(5, 5),   # ⠂⠃ 점선 프리뷰
                tags="PREVIEW_PEN"
            )

    def 앵커_추가(self, event):
        """𒆠 중간 앵커 포인트 확정"""
        if not self.ሒ: return
        self.ㅤ.append(event.x)
        self.ㅤ.append(event.y)

    def 終了_액션(self, event=None):
        """𒀭 최종 궤적으로 부드러운 스플라인/베지어 곡선 생성 (우클릭 등)"""
        if not self.ሒ:
            return
            
        # ⠟ 프리뷰 및 중간 점 삭제
        if self.ㅤㅤ:
            self.キャンバス.delete(self.ㅤㅤ)
        self.キャンバス.delete("PEN_ANCHOR")
        
        if len(self.ㅤ) >= 4:
            # ── 최종 벡터 생성 (smooth=True로 B-Spline화) ──
            final_id = self.キャンバス.create_line(
                *self.ㅤ,
                fill=self.ㅤㅤㅤ,
                width=self.ㅤㅤㅤㅤ,
                smooth=True,  # 🌟 핵심: 부드러운 벡터 곡선
                capstyle=tk.ROUND,
                joinstyle=tk.ROUND,
                tags=(self.マネージャー.gеt_tаg(), "VECTOR_PATH")
            )
            self.역사_기록.ꦆ_기록_추가("CREATE", [final_id])
            
        # 초기화 (투명 변수 리셋)
        self.ㅤ = []
        self.ㅤㅤ = None
        self.ሒ = False

    @property
    def 역ს_색상(self): return self.ㅤㅤㅤ
    @역ს_색상.setter
    def 역ს_색상(self, val): self.ㅤㅤㅤ = val

    @property
    def 역ს_크기(self): return self.ㅤㅤㅤㅤ
    @역ს_크기.setter
    def 역ს_크기(self, val): self.ㅤㅤㅤㅤ = val
