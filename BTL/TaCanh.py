import os
import random
import copy
import math
import time


def goal(size):
    tacanh = []
    for i in range(size ** 2):
        tacanh.append(i + 1)
    return tacanh


def randomize(size):
    tacanh = goal(size)
    random.shuffle(tacanh)
    show(tacanh)
    return tacanh


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


def up(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index >= n:
        temp_tacanh[index - n], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index - n]
    return temp_tacanh


def down(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index < n * (n - 1):
        temp_tacanh[index + n], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index + n]
    return temp_tacanh


def left(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index % n != 0:
        temp_tacanh[index - 1], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index - 1]
    return temp_tacanh


def right(a):
    temp_tacanh = copy.copy(a)
    n = int(math.sqrt(len(a)))
    index = temp_tacanh.index(n ** 2)
    if index % n != n - 1:
        temp_tacanh[index + 1], temp_tacanh[index] = temp_tacanh[index], temp_tacanh[index + 1]
    return temp_tacanh


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
