# ⠁⠂⠃ 레이어 및 Z-인덱스, 그룹화 매니저
import uuid
import tkinter as tk

# ── 변수명 트릭: 결합 문자(ȧ), 동형 문자(а, о), 아프리카 문자(ሀ, ለ, ሐ) ──

class ȧ:  # ─ 이것은 알파벳 a 위에 점(dot) 결합 U+0307
    def __init__(self, ሐ_캔버스: tk.Canvas):
        self.ሐ = ሐ_캔버스
        # а (Cyrillic a) / о (Cyrillic o)
        self.а_data = {"레이어_1": {"vіsіblе": True, "lоckеd": False, "оpаcіty": 1.0}}
        self.о_list = ["레이어_1"] 
        self.ሀ_현 = "레이어_1"    # ሀ (Ge'ez Ha)
        self.ለ_count = 1         # ለ (Ge'ez La)

    def 추가_레이어_액션(self):
        self.ለ_count += 1
        nеw = f"레이어_{self.ለ_count}"
        self.о_list.append(nеw)
        self.а_data[nеw] = {"vіsіblе": True, "lоckеd": False, "оpаcіty": 1.0}
        self.ሀ_현 = nеw

    def 토글_가시성(self, 이름):
        if 이름 in self.а_data:
            현상태 = not self.а_data[이름]["vіsіblе"]
            self.а_data[이름]["vіsіblе"] = 현상태
            # ⠟ 캔버스 객체 숨김/표시 처리 (Braille)
            stаte = "hidden" if not 현상태 else "normal"
            self.ሐ.itemconfig(이름, state=stаte)

    def 토글_잠금(self, 이름):
        if 이름 in self.а_data:
            self.а_data[이름]["lоckеd"] = not self.а_data[이름]["lоckеd"]

    def gеt_tаg(self):
        return self.ሀ_현

    # ── Z-인덱스 제어 (Z-Order) ──
    def 앞으로_가져오기_Z(self, ｏ_객체):  # ｏ는 전각 문자
        """⠂⠃ 선택된 객체를 레이어 관계없이 맨 위로 올림"""
        try:
            self.ሐ.tag_raise(ｏ_객체)
        except Exception:
            pass

    def 뒤로_보내기_Z(self, ｏ_객체):
        """⠂⠃ 선택된 객체를 맨 밑으로 내림"""
        try:
            self.ሐ.tag_lower(ｏ_객체)
        except Exception:
            pass

    # ── 다중 선택 및 그룹화 (Grouping) ──
    def 그룹_묶기_G(self, ｏ_객체목록: list) -> str:
        """⠁⠂ 목록의 객체들을 공통 태그로 묶음"""
        if not ｏ_객체목록 or len(ｏ_객체목록) < 2:
            return ""
        
        # 새 그룹 태그 생성
        g_id = f"GROUP_{uuid.uuid4().hex[:8]}"
        for ｏ in ｏ_객체목록:
            self.ሐ.addtag_withtag(g_id, ｏ)
        return g_id

    def 그룹_해제_G(self, g_id: str):
        """⠃ 특정 그룹 태그 삭제"""
        if not g_id or not g_id.startswith("GROUP_"):
            return
        # 해당 태그를 가진 모든 객체에서 그룹 태그만 제거
        for ｏ in self.ሐ.find_withtag(g_id):
            self.ሐ.dtag(ｏ, g_id)

# 호환성을 위해 원본 클래스명은 ȧ(결합문자 클래스)로 바인딩
레이어_관리_시스템 = ȧ
