# Bài tính giai thừa
def tinh_giai_thua(n):
    giai_thua = 1
    for i in range(1, n+1): #vòng lặp i với phạm vi từ 1 đến n+1
        giai_thua = giai_thua*i
        #giá trị của biến i lần lượt được gán bằng 1, 2, 3, ..., n. Trong mỗi lần lặp,
        # giá trị của biến giai_thua sẽ được nhân với giá trị của biến i,
        # và kết quả sẽ được gán lại cho biến giai_thua.

    return giai_thua
print(tinh_giai_thua(7))
