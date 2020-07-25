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
root = tkk.FormK(18,18,10)
root.title("tkinter all GUI")
root.geometry("1000x800")



# 背景色
root.bg = '#FFFFFF'
root.configure(background=root.bg)



#### 画面オブジェクト作成

# 1.メニューの設定
Label11 = tkk.LabelK()
Label11["text"] = "ALL TKinter GUI ects"
Label11.layout = "1,1,1,17"


btnQuit = tkk.ButtonK()
btnQuit["text"] = "終了"
btnQuit["command"] = root.destroy
btnQuit.layout = "1,18,1,1"


# ButtonK
Label21 = tkk.LabelK()
Label21["text"] = "ButtonK"
Label21.layout = "2,1,1,2"

Button = tkk.ButtonK()
Button.layout = "2,3,1,3"


# CanvasK
Label31 = tkk.LabelK()
Label31["text"] = "CanvasK"
Label31.layout = "3,1,1,5"

Canvas = tkk.CanvasK()
Canvas.layout = "4,1,4,5"




# CheckbuttonK
Label27 = tkk.LabelK()
Label27["text"] = "CheckbuttonK"
Label27.layout = "2,7,1,2"

Checkbutton = tkk.CheckbuttonK()
Checkbutton.layout = "2,9,1,3"

# EntryK
Label213 = tkk.LabelK()
Label213["text"] = "EntryK"
Label213.layout = "2,13,1,2"

Entry = tkk.EntryK()
Entry.layout = "2,15,1,3"




# FrameK
Label37 = tkk.LabelK()
Label37["text"] = "FrameK"
Label37.layout = "3,7,1,5"

Frame = tkk.FrameK()
Frame.layout = "4,7,4,5"



# LabelFrameK
Label313 = tkk.LabelK()
Label313["text"] = "LabelFrameK"
Label313.layout = "3,13,1,5"

LabelFrameK = tkk.LabelFrameK()
LabelFrameK.layout = "4,13,4,5"


# LabelK
Label81 = tkk.LabelK()
Label81["text"] = "Label"
Label81.layout = "8,1,1,2"

Label = tkk.LabelK()
Label.layout = "8,3,1,3"

# ListboxK
Label87 = tkk.LabelK()
Label87["text"] = "ListboxK"
Label87.layout = "8,7,1,2"

Listbox = tkk.ListboxK()
Listbox.layout = "8,9,1,3"



# MenubuttonK
Label1 = tkk.LabelK()
Label1["text"] = "MenubuttonK"
Label1.layout = "8,13,1,2"

MenubuttonK = tkk.MenubuttonK()
MenubuttonK.layout = "8,15,1,3"


# MenuK
Label91 = tkk.LabelK()
Label91["text"] = "MenuK"
Label91.layout = "9,1,1,2"

MenuK = tkk.MenuK()
MenuK.layout = "9,3,1,3"

## MessageK
Label96 = tkk.LabelK()
Label96["text"] = "MessageK"
Label96.layout = "9,7,1,2"

MessageK = tkk.MessageK()
MessageK.layout = "9,9,1,3"


## PanedWindowK
Label96 = tkk.LabelK()
Label96["text"] = "PanedWindowK"
Label96.layout = "9,13,1,5"

PanedWindowK = tkk.PanedWindowK()
PanedWindowK.layout = "10,13,4,5"



## ProgressbarK
Label101 = tkk.LabelK()
Label101["text"] = "ProgressbarK"
Label101.layout = "10,1,1,2"

ProgressbarK = tkk.ProgressbarK()
ProgressbarK.layout = "10,3,1,3"


## RadiobuttonK
Label101 = tkk.LabelK()
Label101["text"] = "RadiobuttonK"
Label101.layout = "10,7,1,2"

RadiobuttonK = tkk.RadiobuttonK()
RadiobuttonK.layout = "10,9,1,3"


## SpinboxK
Label111 = tkk.LabelK()
Label111["text"] = "SpinboxK"
Label111.layout = "11,1,1,2"

SpinboxK = tkk.SpinboxK()
SpinboxK.layout = "11,3,1,3"



# TextK
Label117 = tkk.LabelK()
Label117["text"] = "Text"
Label117.layout = "11,7,1,2"

TextK = tkk.TextK()
TextK.layout = "11,9,1,3"


## TreeviewK
Label111 = tkk.LabelK()
Label111["text"] = "TreeviewK"
Label111.layout = "12,1,1,11"

TreeviewK = tkk.TreeviewK()
TreeviewK.layout = "13,1,5,11"




root.set_layout()

# メインループ
root.mainloop()
