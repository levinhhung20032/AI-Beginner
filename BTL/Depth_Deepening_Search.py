from BTL import TaCanh
import copy
import math
from timeit import default_timer


# Hàm tái định hướng
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


# Hàm kiểm tra tính lặp của trạng thái, trả về danh sách trạng thái đã bỏ lặp
def check(possible_list, diary, option):
    if option == 1:
        # Option 1: remove existed scenario
        back_list = []
        for i in possible_list:
            if i[0] not in diary:
                back_list.append(i)
        return back_list
    elif option == 2:
        # Option 2: normal
        return possible_list


# Hàm đính kèm độ sâu của trạng thái
def depth(possible_list, depth):
    temp = []
    for i in possible_list:
        temp.append((i[0], i[1], depth))
    return temp


# Chiến lược tìm kiếm sâu lặp
def Depth_Deepening_Search(a, mode):
    temp = copy.copy(a)
    temp.sort()
    goal_tacanh = temp
    start = default_timer()
    status = []
    path = []
    moves = [(a, "begin", 1)]
    diary = [a]
    count = 0
    MaxDepth = 15
    TempDepth = 5

    while True:
        # Nếu thời gian xử lý vượt quá 30s hoặc đã vét cạn, chương trình sẽ coi trạng thái không thể giải
        if (default_timer() - start) * 1000 > 30000:
            return "Unsolvable!", (default_timer() - start) * 1000, count
        else:
            if not moves:
                # Nếu độ sâu đang xét lớn hơn độ sâu tối đa, chương trình sẽ coi trạng thái không thể giải
                if TempDepth > MaxDepth:
                    return "Unsolvable!", (default_timer() - start) * 1000, count
                else:  # Reset các nhật ký lưu trũ cũ để tìm kiếm với độ sâu mới
                    status = []
                    diary = [a]
                    moves = [(a, "begin", 1)]
                    TempDepth += 1
            else:
                prev_moves = copy.copy(moves)
                status += prev_moves  # Nhật kí trạng thái ghi lại những trạng thái đã được xét
                moves = []
                for i in prev_moves:
                    if i[2] > TempDepth:
                        continue
                    else:
                        count += 1
                        diary.append(i[0])
                        if i[0] == goal_tacanh:
                            path.append(i)  # Nếu tìm thấy trạng thái đích, thêm trạng thái đích vào đường dẫn
                            break
                        else:
                            # Nếu chưa tìm thấy trạng thái đích, tiếp tục thêm những trạng thái con vào hàng đợi
                            possible_moves = TaCanh.possible_moves(i[0])
                            possible_moves = depth(possible_moves, i[2] + 1)
                            moves = check(possible_moves, diary, mode) + moves
                else:
                    continue
                break

    # Đảo ngược nhật ký để tìm đường dẫn
    status.reverse()

    temp = goal_tacanh
    for i in status:  # Truy ngược từ trạng thái đích về trạng thái ban đầu dựa vào nhật kí trạng thái
        if i[0] == temp:
            temp = redirect(i)
            path.append(i)
        elif temp is None:
            break

    # Đảo ngược đường dẫn (Do đường dẫn đang chỉ từ trạng thái đích về trạng thái ban đầu)
    path.reverse()
    # Bỏ trạng thái ban đầu khỏi đường dẫn
    path.pop()
    return path, (default_timer() - start) * 1000, count


# Hàm in ra kết quả thuật toán
def output(option, mode):
    if option[0] == 1:
        # Option 1: Wanted scenario input
        path, time, count = Depth_Deepening_Search(option[1], mode)
    elif option[0] == 2:
        # Option 2: Random scenario
        path, time, count = Depth_Deepening_Search(TaCanh.randomize(option[1]), mode)
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
