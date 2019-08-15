import requests
import json
import numpy

# http://202.207.12.223:8000/context/c03152f5db8918b9905d449686685f77

url = 'http://202.207.12.223:8000/step_07'
response = requests.get(url)
print(response.text)

json_str = json.loads(response.text)
board = json_str['board']
coord = json_str['coord']

board_list = numpy.zeros((15, 15))
step_num = len(board)


def ChangeBoard(x, y, player):
    board_list[x][y] = player



for i in range(0, step_num, 2):
    if (i // 2) % 2 == 0:
        ChangeBoard(ord(board[i]) - ord('a'), ord(board[i+1]) - ord('a'), ord('x'))
    else:
        ChangeBoard(ord(board[i]) - ord('a'), ord(board[i+1]) - ord('a'), ord('o'))

total_chess_shape = ''


def check_chess_type(x, y):
    global total_chess_shape
    one_chess_shape = ''
    for i in range(-4, 5):
        if y + i < 0 or y + i >= 15:
            continue
        if board_list[x][y+i] == 0:
            one_chess_shape += '.'
        if board_list[x][y+i] == ord('o'):
            one_chess_shape += 'o'
        if board_list[x][y+i] == ord('x'):
            one_chess_shape += 'x'
    one_chess_shape += ','
    for i in range(-4, 5):
        if y + i < 0 or y + i >= 15 or x + i < 0 or x + i >= 15:
            continue
        if board_list[x+i][y+i] == 0:
            one_chess_shape += '.'
        if board_list[x+i][y+i] == ord('o'):
            one_chess_shape += 'o'
        if board_list[x+i][y+i] == ord('x'):
            one_chess_shape += 'x'
    one_chess_shape += ','
    for i in range(-4, 5):
        if x + i < 0 or x + i >= 15:
            continue
        if board_list[x+i][y] == 0:
            one_chess_shape += '.'
        if board_list[x+i][y] == ord('o'):
            one_chess_shape += 'o'
        if board_list[x+i][y] == ord('x'):
            one_chess_shape += 'x'
    one_chess_shape += ','
    for i in range(-4, 5):
        if (y - i < 0 or y - i >= 15) or (x + i < 0 or x + i >= 15):
            continue
        if board_list[x+i][y-i] == 0:
            one_chess_shape += '.'
        if board_list[x+i][y-i] == ord('o'):
            one_chess_shape += 'o'
        if board_list[x+i][y-i] == ord('x'):
            one_chess_shape += 'x'
    one_chess_shape += ','
    total_chess_shape += one_chess_shape
    print(total_chess_shape)


for i in coord:
    check_chess_type(ord(i[0]) - ord('a'), ord(i[1]) - ord('a'))


finally_url = url + '?ans=' + total_chess_shape[:-1]
finally_response = requests.get(finally_url)
print(finally_url)
print(finally_response.text)