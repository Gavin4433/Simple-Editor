from tkinter import*
from tkinter.filedialog import  askopenfilename,asksaveasfilename
from tkinter.scrolledtext import  ScrolledText
from tkinter.messagebox import  showinfo,showerror,showwarning,askquestion
import datetime as d
import time
import os,copy 
import sysfrom tkinter import*
#Using Python 3.8.3
from tkinter.filedialog import  askopenfilename,asksaveasfilename
from tkinter.scrolledtext import  ScrolledText
from tkinter.messagebox import  showinfo,showerror,showwarning,askquestion
import datetime as d
import time
import os,copy 
import sys
from tkinter.simpledialog import askstring
window = Tk()
window.title("Our Time Editor1.18(None)")
cont = ScrolledText()
cont.pack(side=BOTTOM)
langfile = '' 
def load():
      global file,window
      asd = askopenfilename(filetypes=[("Text File","txt")])
      file = copy.copy(asd)
      try:
        with open(asd,'r') as f:
             global cont
             cont.delete("1.0",END)
             cont.insert(INSERT,f.read())
      except:
            showerror("错误","错误的文件名!!!")
      window.title("Editor 1.18(" + file + ")")
def save():
      global cont,file
      asd = asksaveasfilename(filetypes=[("Text File","txt")])
      
      file = copy.copy(asd)
      if file =='':
            showerror("文件名不能为空!")
            return
      try:
          with open(asd,'w') as f:
             f.write(cont.get("1.0",END))
      except:
            showerror("Python TK","写入失败!!!")
      file=''
def save2():
      global file
      try:
        with open(file,'w') as f:
             f.write(cont.get("1.0",END))
      except:
            showerror("Python TK","写入失败!!!")
def prints2():
      showinfo("版本","1.18.2.7(V1)")
def prints3():
      datea = d.datetime.today()
      year = datea.year
      month = datea.month
      day = datea.day
      showinfo("date",str(year) + '年' + str(month) +'月' + str(day) + "日")

def e():
      esc = askquestion("Python TK","你想退出吗?")
      if esc == 'yes':
            sys.exit()
      else:
            return
def prints7():
      datea = d.datetime.today()
      hour = datea.hour
      minutes = datea.minute
      showinfo("time",str(hour) + ' : ' + str(minutes))
def author():
      showinfo("Python TK","Gavin4433,Email:Gavin_2009@163.com")



file = ''

menubar = Menu(window)
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=load, accelerator='Ctrl+O')
filemenu.add_command(label="保存", command=save2, accelerator='Ctrl+S')
filemenu.add_command(label="另存为", command=save)
filemenu.add_separator()
filemenu.add_command(label="退出", command=e)
menubar.add_cascade(label="文件", menu=filemenu)
timetable = Menu(menubar, tearoff=False)
timetable.add_command(label="时间",command=prints7)
timetable.add_command(label="日期",command=prints3)
menubar.add_cascade(label="杂项", menu=timetable)
about = Menu(menubar, tearoff=False)
about.add_command(label="版本",command=prints2)
about.add_command(label="作者",command=author)
about.add_command(label="语言",command=lang)
menubar.add_cascade(label="关于", menu=about)
# 显示菜单
window.config(menu=menubar)
window.bind("<Control-o>", lambda event: load())
window.bind("<Control-s>", lambda event: save2())
mainloop()

from tkinter.simpledialog import askstring
window = Tk()
window.title("Our Time Editor1.18(None)")
cont = ScrolledText()
cont.pack(side=BOTTOM)
langfile = '' 
def load():
      global file,window
      asd = askopenfilename(filetypes=[("Text File","txt")])
      file = copy.copy(asd)
      try:
        with open(asd,'r') as f:
             global cont
             cont.delete("1.0",END)
             cont.insert(INSERT,f.read())
      except:
            showerror("错误","错误的文件名!!!")
      window.title("Editor 1.18(" + file + ")")
def save():
      global cont,file
      asd = asksaveasfilename(filetypes=[("Text File","txt")])
      
      file = copy.copy(asd)
      if file =='':
            showerror("文件名不能为空!")
            return
      try:
          with open(asd,'w') as f:
             f.write(cont.get("1.0",END))
      except:
            showerror("Python TK","写入失败!!!")
      file=''
def save2():
      global file
      try:
        with open(file,'w') as f:
             f.write(cont.get("1.0",END))
      except:
            showerror("Python TK","写入失败!!!")
def prints2():
      showinfo("版本","1.18.2.7(V1)")
def prints3():
      datea = d.datetime.today()
      year = datea.year
      month = datea.month
      day = datea.day
      showinfo("date",str(year) + '年' + str(month) +'月' + str(day) + "日")

def e():
      esc = askquestion("Python TK","你想退出吗?")
      if esc == 'yes':
            sys.exit()
      else:
            return
def prints7():
      datea = d.datetime.today()
      hour = datea.hour
      minutes = datea.minute
      showinfo("time",str(hour) + ' : ' + str(minutes))
def author():
      showinfo("Python TK","Gavin4433,Email:Gavin_2009@163.com")



file = ''

menubar = Menu(window)
# 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="打开", command=load, accelerator='Ctrl+O')
filemenu.add_command(label="保存", command=save2, accelerator='Ctrl+S')
filemenu.add_command(label="另存为", command=save)
filemenu.add_separator()
filemenu.add_command(label="退出", command=e)
menubar.add_cascade(label="文件", menu=filemenu)
timetable = Menu(menubar, tearoff=False)
timetable.add_command(label="时间",command=prints7)
timetable.add_command(label="日期",command=prints3)
menubar.add_cascade(label="杂项", menu=timetable)
about = Menu(menubar, tearoff=False)
about.add_command(label="版本",command=prints2)
about.add_command(label="作者",command=author)
about.add_command(label="语言",command=lang)
menubar.add_cascade(label="关于", menu=about)
# 显示菜单
window.config(menu=menubar)
window.bind("<Control-o>", lambda event: load())
window.bind("<Control-s>", lambda event: save2())
mainloop()
#something good ...
