'''
计算下一步的回报，以及结束
'''

import numpy as np

UNIT = 40
height = 15         # 棋盘高度
weight = 15         # 棋盘宽度
value1=50000        # *****
value2=4320         # +****+ 会算成两次下面
value3=720          # -****+   or  +****-
value4=720          # +***+
value5=720          # -***++   or  ++***-  +**+* *+**+
value6=120          # ++**+   0r  +**++  不计算**+++这种
value7=720          # **+**     or *+***  or ***+*
value8=720          # *++**  or **++*
value9=0            # *+*+*
value10=1000


class env():
    def __init__(self):
        # 初始化环境
        self.action_space = np.arange(256)              # 动作空间 [0,1,......,255] 255个0
        self.n_actions = 256                            # 动作可能的数量
        self.n_features = 256                           # 功能可能的数量  ？？？？？
        self.qipan = np.zeros([15, 15], dtype=np.int)   # 定义棋盘
        self.num1 = 0       # 白棋
        self.num2 = 0       # 黑棋
        self.done = False   # 棋局是否完成

    def reset(self):
        # 重置棋盘
        self.qipan = np.zeros([15, 15], dtype=np.int)   # 初始化棋盘
        self.done = False   # 重置棋局是否完成
        return np.copy(self.qipan)

    def pwn(self, action, flag):
        x = action // 15
        y = action % 15                 # ?????????????????????????????
        if flag == 'White':
            self.qipan[x, y] = 1
        else:
            self.qipan[x, y] = 2
        p2 = self.pww(flag)
        return p2

    def pww(self, flag):
        # 计算flag人赢得可能性
        self.num1 = 0   # 白棋x
        self.num2 = 0   # 黑棋o

        # 计算左斜线方向
        # 计算上半部分，长度为5
        for i in range(4, 15):
            for j in range(i-4+1):
                listcase = [self.qipan[j, i-j], self.qipan[j+1, i-j-1], self.qipan[j+2, i-j-2], self.qipan[j+3, i-j-3], self.qipan[j+4, i-j-4]]
                self.match(listcase)
        # 计算上半部分，长度为6
        for i in range(5, 15):
            for j in range(i-4):
                listcase = [self.qipan[j, i-j], self.qipan[j+1, i-j-1], self.qipan[j+2, i-j-2], self.qipan[j+3, i-j-3], self.qipan[j+4, i-j-4], self.qipan[j+5, i-j-5]]
                self.match(listcase)
        # 计算下半部分，长度为5
        for i in range(1, 11):
            for j in range(14, i + 4 - 1, -1):
                listcase = [self.qipan[i - j + 14, j], self.qipan[i - j + 15, j - 1], self.qipan[i - j + 16, j - 2],
                            self.qipan[i - j + 17, j - 3], self.qipan[i - j + 18, j - 4]]
                self.match(listcase)
        # 计算下半部分，长度为6
        for i in range(1, 11):
            for j in range(14, i + 4, -1):
                listcase = [self.qipan[i - j + 14, j], self.qipan[i - j + 15, j - 1], self.qipan[i - j + 16, j - 2],
                            self.qipan[i - j + 17, j - 3], self.qipan[i - j + 18, j - 4], self.qipan[i - j + 19, j - 5]]
        # 计算右斜线方向
        # 计算下半部分，长度为5
        for i in range(10, -1, -1):
            for j in range(i + 1):
                listcase = [self.qipan[i, j], self.qipan[i + 1, j + 1], self.qipan[i + 2, j + 2],
                            self.qipan[i + 3, j + 3], self.qipan[i + 4, j + 4]]
                self.match(listcase)
        # 计算上半部分，长度为5
        for j in range(1, 11):
            for i in range(11 - j):
                listcase = [self.qipan[i, j + i], self.qipan[i + 1, j + i + 1], self.qipan[i + 2, j + i + 2],
                            self.qipan[i + 3, j + i + 3], self.qipan[i + 4, j + i + 4]]
                self.match(listcase)
        # 计算上半部分，长度为6
        for j in range(1, 10):
            for i in range(14 - j):
                listcase = [self.qipan[i, j + i], self.qipan[i + 1, j + i + 1], self.qipan[i + 2, j + i + 2],
                            self.qipan[i + 3, j + i + 3], self.qipan[i + 4, j + i + 4], self.qipan[i + 5, j + i + 5]]
                self.match(listcase)
        # 计算下半部分，长度为6
        for i in range(9, -1, -1):
            for j in range(i + 1):
                listcase = [self.qipan[i, j], self.qipan[i + 1, j + 1], self.qipan[i + 2, j + 2],
                            self.qipan[i + 3, j + 3], self.qipan[i + 4, j + 4], self.qipan[i + 5, j + 5]]
                self.match(listcase)
        # 计算横方向
        # 长度为5
        for i in range(15):
            for j in range(11):
                listcase = [self.qipan[i, j], self.qipan[i, j + 1], self.qipan[i, j + 2], self.qipan[i, j + 3],
                            self.qipan[i, j + 4]]
                self.match(listcase)
        # 长度为6
        for i in range(15):
            for j in range(10):
                listcase = [self.qipan[i, j], self.qipan[i, j + 1], self.qipan[i, j + 2], self.qipan[i, j + 3],
                            self.qipan[i, j + 4], self.qipan[i, j + 5]]
                self.match(listcase)
        # 计算纵方向
        # 长度为5
        for j in range(15):
            for i in range(11):
                listcase = [self.qipan[i, j], self.qipan[i + 1, j], self.qipan[i + 2, j], self.qipan[i + 3, j],
                            self.qipan[i + 4, j]]
                self.match(listcase)
        # 长度为5
        for j in range(15):
            for i in range(10):
                listcase = [self.qipan[i, j], self.qipan[i + 1, j], self.qipan[i + 2, j], self.qipan[i + 3, j],
                            self.qipan[i + 4, j],
                            self.qipan[i + 5, j]]
                self.match(listcase)
        if flag == 'White':
            return self.num1 - self.num2
        else:
            return self.num2 - self.num1

    def pwb(self, flag):
        p1 = self.pww(flag)
        return p1

    def match(self, listcase):
        if len(listcase) == 5:
            if listcase in [[1,1,1,1,1]]:
                self.done = True
                self.num1 += value1
            elif listcase in [[2,2,2,2,2]]:
                self.done = True
                self.num2 += value1
            elif listcase in [[0,1,1,1,0],[0,1,1,0,1],[1,0,1,1,0],[1,1,1,0,0],[0,0,1,1,1]]:
                self.num1 += value4
            elif listcase in [[0,2,2,2,0],[0,2,2,0,2],[2,0,2,2,0],[2,2,2,0,0],[0,0,2,2,2]]:
                self.num2 += value4
            elif listcase in [[0,0,1,1,0],[0,1,1,0,0],[1,1,0,0,0]]:
                self.num1 += value6
            elif listcase in [[0,0,2,2,0],[0,2,2,0,0],[2,2,0,0,0]]:
                self.num2 += value6
            elif listcase in [[1,1,0,1,1],[1,0,1,1,1],[1,1,1,0,1],[1,1,1,1,0],[0,1,1,1,1]]:
                self.num1 += value10
            elif listcase in [[2,2,0,2,2],[2,0,2,2,2],[2,2,2,0,2],[2,2,2,2,0],[0,2,2,2,2]]:
                self.num2 += value10
            elif listcase in [[1,1,0,0,1],[1,0,0,1,1],[1,1,0,1,0]]:
                self.num1 += value8
            elif listcase in [[2,2,0,0,2],[2,0,0,2,2],[2,2,0,2,0]]:
                self.num2 += value8
            elif listcase in [[1,0,1,0,1]]:
                self.num1 += value9
            elif listcase in [[2,0,2,0,2]]:
                self.num2 += value9
            elif listcase in [[1,1,1,0,0],[0,0,1,1,1],[1,1,0,0,1],[1,1,0,1,0]]:
                self.num1 += value5
            elif listcase in [[2,2,2,0,0],[0,0,2,2,2],[2,2,0,0,2],[2,2,0,2,0]]:
                self.num2 += value5
        elif len(listcase) == 6:
            if listcase in [[0,1,1,1,1,0]]:
                self.num1 += value2
            elif listcase in [[0,2,2,2,2,0]]:
                self.num2 += value2
            elif listcase in [[2,1,1,1,1,0],[0,1,1,1,1,2]]:
                self.num1 += value3
            elif listcase in [[1,2,2,2,2,0],[0,2,2,2,2,1]]:
                self.num2 += value3
            elif listcase in [[1,2,2,2,0,0],[0,0,2,2,2,1]]:
                self.num2 += value5
            elif listcase in [[2,1,1,1,0,0],[0,0,1,1,1,2]]:
                self.num1 += value5