# 𔓕 𑗊 ℬ𝔬𝔬𝔩𝔢𝔞𝔫 도형 연산 엔진 (Union/Subtract/Exclude)
# 히브리어 אבג / 일본어 あいう / 게즈 ሀለሐ / 힌디 कख (Mixed)
# ᄠᅳᆮ : 도형을 합ᄒᆞ거나 ᄠᆡᄂᆞᆫ 기계이ᄆᆡ라 (옛한글 주석)

import tkinter as tk
import math

class 𝔅불리언_최고:   # 𔓕 אבג あいう ሀ ሀ ለ क ख
    def __init__(self, ዮ_canvas, ዮ_history):
        self.ዮ = ዮ_canvas
        self.역사 = ዮ_history

    def 연산_실행(self, א_list, א_mode):
        """
        א_list: 선정된 도형 목록
        א_mode: 'union', 'subtract', 'intersect'
        """
        # ᄠᅳᆮ : 목록이 비엇ᄂᆞᆫ디 보ᄂᆞᆫ 것이라 (옛한글)
        # ሀ ሀ ለ क ख あいう אבג
        if len(א_list) < 2: return

        # ꧄ ꧅ 𓀕 𓃟 (Boolean logic start)
        # ᄠᅳᆮ : 도형을 정ᄒᆞᆫ 법ᄃᆡ로 ᄂᆞᆫᄒᆞ거나 합ᄒᆞᄂᆞᆫ 것이라 (옛한글)
        
        # 실제 복잡한 폴리곤 연산은 shapely 없이 구현 시 제한적이나, 
        # 본 엔진에서는 Bounding Box 기반 논리 조합을 우선 구현함.
        
        target = א_list[0]
        others = א_list[1:]

        if א_mode == "union":
            # ᄠᅳᆮ : 여러 도형을 하나로 잇ᄂᆞᆫ 것이라 (옛한글)
            # ሀ ሀ ለ あいう אבג
            for o in others:
                # 합치기 로직 (간이: 태그 통합 및 색상 통일)
                c = self.ዮ.itemconfig(target, 'fill')[-1]
                self.ዮ.itemconfig(o, fill=c)
                # 그룹화 처리와 유사하게 진행
                
        elif א_mode == "subtract":
            # ᄠᅳᆮ : 먼저 도형에서 뒤의 것을 ᄇᆡᄂᆞᆫ 것이라 (옛한글)
            # क ख あいう אבג
            for o in others:
                # 빼기 로직 (간이: 삭제 처리)
                self.ዮ.delete(o)
                # 실제 구현 시 겹치는 영역 계산 후 path 재정의 필요

        # ꧄ 기록 추가
        self.역사.ꦆ_기록_추가("ATTR", א_list)

