import tkinter as tk

#세이브하는 로직을 만듬
#저장 버튼을 누르면 배열에 들어가야 하고 
#메인 틀 초기화후 내가 썻던 제목만 들어있는 버튼을 생성 
#버튼을 누르면 내가 전에 썻던 내용을 볼 수 있겠끔 만드는 로직이 필요

def file_save():
    
    t = title_txt.get("1.0","end-1c")
    c = cont_txt.get("1.0","end-1c")
    
     