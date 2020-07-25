# -*- coding: utf-8 -*-

#### インポート
import tkinter as tk
import tkinter.ttk as ttk

from tkinter import messagebox
from tkinter import filedialog
from pathlib import Path

# フォーム
class FormK(tk.Tk):
    pass

    def __init__(self, p_max_row, p_max_col, p_padding):
        super(FormK, self).__init__()
        
        ## レイアウト用プロパティ
        self.MAX_ROW = p_max_row
        self.MAX_COL = p_max_col
        self.PAD_OUT = p_padding
        self.PAD_IN  = p_padding

        # 定数設定
        self.CONST_MSG_ICON_INFO = 1
        self.CONST_MSG_ICON_ALERT = 2
        self.CONST_MSG_ICON_ERROR = 3
         
        self.CONST_MSG_QUES_YES_NO = 1
        self.CONST_MSG_QUES_OK_CANCEL = 2
        self.CONST_MSG_QUES_RETRY_CANCEL = 4

    ## 定義時の画面サイズ設定
    def geometry(self,newGeometry=None):
        super(FormK, self).geometry(newGeometry)
        sp = newGeometry.split("x")
        self.HEIGHT = int(sp[0])
        self.WIDTH  = int(sp[1])


    ## メッセージボックス
    def MsgBox(self,p_msg,p_title,p_icon,p_ques):

        # 返却値初期値
        o_res = None

        if (p_ques == None):
            if (p_icon == self.CONST_MSG_ICON_INFO):
                messagebox.showinfo(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ALERT):
                messagebox.showwarning(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ERROR):
                messagebox.showerror(p_title,p_msg)
        if (p_ques == self.CONST_MSG_QUES_YES_NO):
            if (p_icon == self.CONST_MSG_ICON_INFO):
                o_res = messagebox.askyesno(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ALERT):
                o_res = messagebox.askyesno(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ERROR):
                o_res = messagebox.askyesno(p_title,p_msg)
        if (p_ques == self.CONST_MSG_QUES_OK_CANCEL):
            if (p_icon == self.CONST_MSG_ICON_INFO):
                o_res = messagebox.askokcancel(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ALERT):
                o_res = messagebox.askokcancel(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ERROR):
                o_res = messagebox.askokcancel(p_title,p_msg)
        if (p_ques == self.CONST_MSG_QUES_RETRY_CANCEL):
            if (p_icon == self.CONST_MSG_ICON_INFO):
                o_res = messagebox.askretrycancel(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ALERT):
                o_res = messagebox.askretrycancel(p_title,p_msg)
            if (p_icon == self.CONST_MSG_ICON_ERROR):
                o_res = messagebox.askretrycancel(p_title,p_msg)
        return o_res

    ## オブジェクトを配置する
    def set_layout(self):

        n_height_in = self.HEIGHT - (self.PAD_OUT * 2)
        n_height_one = (n_height_in - ((self.MAX_ROW - 1) * self.PAD_IN)) / self.MAX_ROW

        n_width_in = self.WIDTH - (self.PAD_OUT * 2)
        n_width_one = (n_width_in  - ((self.MAX_COL - 1) * self.PAD_IN)) / self.MAX_COL

        # 計算用
        #print("n_height_in="+str(n_height_in))
        #print("n_height_one="+str(n_height_one))
        #print("n_width_in="+str(n_width_in))
        #print("n_width_one="+str(n_width_one))

        for v in self.children:
            try:
                if self.children[v].layout != None:
                    sp = self.children[v].layout.split(",")

                    # 計算用
                    #s_layout = "relx="  +       str(round(((self.PAD_OUT) + ((int(sp[0])-1) * n_width_one)  + ((int(sp[0]) - 1) * self.PAD_IN)) / self.WIDTH ,4))
                    #s_layout += ",rely=" +      str(round(((self.PAD_OUT) + ((int(sp[1])-1) * n_height_one) + ((int(sp[1]) - 1) * self.PAD_IN)) / self.HEIGHT ,4))
                    #s_layout += ",relwidth="  + str(round(( (int(sp[2]) * n_width_one)     + ((int(sp[2]) - 1) * self.PAD_IN)) / self.WIDTH ,4))
                    #s_layout += ",relheight=" + str(round(( (int(sp[3]) * n_height_one)    + ((int(sp[3]) - 1) * self.PAD_IN)) / self.HEIGHT ,4))
                    #print(s_layout)

                    self.children[v].place_configure(
                        rely     =round((float(self.PAD_OUT) + ((int(sp[0])-1) * n_width_one)  + ((int(sp[0]) - 1) * self.PAD_IN)) / self.WIDTH ,4)
                       ,relx     =round((float(self.PAD_OUT) + ((int(sp[1])-1) * n_height_one) + ((int(sp[1]) - 1) * self.PAD_IN)) / self.HEIGHT ,4)
                       ,relheight=round(((int(sp[2]) * n_width_one)  + ((int(sp[2]) - 1) * self.PAD_IN)) / self.WIDTH ,4)
                       ,relwidth =round(((int(sp[3]) * n_height_one) + ((int(sp[3]) - 1) * self.PAD_IN)) / self.HEIGHT ,4)
                    )
            except:
                print("No TkinterK Object(" + v +").")
                pass


        pass

