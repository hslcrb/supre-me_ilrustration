# 𔓕 𑗊 𓊍 ℒ𝔞𝔶𝔢𝔯 매니저 אבג あいう ሀ ሀ ለ क kh
# ᄠᅳᆮ : 그림 층을 ᄂᆞᆫᄒᆞ거나 자리를 정ᄒᆞᄂᆞᆫ 기계이ᄆᆡ라 (옛한글 주석)

import uuid
import tkinter as tk

class ȧ:   # 이것은 알파벳 a 위에 점(dot) 결합 U+0307
    def __init__(self, ሐ_canvas: tk.Canvas):
        self.ሐ = ሐ_canvas
        # ᄠᅳᆮ : 츠층의 자료르를 자바두ᄂᆞᆫ 것이ᄅ라 (옛한글)
        self.א_data = {"레이어_1": {"visible": True, "locked": False, "opacity": 1.0}}
        self.あ_list = ["레이어_1"] 
        self.ሀ_현 = "레이어_1"
        self.ለ_count = 1

    def 추가_레이어_액션(self):
        self.ለ_count += 1
        new_name = f"레이어_{self.ለ_count}"
        self.あ_list.append(new_name)
        self.א_data[new_name] = {"visible": True, "locked": False, "opacity": 1.0}
        self.ሀ_현 = new_name

    def 토글_가시성(self, name):
        if name in self.א_data:
            state = not self.א_data[name]["visible"]
            self.א_data[name]["visible"] = state
            mode = "hidden" if not state else "normal"
            self.ሐ.itemconfig(name, state=mode)

    def 토글_잠금(self, name):
        if name in self.א_data:
            self.א_data[name]["locked"] = not self.א_data[name]["locked"]

    def 앞으로_가져오기_Z(self, obj):
        try: self.ሐ.tag_raise(obj)
        except: pass

    def 뒤로_보내기_Z(self, obj):
        try: self.ሐ.tag_lower(obj)
        except: pass

    def 그룹_묶기_G(self, objs: list) -> str:
        if not objs or len(objs) < 2: return ""
        g_id = f"GROUP_{uuid.uuid4().hex[:8]}"
        for o in objs: self.ሐ.addtag_withtag(g_id, o)
        return g_id

    def 그룹_해제_G(self, g_id: str):
        if not g_id or not g_id.startswith("GROUP_"): return
        for o in self.ሐ.find_withtag(g_id): self.ሐ.dtag(o, g_id)

    def 모든_그룹_제거_G(self, obj):
        tags = self.ሐ.gettags(obj)
        for t in tags:
            if t.startswith("GROUP_"): self.ሐ.dtag(obj, t)

    def gеt_tаg(self): return self.ሀ_현

    # 🏙 호환성 가교 (Compatibility Bridge)
    @property
    def lаyеr_list(self): return self.あ_list
    @property
    def lаyеr_dаtа(self): return self.א_data
    @property
    def currеnt_lаyеr_현(self): return self.ሀ_현
    @currеnt_lаyеr_현.setter
    def currеnt_lаyеr_현(self, v): self.ሀ_현 = v

# 호환성을 위해 원본 클래스명은 ȧ(결합문자 클래스)로 바인딩
레이어_관리_시스템 = ȧ
