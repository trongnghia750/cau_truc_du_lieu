# BT04 Bài toán mã đi tuần

n = 8


# isSafe - Nó kiểm tra xem nước đi có nằm trong bàn cờ hay không?
def isSafe(x, y, board):
    # x, y là toạ độ của quân Mã trong bàn cờ ma trận n x n (ở đây xét bàn cờ 8 x 8)
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False


# hàm tính nước đi của quân Mã
def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos):
    if (pos == n ** 2):  # điều kiện này chắc chắc FALSE cho đến khi quân Mã di chuyển hết bàn cờ, cũng là lúc pos = 64
        return True  # FALSE thì thực hiện vòng lặp phía dưới

    for i in range(8):
        new_x = curr_x + move_x[i]  # toạ độ mới = toạ độ hiện tại + cách di chuyển
        new_y = curr_y + move_y[i]  # toạ độ mới này sẽ được thay xuống hàm isSafe phía dưới,
        # để kiểm tra xem có hợp lệ, tức có nằm trong bàn cờ hay không?

        if (isSafe(new_x, new_y, board)):  # nếu toạ độ mới này thoả mãn điều kiện hàm isSafe phía trên,
            # tức là nằm trong bàn cờ, thì thực thi lệnh sau

            board[new_x][new_y] = pos  # đánh dấu vị trí đã đến (new) = giá trị của pos
            # pos này được hiểu là thứ tự nước đi, nên nó sẽ +1 sau mỗi lần lặp

            # sử dụng toạ độ mới phía trên để tiếp tục thay vào hàm solveKTUtil
            # điều kiện này cũng chắc chắn là FALSE để tiếp tục vòng lặp cho đến khi pos+1=64
            if (solveKTUtil(board, new_x, new_y, move_x, move_y, pos + 1)):
                return True
            board[new_x][new_y] = -1
    return False


# hàm xuất ra màn hình hành trình ( hay thứ tự nước đi ) của quân Mã
def printSolution(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT():  # hàm này là hàm main

    # tạo bàn cờ ma trận tỉ lệ n x n, với các phần tử ma trận đều mang giá trị là -1
    board = [[-1 for i in range(n)] for i in range(n)]

    board[4][0] = 0  # vị trí xuất phát của quân Mã
    # ở đây chúng ta đang thử đặt Mã ở vị trí (4,0) trong ma trận,
    # với gốc toạ độ là góc phía trên, bên trái
    # gán cho nó = 0 vì đây là vị trí xuất phát)

    pos = 1  # chỉ số của nước đi ĐẦU TIÊN
    # nếu thử thay pos = 2 thì Mã sẽ không đi hết được bàn cờ,
    # vị trí chưa đi tới có giá trị = -1 trong bàn cờ)

    move_x = [2, 1, -1, -2, -2, -1, 1, 2]  # toạ độ di chuyển (cách di chuyển) của quân Mã
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    if (not solveKTUtil(board, 4, 0, move_x, move_y, pos)):
        print("Giải pháp không tồn tại")
    else:
        printSolution(board)


if __name__ == "__main__":
    solveKT()
