import tkinter as tk
import tkinter.messagebox as mbox
import os
import tkinter.filedialog
from tkinter import StringVar, IntVar
import cv2
from PIL import Image, ImageTk


class MainFrame(tk.Frame):
    def __init__(self, master):
        self.root = master
        self.root.title('数据收集及处理工具')
        self.root.geometry('1480x1224')
        # self.root.iconbitmap("./logo.icns")
        MainPage(self.root)


class MainPage():
    def __init__(self, master):
        self.master = master
        self.MainPage = tk.Frame(self.master,)
        self.MainPage.pack()
        tk.Label(self.MainPage,
                 text="选择你要使用的工具：                                                                   ",
                 fg='red'
                 ).pack()
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
        DataCollect(self.master, text=None)

    def switch_2(self,):
        self.MainPage.destroy()
        DataProcess(self.master)

    def switch_3(self,):
        self.MainPage.destroy()
        DataValidate(self.master, img_lb=None, filepath=None)

    def quit(self):
        # quit_bool = mbox.askokcancel('提示', '确定要退出吗？')
        # if quit_bool is True:
        root.destroy()


class DataCollect(tk.Frame):
    def __init__(self, master, text):
        self.master = master
        self.DataCollect = tk.Frame(self.master,)
        self.DataCollect.pack()
        self.text = StringVar()
        tk.Label(self.DataCollect,
                 text='数据收集').pack()
        tk.Button(self.DataCollect,
                  width=40,
                  text='设备端存图下载',
                  command=self.download_from_device).pack()
        tk.Button(self.DataCollect,
                  width=40,
                  text='视频截取',
                  command=self.capture_video).pack()
        tk.Label(self.DataCollect, textvariable=self.text).pack()
        tk.Button(self.DataCollect,
                  width=30,
                  text='返回上一层',
                  command=self.back_to_main).pack()

    def back_to_main(self):
        self.DataCollect.destroy()
        MainPage(self.master)

    def download_from_device(self):
        mbox.showinfo(title="待补全", message="功能待补全")

    def capture_video(self):
        filepath = tk.filedialog.askdirectory()
        if filepath != '':
            self.text.set("您选择的文件是:"+filepath)
            # tk.Button(self.DataCollect, text='确认开始', command=tk.DISABLED).pack()
        else:
            self.text.set("您没有选择任何文件！")
            btn.destroy()


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
                  command=self.CropPicture).pack()
        tk.Button(self.DataProcess,
                  width=40,
                  text='图片翻转',
                  command=self.FlipPicture).pack()
        tk.Button(self.DataProcess,
                  width=40,
                  text='返回上一层',
                  command=self.back_to_main).pack()

    def back_to_main(self):
        self.DataProcess.destroy()
        MainPage(self.master)

    def CropPicture(self):
        mbox.showinfo(title="待补全", message="功能待补全")

    def FlipPicture(self):
        mbox.showinfo(title="待补全", message="功能待补全")


class DataValidate(tk.Frame):
    def __init__(self, master, img_lb, filepath):
        self.master = master
        self.DataValidate = tk.Frame(self.master,)
        self.DataValidate.pack()
        self.filepath = StringVar()
        self.img_lb = tk.Label(self.DataValidate)
        tk.Label(self.DataValidate,
                 text='数据检验').pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='人体框任务',
                  command=self.det_validate).pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='关节点任务',
                  command=tk.DISABLED).pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='返回上一层',
                  command=self.back_to_main).pack()
        self.img_lb.pack()

    def back_to_main(self):
        self.DataValidate.destroy()
        MainPage(self.master)

    def det_validate(self):
        mbox.showinfo(title="待补全", message="功能待补全")
        self.filepath = '../fiture_dataset/2020_Det_1/Det_1.jpeg'
        img = cv2.imread(self.filepath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=img)
        # tk.Label(self.DataValidate, image=imgtk).pack()
        self.img_lb.config(image=imgtk)
        self.img_lb.image = imgtk

    def pose_validate(self):
        mbox.showinfo(title="待补全", message="功能待补全")


if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
