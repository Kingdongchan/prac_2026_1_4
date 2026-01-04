import tkinter as tk
#라벨 클래스 생성

class label:
    def __init__(self, main, text, side):
        self.main = main
        self.text = text
        self.side = side
        
    def lb_maker(self):
        lb = tk.Label(self.main, text=self.text)
        lb.pack(side=self.side, expand=True)
        