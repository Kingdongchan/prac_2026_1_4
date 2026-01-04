import tkinter as tk
from tkinter import messagebox

import object.button as bt
import object.frame as frm
import object.label as lab
import object.text as tx

root = tk.Tk()
root.geometry("400x600")
#상위(제목, txt공간) 프레임
top_frm = frm.frame(root, 400, 50, "top", "white")
top_frm_obj = top_frm.frm_maker()
#'제목' 라벨 생성
title_lb = lab.label(top_frm_obj, "제목: ", "left")
title_lb.lb_maker()
#제목 옆에 텍스트 파일
title_txt = tx.text(top_frm_obj, 50, 1, "left")
title_txt.txt_maker()
#하위(제목, txt공간0 프레임
under_frm = frm.frame(root, 400, 250, "top", "white")
under_frm_obj = under_frm.frm_maker()
#'내용' 라벨 생성
cont_lb = lab.label(under_frm_obj, "내용: ", "left")
cont_lb.lb_maker()

cont_txt = tx.text(under_frm_obj, 50, 100, "left")
cont_txt.txt_maker()

root.mainloop()
