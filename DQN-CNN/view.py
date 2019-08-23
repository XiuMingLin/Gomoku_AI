from tkinter import *
import tkinter.messagebox
from environment import env
import numpy as np
import time
from CNN_DQN import DeepQNetwork

'''
tkinter界面
'''
space = 255
space_col = 15

class view(tkinter.Tk):
    def __init__(self):
        self.gameStart = False
        self.status = False
        self.reward = 0
        super(view, self).__init__()
        self.n_actions = 256
        self.n_features = 256
        self.doneList = []
        self.allphoto = []
        self.initView()
        self.env = env()
        self.wobservation = None
        self.wobservation_ = None
        self.actions1 = None
        self.RL = DeepQNetwork(self.n_actions, self.n_features)

    def initView(self):
        def buttonCallBack():
            self.RL.getvarriable()      # 没有
            self.gameStart = True
            if len(self.allphoto) > 0:
                for i in self.allphoto:
                    self.w.delete(i)

            self.allphoto.clear()
            self.doneList.clear()
            observation = self.env.reset()

        self.master = Tk()
        self.master.title('5z7')
        self.master.resizable(width=False, height=False)
        self.w = Canvas(self.master, bg="#FFFF0", width=700, height=630)
        for c in range(40, 490, 30):
            x0, y0, x1, y1 = c, 40, c, 580

    def callback(self, event):
        if self.gameStart:
            mouse_x = event.x
            mouse_y = event.y
            if 470 > mouse_x > 20 and 470 > mouse_y > 20:
                a = round((mouse_x - 40) / 30)
                b = round((mouse_y - 40) / 30)
                action = b * 15 + a
                observation = self.getdouble(np.reshape(np.copy(self.env.qipan), [1, space]))
                bobservation = self.transfore(observation)
                qipan, observation_, reward, done = self.step(action, 'Black')


    def show(self, action, flag):
        y = (action // 15) * 30 + 40
        x = (action % 15) * 30 + 40
        if flag == 'Black':
            a = self.w.cr               # 未完成

    def setPosition(self, action, flag):
        if action in self.doneList:
            tkinter.messagebox.showinfo(title='提示', message='当前位置不可下')
        else:
            self.doneList.append(action)
            self.show(action, flag)

    def step(self, action, flag):
        p1 = self.env.pwb(flag)
        p2 = self.env.pwn(action, flag)

        s = p2 - p1
        print("该步的回报值：%d", s)
        self.setPosition(action, flag)          # 未完成

    def transfore(self, observation):
        s1 = observation[0, :space]
        s2 = observation[0, space:]
        s = np.hstack((s1, s2))
        return s

    def getdouble(self, qipan):
        w_qipan = np.zeros([1, space])
        b_qipan = np.zeros([1, space])
        w_array = np.where(qipan == 1)[1]
        b_array = np.where(qipan == 2)[1]
        w_qipan[0, w_array] = 1
        b_qipan[0, b_array] = 1
        s = np.hstack((w_qipan, b_qipan))
        return s