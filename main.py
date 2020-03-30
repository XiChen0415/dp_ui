import tkinter as tk
import tkinter.messagebox as mbox


class MainUI(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('数据收集及处理工具')
        self.master.geometry('800x600')
        self.pack()
        self.createWidgets()
        self.master.mainloop()

    def createWidgets(self):
        # self.firstLabel = tk.Label(self, text="数据收集及处理脚本")
        # self.firstLabel.pack()
        self.clickButton = tk.Button(self, text="请选择", command=self.answer)
        self.main_btn_1 = tk.Button(self,
                                    text="数据收集",
                                    # height=5,
                                    width=40,
                                    command=tk.DISABLED)
        self.main_btn_2 = tk.Button(self,
                                    text="数据处理",
                                    # height=5,
                                    width=40,
                                    command=tk.DISABLED)
        self.main_btn_3 = tk.Button(self,
                                    text="数据检验",
                                    # height=5,
                                    width=40,
                                    command=tk.DISABLED)
        self.main_btn_4 = tk.Button(self,
                                    text="退出",
                                    # height=5,
                                    width=40,
                                    command=self.quit)
        self.clickButton.pack()
        self.main_btn_1.pack()
        self.main_btn_2.pack()
        self.main_btn_3.pack()
        self.main_btn_4.pack()

    def answer(self):
        mbox.showinfo("hi")

    def quit(self):
        quit_bool = mbox.askokcancel('提示', '确定要退出吗？')
        if quit_bool is True:
            self.master.destroy()


if __name__ == "__main__":
    app = MainUI()
