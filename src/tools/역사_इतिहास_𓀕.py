# ꧄ ꧅ 𝔘𝔫𝔡𝔬/ℜ𝔢𝔡𝔬 엔진 (𝔄𝔠𝔱𝔦𝔬𝔫 ℌ𝔦𝔰𝔱𝔬𝔯𝔶)
# ♩ ♪ ♫ ♬ (Comments only) / ꧄ (Javanese) / ㅤ (Hangul Filler)

import tkinter as tk

class 𝔘역사_최고:   # 𝔘 = Fraktur U
    def __init__(self, ሐ_캔버스):
        self.ሐ = ሐ_캔버스
        self.ꦄ_undo_stack = [] # ♩ (Quarter Note)
        self.ꦅ_redo_stack = [] # ♪ (Eighth Note)
        self.ㅤ_lock = False    # ㅤ (투명) 기록 중복 방지 락

    def ꦆ_기록_추가(self, ꦈ_action_type, ꦄ_items, ꦅ_data=None):
        """
        ꦈ_action_type: 'CREATE', 'DELETE', 'MOVE', 'ATTR'
        ꦄ_items: 캔버스 아이템 ID 목록
        ꦅ_data: 이전 좌표나 속성 값들
        """
        if self.ㅤ_lock: return
        
        # ꧄ ꧅ 쓰레기 수거 (Garbage Collection): 더 이상 복원 불가능한 숨겨진 객체 영구 삭제
        for ꦈ_act in self.ꦅ_redo_stack:
            if ꦈ_act["type"] == "CREATE":
                for i in ꦈ_act["ids"]:
                    try:
                        if self.ሐ.itemcget(i, "state") == "hidden":
                            self.ሐ.delete(i)
                    except: pass
        
        # 새로운 액션이 들어오면 Redo 스택 초기화
        self.ꦅ_redo_stack.clear()
        
        액션_패키지 = {
            "type": ꦈ_action_type,
            "ids": ꦄ_items,
            "data": ꦅ_data
        }
        self.ꦄ_undo_stack.append(액션_패키지)
        # 최대 100개까지만 보관 (안정성)
        if len(self.ꦄ_undo_stack) > 100:
            self.ꦄ_undo_stack.pop(0)

    def ꦇ_undo_액션(self):
        if not self.ꦄ_undo_stack: return
        
        self.ㅤ_lock = True
        ꦈ_act = self.ꦄ_undo_stack.pop()
        
        # Undo 로직
        if ꦈ_act["type"] == "CREATE":
            # 생성 취소 -> 일단 숨김 (Redo를 위해 완전삭제 안함)
            for i in ꦈ_act["ids"]:
                self.ሐ.itemconfig(i, state="hidden")
        elif ꦈ_act["type"] == "DELETE":
            # 삭제 취소 -> 다시 표시
            for i in ꦈ_act["ids"]:
                self.ሐ.itemconfig(i, state="normal")
        elif ꦈ_act["type"] == "MOVE":
            # 이동 취소 -> 반대로 이동
            dx, dy = ꦈ_act["data"]
            for i in ꦈ_act["ids"]:
                self.ሐ.move(i, -dx, -dy)
        
        self.ꦅ_redo_stack.append(ꦈ_act)
        self.ㅤ_lock = False

    def ꦈ_redo_액션(self):
        if not self.ꦅ_redo_stack: return
        
        self.ㅤ_lock = True
        ꦈ_act = self.ꦅ_redo_stack.pop()
        
        # Redo 로직
        if ꦈ_act["type"] == "CREATE":
            for i in ꦈ_act["ids"]:
                self.ሐ.itemconfig(i, state="normal")
        elif ꦈ_act["type"] == "DELETE":
            for i in ꦈ_act["ids"]:
                self.ሐ.itemconfig(i, state="hidden")
        elif ꦈ_act["type"] == "MOVE":
            dx, dy = ꦈ_act["data"]
            for i in ꦈ_act["ids"]:
                self.ሐ.move(i, dx, dy)
                
        self.ꦄ_undo_stack.append(ꦈ_act)
        self.ㅤ_lock = False
