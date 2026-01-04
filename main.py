import tkinter as tk

import object.button as bt 
import object.frame as frm

root = tk.Tk()
root.title("board_App")
root.geometry("400x600")
#맨 위 프레임 설정
main_frm =frm.frame(root, 450, 350, "top", "white")
main_frm.frm_maker()

#아래 메뉴 프레임 설정
menu_frm =frm.frame(root, 400, 50, "bottom", "lightgray")
menu_frm.frm_maker()

#게시판, 홈, 뉴스, 
root.mainloop()