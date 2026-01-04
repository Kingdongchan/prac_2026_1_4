import tkinter as tk

#홈버튼을 누르면 메인 틀이 초기화되고 목록만 남음

def home_click(main_frm_obj):
    for widget in main_frm_obj.winfo_children():
        widget.destroy()
        
        