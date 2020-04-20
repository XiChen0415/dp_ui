import tkinter as tk
import tkinter.messagebox as mbox
import os, shutil
import tkinter.filedialog
from tkinter import StringVar, IntVar
import cv2
from PIL import Image, ImageTk, ImageDraw, ImageFont
import numpy as np
import sys
import json


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
                 text="选择你要使用的工具：",
                 font=("Arial", 16),
                 fg='red'
                 ).pack()
        tk.Button(self.MainPage,
                  text="数据收集",
                  height=5,
                  width=40,
                  font=("Arial", 16),
                  command=self.switch_1).pack()
        tk.Button(self.MainPage,
                  text="数据处理",
                  height=5,
                  width=40,
                  font=("Arial", 16),
                  command=self.switch_2).pack()
        tk.Button(self.MainPage,
                  text="数据检验",
                  height=5,
                  width=40,
                  font=("Arial", 16),
                  command=self.switch_3).pack()
        tk.Button(self.MainPage,
                  text="退出",
                  height=5,
                  width=40,
                  font=("Arial", 16),
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
                  width=40, height=5,
                  text='设备端存图下载',
                  font=("Arial", 16),
                  command=self.download_from_device).pack()
        tk.Button(self.DataCollect,
                  width=40, height=5,
                  text='视频截取',
                  font=("Arial", 16),
                  command=self.capture_video).pack()
        tk.Label(self.DataCollect, textvariable=self.text).pack()
        tk.Button(self.DataCollect,
                  width=30, height=5,
                  text='返回上一层',
                  font=("Arial", 16),
                  command=self.back_to_main).pack()

    def back_to_main(self):
        self.DataCollect.destroy()
        MainPage(self.master)

    def download_from_device(self):
        mbox.showinfo(title="待补全", message="功能待补全")

    def capture_video(self):
        file_path = tk.filedialog.askdirectory()
        if file_path != '':
            # file_path = '/Users/xiaoge/Downloads/video1/'
            self.text.set("您选择的文件是:"+file_path)
        files = os.listdir(file_path)
        i = 1
        # vc = cv2.VideoCapture(file_path+files[0])
        for video_file in files:
            if video_file != '.DS_Store':
                vc = cv2.VideoCapture(file_path+video_file)
                if vc.isOpened():
                    rval, frame = vc.read()
                else:
                    rval = False
                timeF = 300
                f = 1
                while rval:
                    rval, frame = vc.read()
                    if (f % timeF == 0) & (frame is not None):
                        cv2.imwrite('/Users/xiaoge/Downloads/pic1/'+str(i)+'.jpg', frame)
                        i = i+1
                    f = f+1
                    cv2.waitKey(1)
                vc.release()
            tk.Button(self.DataCollect, text='确认开始', command=tk.DISABLED).pack()
        # else:
        # self.text.set("您没有选择任何文件！")
        # btn.destroy()


