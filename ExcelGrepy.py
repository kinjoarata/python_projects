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
root = tkk.FormK(10,20,10)
root.title("Excel Grepy")
root.geometry("1000x800")


#'excelgrepy_icon.ico'


# 背景色
root.bg = '#9ABF5F'
root.configure(background=root.bg)
root.result = tk.StringVar()



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

# フォルダ選択ダイアログ
def btnFolderDir_click():
    root = tk.Tk()
    root.withdraw()
    iDir = ""
    file = filedialog.askdirectory(initialdir = iDir)
    
    # 処理ファイル名の出力
    if file != "":
        txtPath.delete(0, tk.END)
        txtPath.insert(0, file)

# クリアボタン
def btnClear_click():

    # メッセージ初期化
    root.result.set("")

    # 各種パス初期化
    txtPath.delete(0, tk.END)
    txtStr.delete(0, tk.END)

    # grid初期化
    x = tree.get_children()
    for item in x:
        tree.delete(item)

    # プログレスバー更新（初期化）
    progress.configure(value=0, maximum=100)
    progress.update()


# 精査ボタン
def btnCheck_click():

    # メッセージ初期化
    root.result.set("")

    # grid初期化
    x = tree.get_children()
    for item in x:
        tree.delete(item)

    # パラメータ取得
    p_temp = Path(txtPath.get())

    # エラーチェック
    if txtPath.get() == "":
        messagebox.showerror("エラー", "検索するフォルダを選択してください。")
        return

    cnt = 0
    for i in p_temp.glob('**/*.xlsx'):
        row_data =[i.name, '-', i]
        tree.insert("","end",tags=cnt,values=row_data)
        cnt += 1

    if cnt == 0:
        root.result.set(str(cnt) + "該当のフォルダにはxlsxファイルは存在しませんでした。")
    else:
        root.result.set(str(cnt) + "個のファイルが見つかりました！")


# Grepボタン
def btnGrep_click():

    # メッセージ初期化
    root.result.set("")

    # grid初期化
    x = tree.get_children()
    for item in x:
        tree.delete(item)

    # パラメータ取得
    p_temp = Path(txtPath.get())
    s_str = txtStr.get()

    # エラーチェック
    if txtPath.get() == "":
        messagebox.showerror("エラー", "検索するフォルダを選択してください。")
        return
    if s_str == "":
        messagebox.showerror("エラー", "検索する文字列を入力してください。")
        return

    cnt = 0
    prg_cnt = 0
    max_cnt = 0

    # 検索結果数をカウント
    for i in p_temp.glob('**/*.xlsx'):
        max_cnt += 1

    # プログレスバーを設定
    progress.configure(value=prg_cnt, maximum=max_cnt)

    for i in p_temp.glob('**/*.xlsx'):
        # 引数のExcelファイルを開く
        wb = px.load_workbook(i, data_only=True)
        for nm in wb.get_sheet_names():
            ws = wb[nm]
            value_matrix = str(list(ws.values))
            value_matrix = value_matrix.replace('(None','')
            value_matrix = value_matrix.replace('None), ','')
            value_matrix = value_matrix.replace(', None','')
            if (s_str in str(value_matrix)):
                row_data =[i.name, nm, i]
                tree.insert("","end",tags=cnt,values=row_data)
                cnt += 1
        wb.close()


        # プログレスバー更新
        prg_cnt += 1
        progress.configure(value=prg_cnt)
        progress.update()

    # プログレスバー更新（END）
    progress.configure(value=max_cnt, maximum=max_cnt)
    progress.update()

    if cnt == 0:
        root.result.set("該当のフォルダには検索文字列は存在しませんでした。")
    else:
        root.result.set(str(cnt) + "個のファイルが見つかりました！")

# treeviewダブルクリック
def tree_row_dclick(self):
    # 行データの取得
    selected_items = tree.selection()
    row_data = tree.item(selected_items[0])
    # パスの取得
    row_value = row_data['values']
    file_path = row_value[2]
    # ファイルを開く
    #print (file_path)
    subprocess.Popen(['start', file_path], shell=True)




#### 画面オブジェクト作成

# 1.メニューの設定
btnQuit = tkk.ButtonK()
btnQuit["text"] = "終了"
btnQuit["command"] = root.destroy
btnQuit.layout = "1,10,1,1"


# ラベルの生成
lblProg = tkk.LabelK()
lblProg["text"] = "進捗"
lblProg["bg"] = root.bg
lblProg["anchor"] = "e"
lblProg.layout = "1,1,1,1"

progress = tkk.ProgressbarK()
progress.configure( value=0
                  , mode='determinate'
                  , maximum=1000
                  , length=600)
progress.layout = "1,2,1,8"


## 2 row ################################################
# ラベルの生成
lblFilePath = tkk.LabelK()
lblFilePath["text"] = "フォルダパス"
lblFilePath["bg"] = root.bg
lblFilePath["anchor"] = "e"
lblFilePath.layout = "2,1,1,1"

# 入力ボックス(FilePath)
txtPath = tkk.EntryK()
txtPath.layout = "2,2,1,8"

# 参照ボタン
btnFolderDir = tkk.ButtonK()
btnFolderDir["text"] = "参照"
btnFolderDir["command"] = btnFolderDir_click
btnFolderDir.layout = "2,10,1,1"


## 3 row ################################################
# ラベルの生成
lblFilePath = tkk.LabelK()
lblFilePath["text"] = "検索文字列"
lblFilePath["bg"] = root.bg
lblFilePath["anchor"] = "e"
lblFilePath.layout = "3,1,1,1"

# 検索文字
txtStr = tkk.EntryK()
txtStr.layout = "3,2,1,8"

## 4 row ################################################
# ラベルの生成
lblCond = tkk.LabelK()
lblCond["text"] = "検索結果"
lblCond["bg"] = root.bg
lblCond["anchor"] = "e"
lblCond.layout = "4,1,1,1"

lblCondResult = tkk.LabelK()
lblCondResult["textvariable"] = root.result
lblCondResult["anchor"] = "w"
lblCondResult.layout = "4,2,1,8"


## 5 row ################################################

# 検索処理
btnGrep = tkk.ButtonK()
btnGrep["text"] = "Grep"
btnGrep["command"] = btnGrep_click
btnGrep.layout = "5,10,1,1"

btnCheck = tkk.ButtonK()
btnCheck["text"] = "精 査"
btnCheck["command"] = btnCheck_click
btnCheck.layout = "5,9,1,1"

btnCheck = tkk.ButtonK()
btnCheck["text"] = "クリア"
btnCheck["command"] = btnClear_click
btnCheck.layout = "5,1,1,1"


## 6-20 row ################################################
# ツリービューの作成
tree = tkk.TreeviewK()

tree["columns"] = (1,2,3)
tree["show"] = "headings"
tree.column(1,width=100)
tree.column(2,width=75)
tree.column(3,width=100)
tree.heading(1,text="ファイル名")
tree.heading(2,text="シート名")
tree.heading(3,text="ファイルパス")
tree.bind('<Double-1>', tree_row_dclick)

# ツリービューのスタイル変更
style = ttk.Style()
#tree.pack(fill="both",padx=3,pady=3 ,expand=1)
tree.layout = "6,1,15,10"


root.set_layout()

# メインループ
root.mainloop()
