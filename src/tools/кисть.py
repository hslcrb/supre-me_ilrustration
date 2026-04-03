import tkinter as tk

class Рисование:
    def __init__(self, ტილო):
        self.ტილო = ტილო
        self.x = None
        self.y = None

    def ხატვა(self, 이벤트):
        if self.x is not None and self.y is not None:
            self.ტილო.create_line(
                self.x, self.y, 
                이벤트.x, 이벤트.y, 
                width=3, 
                fill="black", 
                capstyle="round", 
                smooth=True
            )
        self.x = 이벤트.x
        self.y = 이벤트.y

    def დასრულება(self, 멈춤):
        self.x = None
        self.y = None
