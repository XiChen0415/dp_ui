import tkinter as tk
import tkinter.messagebox as mbox
import base64
import os
# from StartPage import *


class MainFrame(tk.Frame):
    def __init__(self, master):
        self.root = master
        self.root.title('数据收集及处理工具')
        self.root.geometry('800x600')
        # self.root.iconbitmap("./logo.icns")
        MainPage(self.root)


class MainPage():
    def __init__(self, master):
        self.master = master
        self.MainPage = tk.Frame(self.master,)
        self.MainPage.pack()
        # master.title('数据收集及处理工具')
        # master.geometry('800x600')
        tk.Button(self.MainPage,
                  text="数据收集",
                  # height=5,
                  width=40,
                  command=self.switch_1).pack()
        tk.Button(self.MainPage,
                  text="数据处理",
                  # height=5,
                  width=40,
                  command=self.switch_2).pack()
        tk.Button(self.MainPage,
                  text="数据检验",
                  # height=5,
                  width=40,
                  command=self.switch_3).pack()
        tk.Button(self.MainPage,
                  text="退出",
                  # height=5,
                  width=40,
                  command=self.quit).pack()

    def switch_1(self,):
        self.MainPage.destroy()
        DataCollect(self.master)

    def switch_2(self,):
        self.MainPage.destroy()
        DataProcess(self.master)

    def switch_3(self,):
        self.MainPage.destroy()
        DataValidate(self.master)

    def quit(self):
        quit_bool = mbox.askokcancel('提示', '确定要退出吗？')
        if quit_bool is True:
            root.destroy()


class DataCollect(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.DataCollect = tk.Frame(self.master,)
        self.DataCollect.pack()
        tk.Label(self.DataCollect,
                 text='数据收集').pack()
        tk.Button(self.DataCollect,
                  width=40,
                  text='设备端存图下载',
                  command=tk.DISABLED).pack()
        tk.Button(self.DataCollect,
                  width=40,
                  text='视频截取',
                  command=tk.DISABLED).pack()
        tk.Button(self.DataCollect,
                  width=40,
                  text='返回上一层',
                  command=self.back_to_main).pack()

    def back_to_main(self):
        self.DataCollect.destroy()
        MainPage(self.master)


class DataProcess(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.DataProcess = tk.Frame(self.master,)
        self.DataProcess.pack()
        tk.Label(self.DataProcess,
                 text='数据处理').pack()
        tk.Button(self.DataProcess,
                  width=40,
                  text='图片裁剪',
                  command=tk.DISABLED).pack()
        tk.Button(self.DataProcess,
                  width=40,
                  text='图片翻转',
                  command=tk.DISABLED).pack()
        tk.Button(self.DataProcess,
                  width=40,
                  text='返回上一层',
                  command=self.back_to_main).pack()

    def back_to_main(self):
        self.DataProcess.destroy()
        MainPage(self.master)


class DataValidate(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.DataValidate = tk.Frame(self.master,)
        self.DataValidate.pack()
        tk.Label(self.DataValidate,
                 text='数据检验').pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='人体框任务',
                  command=tk.DISABLED).pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='关节点任务',
                  command=tk.DISABLED).pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='返回上一层',
                  command=self.back_to_main).pack()

    def back_to_main(self):
        self.DataValidate.destroy()
        MainPage(self.master)


if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
