def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print("Di chuyển Đĩa 1 từ cột nguồn", source, "đến cột nhận", destination) # chạy từ nguồn đến cột nhận đến hỗ trợ
        return

    TowerOfHanoi(n - 1, source, auxiliary, destination) # giảm 1 đĩa
                                                        # chạy từ nguồn đến hỗ trợ đến cột nhận

    print("Di chuyển Đĩa", n, "từ cột nguồn", source, "đến cột nhận", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source) # giảm 1 đĩa
                                                        # chạy từ hỗ trợ đến cột nhận đến nguồn

n = 4
TowerOfHanoi(n, 'A', 'B', 'C')
