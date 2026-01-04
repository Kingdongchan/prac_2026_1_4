import tkinter as tk
from tkinter import messagebox

import object.button as bt
import object.frame as frm
import object.label as lab
import object.text as tx

def plus_bnt(main_frm_obj):
    #메인 화면에 있는 것들 지우기
    for widget in main_frm_obj.winfo_children():
        widget.destroy()
        
    #상위(제목, txt공간) 프레임
    top_frm = frm.frame(main_frm_obj, 400, 50, "top", "white")
    top_frm_obj = top_frm.frm_maker()
    #'제목' 라벨 생성
    title_lb = lab.label(top_frm_obj, "제목: ", "left")
    title_lb.lb_maker()
    #제목 옆에 텍스트 파일
    title_txt = tx.text(top_frm_obj, 50, 1, "left")
    title_txt.txt_maker()
    #하위(제목, txt공간0 프레임
    mid_frm = frm.frame(main_frm_obj, 400, 250, "top", "white")
    mid_frm_obj = mid_frm.frm_maker()
    #'내용' 라벨 생성
    cont_lb = lab.label(mid_frm_obj, "내용: ", "left")
    cont_lb.lb_maker()
    # 내용 옆에 텍스트 파일
    cont_txt = tx.text(mid_frm_obj, 50, 500, "left")
    cont_txt.txt_maker()
    #아리(저장 버튼) 프레인 생성
    under_frm = frm.frame(main_frm_obj, 500, 50, "top", "white")
    under_frm_obj = under_frm.frm_maker()
    #저장 버튼 생성
    save_btn = bt._button(under_frm_obj, "저장", "right")
    save_btn.bnt_maker()

