# Bài USCLN
def USCLN(a, b):
    if b == 0:
        return a  # nếu b = 0 thì USCLN là a
    else:
        # tiếp tục đệ quy và tìm USCLN của b và a % b (phần dư của a khi chia cho b).
        # Với mỗi lần đệ quy, a sẽ được thay bằng b và b sẽ được thay bằng a % b,
        # cho đến khi b bằng 0. Khi đó, USCLN(a, 0) = a, và a chính là kết quả của bài toán ban đầu.
        return USCLN(b, a % b)


print(USCLN(5, 10))
