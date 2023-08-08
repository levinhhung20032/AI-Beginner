import os
import random
import copy
import math
import time


# Hàm trả về trạng thái đích theo kích thước truyền vào
def goal(size):
    tacanh = []
    for i in range(size ** 2):
        tacanh.append(i + 1)
    return tacanh


# Hàm trả về một trạng thái ngẫu nhiên theo kích thước truyền vào (có thể trả về trường hợp không thể giải được)
def randomize(size):
    tacanh = goal(size)
    random.shuffle(tacanh)
    show(tacanh)
    return tacanh


# Hàm giúp người dùng tự tạo trạng thái mong muốn với kích thước truyền vào
def customize(size):
    x = None
    count = 0
    temp = []
    for i in range(size ** 2):
        temp.append(i + 1)
    show(temp)
    while x != 0:
        x = int(input())
        if x == 5:
            temp = up(temp)
            show(temp)
        elif x == 3:
            temp = right(temp)
            show(temp)
        elif x == 2:
            temp = down(temp)
            show(temp)
        elif x == 1:
            temp = left(temp)
            show(temp)
        if x != 0:
            count += 1
    print(count, "steps:", temp)
    print(temp)
    return temp


# Hàm trả về một trạng thái được tráo ngẫu nhiên từ trạng thái truyền vào với số lần tráo mong muốn
def shuffle(tacanh, steps):
    temp = copy.copy(tacanh)
    count = 0
    diary = [temp]
    n = int(math.sqrt(len(temp)))
    while count < steps:
        blank = temp.index(len(temp))
        direction = random.randint(0, 3)
        if blank < n * (n - 1) and direction == 0 and down(temp) not in diary:
            temp = down(temp)
            diary.append(temp)
            count += 1
        if blank >= n and direction == 1 and up(temp) not in diary:
            temp = up(temp)
            diary.append(temp)
            count += 1
        if blank % n != 0 and direction == 2 and left(temp) not in diary:
            temp = left(temp)
            diary.append(temp)
            count += 1
        if blank % n != n - 1 and direction == 3 and right(temp) not in diary:
            temp = right(temp)
            diary.append(temp)
            count += 1
    return temp


# Hàm trả về trạng thái nếu ô trống di chuyển lên trên so với trạng thái truyền vào
def up(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index >= n:
        temp_tacanh[index - n], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index - n]
    return temp_tacanh


# Hàm trả về trạng thái nếu ô trống di chuyển xuống dưới so với trạng thái truyền vào
def down(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index < n * (n - 1):
        temp_tacanh[index + n], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index + n]
    return temp_tacanh


# Hàm trả về trạng thái nếu ô trống di chuyển sang trái so với trạng thái truyền vào
def left(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index % n != 0:
        temp_tacanh[index - 1], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index - 1]
    return temp_tacanh


# Hàm trả về trạng thái nếu ô trống di chuyển sang phải so với trạng thái truyền vào
def right(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index % n != n - 1:
        temp_tacanh[index + 1], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index + 1]
    return temp_tacanh


# Hàm trả về danh sách các trạng thái có thể được sinh ra từ trạng thái truyền vào
def possible_moves(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    blank = temp_tacanh.index(len(a))
    possible_list = []
    if blank < n * (n - 1):
        possible_list.append((down(temp_tacanh), "down"))
    if blank >= n:
        possible_list.append((up(temp_tacanh), "up"))
    if blank % n != 0:
        possible_list.append((left(temp_tacanh), "left"))
    if blank % n != n - 1:
        possible_list.append((right(temp_tacanh), "right"))
    return possible_list


# Hàm thể hiện trạng thái dưới dạng bài toán Ta Canh
def show(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    print("-", end="")
    for x in range(n):
        print("-" * (len(str(n ** 2)) + 2), end="-")
    print()
    for y in range(n):
        print("|", end="")
        for x in range(n):
            if temp_tacanh[y * n + x] == n ** 2:
                print(" " * (len(str(n ** 2)) + 2), end="|")
            else:
                print(" " * (len(str(n ** 2)) + 1 - len(str(temp_tacanh[y * n + x]))), end="")
                print("%d " % temp_tacanh[y * n + x], end="|")
        print()
        print("-", end="")
        for x in range(n):
            print("-" * (len(str(n ** 2)) + 2), end="-")
        print()
