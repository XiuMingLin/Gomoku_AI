import requests
import json
import numpy

'http://202.207.12.223:8000/context/701672826a45d8d2d998b3a3f66166bf'

url = 'http://202.207.12.223:8000/step_08'
responce = requests.get(url)
print(responce.text)

board_json = json.loads(responce.text)
board_list = board_json['questions']

board = numpy.empty((15, 15), dtype=numpy.str)

score = {10000, 6000, 5000, 2500, 2000, 400, 400, 200, 50, 20}
score_str0 = {'CMMMM', 'MCMMM', 'MMCMM', 'MMMCM', 'MMMMC'}
score_str1 = {'OOOOC', 'COOOO'}
score_str2 = {'.CMMM.', '.MCMM.', '.MMCM.', '.MMMC.'}
score_str3 = {'COOO.', '.OOOC', '.OOCO.', '.OCOO'}
score_str4 = {'OCMMM.', 'OMCMM.', 'OMMCM.', 'OMMMC.', '.CMMMO', '.MCMMO', '.MMCMO', '.MMMCO'}
score_str5 = {'.MMC', '.MCM', '.CMM'}
score_str6 = {'.OOC', 'COO,', 'MOOOC', 'COOOM'}
score_str7 = {'.MMCO', '.MCMO', '.CMMO', 'OMMC.', 'OMCM.', 'OCMM.', 'MOOC', 'COOM'}
score_str8 = {'.MC.', '.CM.'}

def change_board(x, y, type):
    s = ''
    if type == 1:
        if y >= 0 and y <=14 and x >=0 and x <=14:
            board[x][y] = 'x'
    elif type == 2:
        if y >= 0 and y <=14 and x >=0 and x <=14:
            board[x][y] = 'o'
    for i in range(15):
        for j in range(15):
            s += board[i][j]
    return s

def init_board():
    for i in range(15):
        for j in range(15):
            board[i][j] = '.'


def init_board2(board_str):
    j = 0
    for i in range(0, len(board_str), 2):
        if j == 0:
            change_board(ord(board_str[i]) - ord('a'), ord(board_str[i+1]) - ord('a'), 1)
            j = 1
        elif j == 1:
            change_board(ord(board_str[i]) - ord('a'), ord(board_str[i+1]) - ord('a'), 2)
            j = 0


def change_board_2(type):
    if type == 1:
        for i in range(15):
            for j in range(15):
                if board[i][j] == 'x':
                    board[i][j] = 'M'
                if board[i][j] == 'o':
                    board[i][j] = 'O'
    elif type == 2:
        for i in range(15):
            for j in range(15):
                if board[i][j] == 'x':
                    board[i][j] = 'O'
                if board[i][j] == 'o':
                    board[i][j] = 'M'


def check_chess_type(x, y, type):
    one_chess_shape = ''
    if type == 1:
        for i in range(-4, 5):
            if y + i < 0 or y + i >= 15:
                continue
            if board[x][y+i] == 'C':
                one_chess_shape += 'C'
            if board[x][y+i] == '.':
                one_chess_shape += '.'
            if board[x][y+i] == 'O':
                one_chess_shape += 'O'
            if board[x][y+i] == 'M':
                one_chess_shape += 'M'
        return one_chess_shape
    if type == 2:
        for i in range(-4, 5):
            if y + i < 0 or y + i >= 15 or x + i < 0 or x + i >= 15:
                continue
            if board[x+i][y+i] == 'C':
                one_chess_shape += 'C'
            if board[x+i][y+i] == '.':
                one_chess_shape += '.'
            if board[x+i][y+i] == 'O':
                one_chess_shape += 'O'
            if board[x+i][y+i] == 'M':
                one_chess_shape += 'M'
        return one_chess_shape
    if type == 3:
        for i in range(-4, 5):
            if x + i < 0 or x + i >= 15:
                continue
            if board[x+i][y] == 'C':
                one_chess_shape += 'C'
            if board[x+i][y] == '.':
                one_chess_shape += '.'
            if board[x+i][y] == 'O':
                one_chess_shape += 'O'
            if board[x+i][y] == 'M':
                one_chess_shape += 'M'
        return one_chess_shape
    if type == 4:
        for i in range(-4, 5):
            if y - i < 0 or y - i >= 15 or x + i < 0 or x + i >= 15:
                continue
            if board[x+i][y-i] == 'C':
                one_chess_shape += 'C'
            if board[x+i][y-i] == '.':
                one_chess_shape += '.'
            if board[x+i][y-i] == 'O':
                one_chess_shape += 'O'
            if board[x+i][y-i] == 'M':
                one_chess_shape += 'M'
        return one_chess_shape


def find_score(str_board_type):
    max = 0
    total_score = 0
    for i in range(len(score_str0)):
        if str_board_type.find(score_str0[i]) != -1:
            total_score += score[0]
    for i in range(len(score_str1)):
        if str_board_type.find(score_str1[i]) != -1:
            total_score += score[1]
    for i in range(len(score_str2)):
        if str_board_type.find(score_str2[i]) != -1:
            total_score += score[2]
    for i in range(len(score_str3)):
        if str_board_type.find(score_str3[i]) != -1:
            total_score += score[3]
    for i in range(len(score_str4)):
        if str_board_type.find(score_str4[i]) != -1:
            total_score += score[4]
    for i in range(len(score_str5)):
        if str_board_type.find(score_str5[i]) != -1:
            total_score += score[5]
    for i in range(len(score_str6)):
        if str_board_type.find(score_str6[i]) != -1:
            total_score += score[6]
    for i in range(len(score_str7)):
        if str_board_type.find(score_str7[i]) != -1:
            total_score += score[7]
    for i in range(len(score_str8)):
        if str_board_type.find(score_str8[i]) != -1:
            total_score += score[8]

    return total_score


def set_score(board_str):
    init_board()
    init_board2(board_str)
    if (len(board_str) // 2) % 2 == 0:
        change_board_2(1)
    else:
        change_board_2(2)

    for i in range(15):
        for j in range(15):
            if board[i][j] == '.':
                board[i][j] = 'C'
                print(check_chess_type(i, j, 1))
                find_score(check_chess_type(i, j, 1))
                board[i][j] = '.'
                # print(check_chess_type(i, j, 2))
                # print(check_chess_type(i, j, 3))
                # print(check_chess_type(i, j, 4))


set_score(board_list[0])