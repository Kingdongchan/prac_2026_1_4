import tkinter as tk
from tkinter import messagebox
#세이브하는 로직을 만듬
#저장 버튼을 누르면 배열에 들어가야 하고 
#메인 틀 초기화후 내가 썻던 제목만 들어있는 버튼을 생성 
#버튼을 누르면 내가 전에 썻던 내용을 볼 수 있겠끔 만드는 로직이 필요

#담을 공간 생성
blank = []

def file_save(title_txt, cont_txt, main_frm_obj):
    
    #제목와 내용에 쓰여진 것들 가져오기
    t = title_txt.blank.get("1.0","end-1c")
    c = cont_txt.blank.get("1.0","end-1c")

    txt_sum = {"제목": t, "내용": c}

    blank.append(txt_sum)
    
    messagebox.showinfo("저장", "저장이 완료되었습니다.")
    #저장 후 메인 틀 초기화
    for widget in main_frm_obj.winfo_children():
        widget.destory()
        
