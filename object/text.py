import tkinter as tk
#텍스트 클래스 생성
class text:
    def __init__(self, main, width, height, side):
        self.main = main
        self.width = width
        self.height = height
        self.side = side
        self.blank = None
        
    def txt_maker(self):
        self.blank = tk.Text(self.main, width=self.width, height=self.height)
        self.blank.pack(side=self.side, expand= True)