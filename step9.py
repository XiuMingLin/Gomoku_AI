import requests
import json
import numpy
import time

# 'http://202.207.12.223:8000/context/2e329756827e42330f7897cc9499588e'

visit_url = 'http://202.207.12.223:8000/join_game'
play_url = 'http://202.207.12.223:8000/play_game/'   # +id
check_url = 'http://202.207.12.223:8000/check_game/'


user = 'aqua'
password = '123321'

key = [65537,
       135261828916791946705313569652794581721330948863485438876915508683244111694485850733278569559191167660149469895899348939039437830613284874764820878002628686548956779897196112828969255650312573935871059275664474562666268163936821302832645284397530568872432109324825205567091066297960733513602409443790146687029]

board = numpy.empty((15, 15), dtype=numpy.str)
score_list = numpy.zeros((15, 15))
score = [850000, 600000, 30000, 3000, 2000, 800, 55, 35, 7, 0]
score_str0 = ["CMMMM", "MCMMM", "MMCMM", "MMMCM","MMMMC","MMMCM","M.MCM.M"]
score_str1 = ["OOOOC","COOOO","OOOCO","OOCOO","OCOOO"]
score_str2 = [".CMMM.",".MCMM.",".MMCM.",".MMMC.","MCM.M","M.MCM","C.MMM","MMM.C"]
score_str3 = ["COOO.",".OOOC",".OOCO.",".OCOO."]
score_str4 = ["OCMMM.","OMCMM.","OMMCM.","OMMMC.",".CMMMO",".MCMMO",".MMCMO",".MMMCO","O.MMC","O.MCM"]
score_str5 = [".MMC.",".MCM.",".CMM."]
score_str6 = [".OOC","COO.",".COO",".OCO"]
score_str7 = [".MMCO",".MCMO",".CMMO","OMMC.","OMCM.","OCMM.","MOOC","COOM"]
score_str8 = [".MC.",".CM."]
score_str9 = [".OOOOC","COOOO."]
my_score = 0
he_score = 0
iskome = 0
islose = 0
other_score = 0

is_success = ''
winner = ''
step = ''
creator = ''
ready = ''
current_turn = ''
current_stone = ''
left_time = ''
board_str = ''
last_step = ''
win_step = ''


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
    total_score = 20
    global iskome
    for i in range(len(score_str0)):
        if str_board_type.find(score_str0[i]) != -1:
            total_score += score[0]
    for i in range(len(score_str1)):
        if str_board_type.find(score_str1[i]) != -1:
            iskome = 1
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
    for i in range(len(score_str9)):
        if str_board_type.find(score_str9[i]) != -1:
            total_score += score[9]
    # print(total_score)
    return total_score


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


