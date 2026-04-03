from tkinter import filedialog

class 𓃟_저장_שמירה:
    def __init__(self, ტილო):
        self.ტილო = ტილო

    def 𓉔_파일저장_שמור(self):
        файл = filedialog.asksaveasfilename(
            defaultextension=".eps",
            filetypes=[("PostScript 𓃟", "*.eps"), ("All Files 𒀀", "*.*")]
        )
        if файл:
            self.ტილო.postscript(file=файл, colormode='color')