class DataProcess(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.DataProcess = tk.Frame(self.master,)
        self.DataProcess.pack()
        tk.Label(self.DataProcess,
                 text='数据处理').pack()
        tk.Button(self.DataProcess,
                  width=40, height=5,
                  text='图片裁剪',
                  font=("Arial", 16),
                  command=self.CropPicture).pack()
        tk.Button(self.DataProcess,
                  width=40, height=5,
                  font=("Arial", 16),
                  text='图片翻转',
                  command=self.FlipPicture).pack()
        tk.Button(self.DataProcess,
                  width=40, height=5,
                  font=("Arial", 16),
                  text='返回上一层',
                  command=self.back_to_main).pack()

    def back_to_main(self):
        self.DataProcess.destroy()
        MainPage(self.master)

    def CropPicture(self):
        mbox.showinfo(title="待补全", message="功能待补全")

    def FlipPicture(self):
        # mbox.showinfo(title="待补全", message="功能待补全")
        path = "/Users/xiaoge/Downloads/pic/"
        # self.text.set("您选择的文件是:"+file_path)

        def rotate_bound(image, angle):
            (h, w) = image.shape[:2]
            (cX, cY) = (w//2, h//2)
            M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])

            nW = int((h * sin) + (w * cos))
            nH = int((h * cos) + (w * sin))

            M[0, 2] += (nW / 2) - cX
            M[1, 2] += (nH / 2) - cY
            return cv2.warpAffine(image, M, (nW, nH))

        def rotate_image(raw_img_path, save_img_path, angle):
            file_path = raw_img_path
            files = os.listdir(file_path)
            for filename in files:
                if not os.path.isdir(filename):
                    _file = file_path+filename
                    img = cv2.imread(_file)
                    if img is not None:
                        img_rotate = rotate_bound(img, angle)
                        save_file_path = save_img_path + filename
                        cv2.imwrite(save_file_path, img_rotate)
        # if __name__ == '__main__':
        raw_img_path = path
        save_img_path = '/Users/xiaoge/Downloads/fan/'
        shutil.rmtree(save_img_path)
        os.mkdir(save_img_path)
        rotate_image(raw_img_path, save_img_path, 90)


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
                  font=("Arial", 16),
                  command=self.Det_validate).pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='关节点任务',
                  font=("Arial", 16),
                  command=self.Pose_validate).pack()
        tk.Button(self.DataValidate,
                  width=40,
                  text='返回上一层',
                  font=("Arial", 16),
                  command=self.back_to_main).pack()
        self.img_lb.pack()

    def back_to_main(self):
        self.DataValidate.destroy()
        MainPage(self.master)

    def Det_validate(self):
        # mbox.showinfo(title="待补全", message="功能待补全")
        filepath = '/Users/xiaoge/Downloads/Fiture_dataset/Det_04.json'
        json_file = open(filepath, 'r')
        annot = json.loads(json_file.read())
        # 循环 imgpath = []
        # print(len(annot['info']))
        count = 0
        compare = 'Det'
        pos = []
        for e in annot['images']:
            if e['file_name'][0:3] == compare:
                pos.append(count)
            count += 1

        count_ant = 0
        cnt = 0
        for e in annot['annotations']:
            cnt += 1
            if cnt == 10:
                for d in annot['images']:
                    if d['id'] == e['image_id']:
                        file_name = d['file_name']
                        window_name = d['file_name']
                        img = cv2.imread('/Users/xiaoge/Downloads/Fiture_dataset/2020-Jan-2/' + file_name)
                        cnt += 1
                        p1_x = annt['bbox'][0]
                        p1_y = annt['bbox'][1]
                        p2_x = p1_x + annt['bbox'][2]
                        p2_y = p1_y + annt['bbox'][3]
                        cv2.rectangle(img, (p1_x, p1_y), (p2_x, p2_y), (0, 0, 255), 4)
                        cv2.namedWindow('image_window')
                        img_height = img.shape[0]
                        img_width = img.shape[1]
                        cv2.putText(img, window_name, (0, img_height-50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)
                        cv2.imshow('image_window', img)
                        cv2.waitKey(0)
                cv2.destroyAllWindows()
                cnt = 0

    def Pose_validate(self):
        file_path = '/Users/xiaoge/Downloads/Fiture_dataset/Pose.json'
        json_file = open(file_path, 'r')
        annot = json.loads(json_file.read())
        cnt = 0
        for e in annot['annolist']:
            cnt += 1
            if cnt == 10:
                file_name = e['imgdix']+'.jpg'
                img = cv2.imread('/Users/xiaoge/Downloads/Fiture_dataset/2020-Jan-1/'+file_name)
                img_height = img.shape[0]
                img_width = img.shape[1]
                if img_height == 550 or img_height == 720:
                        circle_size = 4
                        text_size = 0.5
                        text_width = 1
                        text_position = 25
                if img_height == 1920:
                        circle_size = 10
                        text_size = 1
                        text_width = 2
                        text_position = 50
                pose_list = []
                for keypoints in e['annopoints']:
                    x = int(keypoints['x'])
                    y = int(keypoints['y'])
                    # if keypoints['is_visible']==1:
                    pose_list.append((x, y))
                    cv2.circle(img, (x, y), circle_size, (0, 0, 255), -1)
                    # cv2.putText(img, str(keypoints['id']), (x+10,y+text_position), cv2.FONT_HERSHEY_COMPLEX, text_size, (0, 0, 255), text_width)

                pairs = [[0, 1], [1, 2], [3, 4], [4, 5], [2, 6], [3, 6], [6, 7], [7, 8], [7, 9], [9, 10], [10, 11], [7, 12], [12, 13], [13, 14]]
                for (p1, p2) in pairs:
                    if (pose_list[p1] is not None) & (pose_list[p2] is not None):
                        cv2.line(img, pose_list[p1], pose_list[p2], (0, 0, 255), thickness=2)

                cv2.namedWindow('image_window')
                cv2.putText(img, name, (0, img_height-50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)
                cv2.imshow('image_window', img)
                if cv2.waitKey(0) == 27:
                    break
                cv2.destroyAllWindows()
                cnt = 0


if __name__ == "__main__":
    root = tk.Tk()
    MainFrame(root)
    root.mainloop()
