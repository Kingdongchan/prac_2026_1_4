import tkinter as tk

#프레임 클래스 생성
class frame:
    def __init__ (self, main, width, height, side, bg):
        self.main = main
        self.width = width
        self.height = height
        self.side = side
        self.bg = bg
        
    def frm_maker(self):
        frm = tk.Frame(self.main, width=self.width, height=self.height, bg=self.bg)
        #v프레임 크기를 고정하기
        frm.pack_propagate(False)
        frm.pack(side=self.side, fill="x")
        
        return frm