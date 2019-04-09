﻿#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys,time,pygame
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    import tkinter.filedialog as tkFileDialog
    import tkinter.simpledialog as tkSimpleDialog    #askstring()
    import tkinter

folder = ''
res = []
num = 0
now_music = ''





class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Myazure音乐播放器DesignedByWangZhen<wangzhenjjcn@gmail.com>')
        self.master.geometry('837x494')
        self.master.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('NextSong.TButton',font=('宋体',9))
        self.NextSong = Button(self.top, text='下一首', command=self.NextSong_Cmd, style='NextSong.TButton')
        self.NextSong.place(relx=0.459, rely=0.081, relwidth=0.106, relheight=0.067)

        self.style.configure('PreSong.TButton',font=('宋体',9))
        self.PreSong = Button(self.top, text='上一首', command=self.PreSong_Cmd, style='PreSong.TButton')
        self.PreSong.place(relx=0.344, rely=0.081, relwidth=0.106, relheight=0.067)

        self.style.configure('Stop.TButton',font=('宋体',9))
        self.Stop = Button(self.top, text='停止', command=self.Stop_Cmd, style='Stop.TButton')
        self.Stop.place(relx=0.229, rely=0.081, relwidth=0.106, relheight=0.067)

        self.style.configure('Play.TButton',font=('宋体',9))
        self.Play = Button(self.top, text='播放', command=self.Play_Cmd, style='Play.TButton')
        self.Play.place(relx=0.115, rely=0.081, relwidth=0.106, relheight=0.067)

        self.style.configure('OpenPath.TButton',font=('宋体',9))
        self.OpenPath = Button(self.top, text='打开', command=self.OpenPath_Cmd, style='OpenPath.TButton')
        self.OpenPath.place(relx=0., rely=0.081, relwidth=0.106, relheight=0.067)

        self.Text1Var = StringVar(value='')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=('宋体',9))
        self.Text1.place(relx=0., rely=0., relwidth=0.909, relheight=0.051)

        self.style.configure('Search.TButton',font=('宋体',9))
        self.Search = Button(self.top, text='搜索', command=self.Search_Cmd, style='Search.TButton')
        self.Search.place(relx=0.908, rely=0., relwidth=0.102, relheight=0.054)

        self.ResaultBoxVar = StringVar(value='ResaultBox')
        self.ResaultBoxFont = Font(font=('宋体',9))
        self.ResaultBox = Listbox(self.top, listvariable=self.ResaultBoxVar, font=self.ResaultBoxFont)
        self.ResaultBox.place(relx=0., rely=0.162, relwidth=1.005, relheight=0.785)

        self.style.configure('Line1.TSeparator',background='#000000')
        self.Line1 = Separator(self.top, orient='horizontal', style='Line1.TSeparator')
        self.Line1.place(relx=0., rely=0.065, relwidth=1.004, relheight=0.002)

        self.style.configure('CopyRight.TLabel',anchor='w', font=('宋体',9))
        self.CopyRight = Label(self.top, text='DesignedByWangZhen', style='CopyRight.TLabel')
        self.CopyRight.place(relx=0., rely=0.972, relwidth=0.135, relheight=0.034)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def NextSong_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("NextSong_Cmd")
        pass

    def PreSong_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("PreSong_Cmd")
        pass

    def Stop_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("Stop_Cmd")
        pass

    def Play_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("Play_Cmd")
        pass

    def OpenPath_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("OpenPath_Cmd")
        global folder
        global res
        if not folder:
            folder = tkFileDialog.askdirectory()
            musics = [folder + '\\' + music
                    for music in os.listdir(folder) \
                            \
                    if music.endswith(('.mp3', '.wav', '.ogg'))]
            res = musics
            print(res)
        if not folder:
            return
        playing = True
        if len(res):
            pygame.mixer.init()
        global num
        while playing:
            if not pygame.mixer.music.get_busy():
                # 随机播放一首歌曲
                nextMusic = res[num]
                print(nextMusic)
                print(num)
                pygame.mixer.music.load(nextMusic.encode())
                # 播放一次
                pygame.mixer.music.play(1)
                #print(len(res)-1)
                if len(res)-1 == num:
                    num = 0
                else:
                    num = num + 1
                nextMusic = nextMusic.split('\\')[1:]
                print('playing....' + ''.join(nextMusic))
            else:
                time.sleep(0.1)
        #     ret = []
        #     for i in musics:
        #         ret.append(i.split('\\')[1:])
        #         res.append(i.replace('\\','/'))
        #     var2 = tkinter.StringVar()
        #     var2.set(ret)
        #     print (var2)
        # global playing
        # playing = True
        # 根据情况禁用和启用相应的按钮
        # buttonPlay['state'] = 'normal'
        # buttonStop['state'] = 'normal'
        # buttonPause['state'] = 'normal'
        # pause_resume.set('播放')
        pass

    def Search_Cmd(self, event=None):
        #TODO, Please finish the function here!
        print("Search_Cmd")
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
