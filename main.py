import tkinter as tk

import object.button as bt 
import object.frame as frm
import plus_button 
import home 
root = tk.Tk()
root.title("board_App")
root.geometry("400x600")
#맨 위 프레임 설정
main_frm =frm.frame(root, 450, 350, "top", "white")
main_frm_obj = main_frm.frm_maker()

#아래 메뉴 프레임 설정
menu_frm =frm.frame(root, 400, 50, "bottom", "lightgray")
menu_frm_obj =menu_frm.frm_maker()

#프레임에 +버튼, 홈버튼, 삭제버튼 추가
#+바튼 생성
plus_btn = bt._button(menu_frm_obj, "+", "left", True, lambda:plus_button.plus_bnt(main_frm_obj))
plus_btn.bnt_maker()

#홈버튼 생성
home_btn = bt._button(menu_frm_obj, "Home", "left", True, lambda:home.home_click(main_frm_obj))
home_btn.bnt_maker()

#삭제버튼
del_btn = bt._button(menu_frm_obj, "del", "left", True)
del_btn.bnt_maker()

root.mainloop()