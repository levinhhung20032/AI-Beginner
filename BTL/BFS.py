from BTL import TaCanh
import copy
import math
from timeit import default_timer


def redirect(a):
    if a[1] == "up":
        return TaCanh.down(a[0])
    elif a[1] == "down":
        return TaCanh.up(a[0])
    elif a[1] == "left":
        return TaCanh.right(a[0])
    elif a[1] == "right":
        return TaCanh.left(a[0])
    elif a[1] == "begin":
        return None


def check(possible_list, diary, option):
    if option == 1:
        # Option 1: remove existed scenario
        back_list = []
        for i in possible_list:
            if i[0] not in diary:
                back_list.append(i)
        return back_list
    elif option == 2:
        # Option 2: normal BFS
        return possible_list


def BFS(a, mode):
    temp = copy.copy(a)
    temp.sort()
    goal_tacanh = temp
    start = default_timer()
    status = []
    path = []
    moves = [(a, "begin")]
    diary = [a]
    count = 0

    while True:
        if (default_timer() - start) * 1000 > 30000 or moves == []:
            return "Unsolvable!", (default_timer() - start) * 1000, count
        else:
            prev_moves = copy.copy(moves)
            status += prev_moves
            moves = []
            for i in prev_moves:
                count += 1
                diary.append(i[0])
                if i[0] == goal_tacanh:
                    path.append(i)
                    break
                else:
                    possible_moves = TaCanh.possible_moves(i[0])
                    moves += check(possible_moves, diary, mode)

            else:
                continue
            break

    status.reverse()

    temp = goal_tacanh
    for i in status:
        if i[0] == temp:
            temp = redirect(i)
            path.append(i)
        elif temp is None:
            break

    path.reverse()
    path.pop()
    return path, (default_timer() - start) * 1000, count


def output(option, mode):
    if option[0] == 1:
        # Option 1: Wanted scenario input
        path, time, count = BFS(option[1], mode)
    elif option[0] == 2:
        # Option 2: Random scenario
        path, time, count = BFS(TaCanh.randomize(option[1]), mode)
    if path == "Unsolvable!":
        print(path)
    else:
        for i in path:
            print(i[1])
            TaCanh.show(i[0])
        print("Size:", int(math.sqrt(len(option[1]))))
        print("Steps:", len(path) - 1)
    print("Time passed:", time, "ms")
    print("Total step processed:", count)
    print("finish")