def set_score(board_str):
    global other_score
    init_board()
    init_board2(board_str)
    if (len(board_str) // 2) % 2 == 0:
        change_board_2(1)
    else:
        change_board_2(2)
    max_score = 0
    # print(board)
    for i in range(15):
        for j in range(15):
            if board[i][j] == '.':
                board[i][j] = 'C'
                # print(check_chess_type(i, j, 1))
                current_score = 0
                current_score += find_score(check_chess_type(i, j, 1))
                current_score += find_score(check_chess_type(i, j, 2))
                current_score += find_score(check_chess_type(i, j, 3))
                current_score += find_score(check_chess_type(i, j, 4))
                score_list[i][j] += current_score
                if max_score < current_score:
                    max_score = current_score
                board[i][j] = '.'
    other_score = max_score
    for i in range(15):
        for j in range(15):
            if score_list[i][j] == max_score:
                s = chr(i+ord('a')) + chr(j+ord('a'))
                return s
    s = ''
    return s


def str_2_num(x):
    return x[0] * (x[1] ** x[2])


def ksm(x):
    num = 1
    a = x[0]
    b = x[1]
    mode = x[2]
    a = a % mode
    while b != 0:
        if b & 1:
            num = (num * a) % mode
        b >>= 1
        a = (a * a) % mode
    return num


def DH(password):
    key_str_len = len(password)
    str2num = 0
    for i in range(key_str_len):
        array = [ord(password[i]), 256, key_str_len - 1 - i]
        str2num += str_2_num(array)

    str2num = [str2num] + key
    str2num = ksm(str2num)
    hex_str2num = hex(str2num)
    return hex_str2num


def init_json(json_str):
    global is_success
    global winner
    global step
    global creator
    global ready
    global current_turn
    global current_stone
    global left_time
    global board_str
    global last_step
    global win_step
    is_success = json_str['is_success']
    if is_success == 'false':
        return
    winner = json_str['winner']
    if winner == 'None':
        step = json_str['step']
        creator = json_str['creator']
        ready = json_str['ready']
        current_turn = json_str['current_turn']
        current_stone = json_str['current_stone']
        left_time = json_str['left_time']
        board_str = json_str['board']
        last_step = json_str['last_step']
        win_step = json_str['win_step']
    # print(step)
    # print(creator)
    # print(ready)
    # print(current_turn)
    # print(current_stone)
    # print(left_time)
    # print(board)
    # print(last_step)
    # print(win_step)


def playgame():
    global he_score
    global my_score
    global other_score
    he_score = 0
    my_score = 0
    other_score = 0
    password_key = DH(password)

    visit_url_finally = visit_url + '?user=' + user + '&password=' + password_key + '&data_type=json'
    visit_response = requests.get(visit_url_finally)
    game_id = json.loads(visit_response.text)['game_id']
    visit_url_finally = visit_url + '?user=' + user + '&password=' + password_key
    visit_response = requests.get(visit_url_finally)
    print(visit_response.url)

    check_url_finally = check_url + str(game_id)
    print(check_url_finally)
    check_response = requests.get(check_url_finally)
    print(check_response.text)
    # with open('a.html','w') as f:
    #     print(check_response.text, file=f)
    check_json = json.loads(check_response.text)
    init_json(check_json)
    while winner == 'None':
        if is_success == 'false':
            return
        print(user+'   ' +current_turn)
        if current_turn == user:
            for i in range(15):
                for j in range(15):
                    score_list[i][j] = 0
            if board_str == '':
                print('http://202.207.12.223:8000/play_game/' + str(game_id) + '/?user=' + user + '&password=' + password_key + '&coord=hh')
                play_responce = requests.get('http://202.207.12.223:8000/play_game/' + str(game_id) + '?user=' + user + '&password=' + password_key + '&coord=hh')
                print(play_responce.text)
            elif len(board_str) == 2:
                nextQP = ''
                if board_str != 'hh':
                    nextQP = 'hh'
                else:
                    nextQP += board_str[0]
                    nextQP += chr(ord(board_str[1])+1)
                print(nextQP)
                print('http://202.207.12.223:8000/play_game/' + str(game_id) + '/?user=' + user + '&password=' + password_key + '&coord=' + nextQP)
                play_responce = requests.get('http://202.207.12.223:8000/play_game/' + str(game_id) + '?user=' + user + '&password=' + password_key + '&coord=' + nextQP)
                print(play_responce.text)
            else:
                nextQP = set_score(board_str)
                print(nextQP)
                print('http://202.207.12.223:8000/play_game/' + str(game_id) + '/?user=' + user + '&password=' + password_key + '&coord=' + nextQP)
                play_responce = requests.get('http://202.207.12.223:8000/play_game/' + str(game_id) + '?user=' + user + '&password=' + password_key + '&coord=' + nextQP)
                print(play_responce.text)

        check_json = json.loads(requests.get(check_url + str(game_id)).text)
        print(board_str)
        if winner == 'None':
            init_json(check_json)
            if is_success == 'false':
                return
        else:
            print(winner)
            return

        time.sleep(5)


def MaxMinState():
    global iskome
    global other_score
    global my_score
    global he_score
    my_score = 0
    he_score = 0
    other_score = 0
    temp_board = board_str
    s = set_score(temp_board)
    my_score = other_score
    if iskome == 1:
        iskome = 0
        return set_score(board_str)
    else:
        temp_board += s
        set_score(temp_board)
        he_score = other_score
        if my_score > he_score:
            return set_score(board_str)
        else:
            temp_board = temp_board + set_score(temp_board)
            return set_score(temp_board)


if __name__=="__main__":
    while 1:
        playgame()