# 以下ABC順

class ButtonK(tk.Button):
    pass
    
    def __init__(self):
        super(ButtonK, self).__init__()
        self.layout = None

class CanvasK(tk.Canvas):
    pass
    
    def __init__(self):
        super(CanvasK, self).__init__()
        self.layout = None

class CheckbuttonK(tk.Checkbutton):
    pass
    
    def __init__(self):
        super(CheckbuttonK, self).__init__()
        self.layout = None

class EntryK(tk.Entry):
    pass
    
    def __init__(self):
        super(EntryK, self).__init__()
        self.layout = None
        self["highlightthickness"] = 1
        self.config(highlightcolor= "red")

class FrameK(tk.Frame):
    pass
    
    def __init__(self):
        super(FrameK, self).__init__()
        self.layout = None

class LabelFrameK(tk.LabelFrame):
    pass
    
    def __init__(self):
        super(LabelFrameK, self).__init__()
        self.layout = None

class LabelK(tk.Label):
    pass
    
    def __init__(self):
        super(LabelK, self).__init__()
        self.layout = None

class ListboxK(tk.Listbox):
    pass
    
    def __init__(self):
        super(ListboxK, self).__init__()
        self.layout = None

class MenubuttonK(tk.Menubutton):
    pass
    
    def __init__(self):
        super(MenubuttonK, self).__init__()
        self.layout = None

class MenuK(tk.Menu):
    pass
    
    def __init__(self):
        super(MenuK, self).__init__()
        self.layout = None

class MessageK(tk.Message):
    pass
    
    def __init__(self):
        super(MessageK, self).__init__()
        self.layout = None

class PanedWindowK(tk.PanedWindow):
    pass
    
    def __init__(self):
        super(PanedWindowK, self).__init__()
        self.layout = None

class ProgressbarK(ttk.Progressbar):
    pass
    
    def __init__(self):
        super(ProgressbarK, self).__init__()
        self.layout = None

class RadiobuttonK(tk.Radiobutton):
    pass
    
    def __init__(self):
        super(RadiobuttonK, self).__init__()
        self.layout = None

class SpinboxK(tk.Spinbox):
    pass
    
    def __init__(self):
        super(SpinboxK, self).__init__()
        self.layout = None

class TextK(tk.Text):
    pass
    
    def __init__(self):
        super(TextK, self).__init__()
        self.layout = None

class TreeviewK(ttk.Treeview):
    pass
    
    def __init__(self):
        super(TreeviewK, self).__init__()
        self.layout = None


