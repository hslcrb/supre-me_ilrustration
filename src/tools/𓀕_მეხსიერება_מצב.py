class 𓀕_상태_מצב_स्थिति:
    def __init__(self, ტილო):
        self.ტილო = ტილო
        self.undo_stack = []
        self.redo_stack = []

    def 𓂝_추가_הוספה(self, 아이템_목록):
        if 아이템_목록:
            self.undo_stack.append(아이템_목록)
            self.redo_stack.clear()

    def 𓃍_실행취소_ביטול(self):
        if self.undo_stack:
            아이템_목록 = self.undo_stack.pop()
            for 아이템 in 아이템_목록:
                self.ტილო.itemconfig(아이템, state='hidden')
            self.redo_stack.append(아이템_목록)

    def 𓆣_다시실행_שוב(self):
        if self.redo_stack:
            아이템_목록 = self.redo_stack.pop()
            for 아이템 in 아이템_목록:
                self.ტილო.itemconfig(아이템, state='normal')
            self.undo_stack.append(아이템_목록)
