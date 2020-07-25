# -*- coding: utf-8 -*-

#### インポート
import os
import tkinter as tk
import tkinter.ttk as ttk
import openpyxl as px
import subprocess

import TKinterK as tkk

from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path

#### rootフレームの設定
root = tkk.FormK(20,15,10)
root.title("Simple Excel Editor")
root.geometry("1000x800")



# 背景色
root.bg = '#9ABF5F'
root.configure(background=root.bg)

# スタイル設定
style = ttk.Style() 
style.configure('TButton', font = 
               ('calibri', 20, 'bold'),
                    borderwidth = '4') 
  
# Changes will be reflected 
# by the movement of mouse. 
style.map('Button'
         , foreground = [('active', '!disabled', 'green')]
         , background = [('active', 'black')]
         )





#### 画面イベント関数










#### 画面オブジェクト作成

# 1.メニューの設定
btnOpen = tkk.ButtonK()
btnOpen["text"] = "開く"
btnOpen["command"] = root.destroy
btnOpen.layout = "1,1,1,1"

btnSave = tkk.ButtonK()
btnSave["text"] = "保存"
btnSave["command"] = root.destroy
btnSave.layout = "2,1,1,1"

btnQuit = tkk.ButtonK()
btnQuit["text"] = "終了"
btnQuit["command"] = root.destroy
btnQuit.layout = "15,1,1,1"


root.set_layout()

# メインループ
root.mainloop()
