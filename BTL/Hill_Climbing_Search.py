from BTL import TaCanh
import copy
import math
from timeit import default_timer
import heapq


# Priority Queue, sử dụng để trả về phần tử có độ ưu tiên cao nhất mà không cần sắp xếp toàn bộ mảng
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, ((priority, -default_timer()), item))

    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty.")
        return heapq.heappop(self.heap)[1]

    def peek(self):
        if self.is_empty():
            raise IndexError("Priority Queue is empty.")
        return self.heap[0][1]

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)


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


# Hàm đánh giá
def grading(tacanh):
    grade = 0
    n = int(math.sqrt(len(tacanh[0])))
    for i in range(n ** 2):
        if tacanh[0][i] != i + 1 and tacanh[0][i] != n ** 2:
            temp = abs(tacanh[0][i] - i - 1)
            grade += (temp // n + temp % n)
    return grade


# Chiến lược tìm kiếm leo đồi
def Hill_Climbing_Search(a, mode):
    temp = copy.copy(a)
    temp.sort()
    goal_tacanh = temp
    start = default_timer()
    status = []
    path = []
    moves = PriorityQueue()
    moves.push((a, "begin"), grading((a, "begin")))
    diary = [a]
    count = 0

    while True:
        # Nếu thời gian xử lý vượt quá 30s hoặc đã vét cạn, chương trình sẽ coi trạng thái không thể giải
        if (default_timer() - start) * 1000 > 30000 or moves.is_empty():
            return "Unsolvable!", (default_timer() - start) * 1000, count
        else:
            count += 1
            item = moves.pop()  # Xét trạng thái có mức ưu tiên cao nhất (hàm đánh giá trả về kết quả nhỏ nhất)
            status.append(item)
            diary.append(item[0])
            if item[0] != goal_tacanh:
                # Nếu chưa tìm thấy trạng thái đích, tiếp tục thêm những trạng thái con vào hàng đợi
                temp = TaCanh.possible_moves(item[0])
                temp = check(temp, diary, mode)
                for i in temp:  # Đưa tất cả trạng thái con vào hàng đợi ưu tiên
                    moves.push(i, grading(i))
            else:
                path.append(item)  # Nếu tìm thấy trạng thái đích, thêm trạng thái đích vào đường dẫn
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
        path, time, count = Hill_Climbing_Search(option[1], mode)
    elif option[0] == 2:
        # Option 2: Random scenario
        path, time, count = Hill_Climbing_Search(TaCanh.randomize(option[1]), mode)
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
