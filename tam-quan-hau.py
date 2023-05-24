
SL = int(input("Nhập số lượng quân Hậu: "))

# tạo bàn cờ Vua ma trận size (SLxSL) với tất cả phần tử có giá trị = 0
board = [[0] * SL for m in range(SL)]

def attack(i, j):
    # kiểm tra hàng ngang và hàng dọc
    for k in range(0, SL):
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # True ở đây nghĩa là có quân Hậu khác nằm trên đường đi (ngang và dọc) của ta

    # kiểm tra đường chéo
    for k in range(0, SL):
        for g in range(0, SL):
            if (k + g == i + j) or (k - g == i - j):
                if board[k][g] == 1:
                    return True
    # True ở đây có nghĩa là có quân Hậu khác nằm trên đường đi (đường chéo) của ta

    return False


# False ở đây nghĩa là không có quân Hậu nào nằm trên đường đi,
# vị trí (i,j) đã hợp lệ

def N_queens(n):  # n = SL = số lượng quân hậu cần sắp xếp
    if n == 0:
        return True  # nếu nhập n khác 0 thì điều kiện này False và sẽ chạy vòng lặp bên dưới,
        # n sẽ giảm dần về 0 theo vòng lặp

    for i in range(0, SL):
        for j in range(0, SL):

            if (not (attack(i, j))) and (board[i][j] != 1):
                # not(attack(i,j)) = attack(i,j) return False, tức là vị trí (i,j) hợp lệ
                # board[i][j] khác 1, để kiểm tra xem vị trí (i,j) có bị trùng với các vị trí trước đó không
                # nếu 2 điều kiện trên đều đúng, thì đánh dấu vị trí (i,j) = 1
                board[i][j] = 1

                if N_queens(n - 1) == True:  # Sau khi đã đánh dấu thì gọi lại hàm để kiểm tra lại n
                    return True  # giá trị của n = giá trị của SL, đều là số lượng quân Hậu
                    # vấn đề sẽ xảy ra nếu như n đã giảm dần về 0 mà i,j vẫn chưa chạy hết SL

                board[i][j] = 0  # test 2 câu lệnh này bằng cách xoá đi, chạy code cho SL = 2 hoặc 3
    return False  # từ đó rút ra: nếu ko có 2 câu lệnh này
    # thì SL quân hậu nhập vào sẽ khác số lượng quân hậu xuất hiện trên màn hình
    # tức là ví dụ nhập vào 3 quân hậu cần sắp xếp,
    # nhưng kết quả chỉ xuất hiện 2 (không đạt yêu cầu bài toán)


N_queens(SL)
for b in board:  # in kết quả ra màn hình
    print(b)
