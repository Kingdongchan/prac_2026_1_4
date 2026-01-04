import tkinter as tk
#버튼 클래스 생성
class _button:
    
    def __init__(self, main, text, side, expand= None,command=None):
        self.main = main
        self.text =text
        self.side = side
        self.expand = expand
        self.command = command
        
    def bnt_maker (self):
        bnt = tk.Button(self.main, text=self.text, command=self.command)
        bnt.pack(side=self.side, expand=self.expand)
        
    