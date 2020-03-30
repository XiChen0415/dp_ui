import tkinter as tk
from main import *


class StartPage(tk.Frame):
    def __init__(self, master=None):
        self.root = master
        self.root.title('数据收集及处理工具')
        self.root.geometry('800x600')
        self.createWidgets()

    def createWidgets(self):
        self.page = Frame(self.root)
        self.page.pack()
        self.clickButton = tk.Button(self, text="请选择", command=self.answer)
        self.clickButton.pack()

    def answer(self):
        mbox.showinfo("hi")


class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title('数据收集及处理工具')
        master.geometry('800x600')
        tk.Button(self,
                  text="数据收集",
                  # height=5,
                  width=40,
                  command=lambda: self.switch_frame(DataCollect).pack()).pack()
        tk.Button(self,
                  text="数据处理",
                  # height=5,
                  width=40,
                  command=tk.DISABLED).pack()
        tk.Button(self,
                  text="数据检验",
                  # height=5,
                  width=40,
                  command=tk.DISABLED).pack()
        tk.Button(self,
                  text="退出",
                  # height=5,
                  width=40,
                  command=self.quit).pack()

    def quit(self):
        quit_bool = mbox.askokcancel('提示', '确定要退出吗？')
        if quit_bool is True:
            self.destroy()
