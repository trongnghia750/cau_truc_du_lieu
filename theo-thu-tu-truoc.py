class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def duyet_cay_thu_tu_truoc(root):
    if root:
        print(root.data, end=" ")  # xử lý nút gốc
        duyet_cay_thu_tu_truoc(root.left_child)  # xử lý cây con trái
        duyet_cay_thu_tu_truoc(root.right_child)  # xử lý cây con phải

# Tạo cây nhị phân
root = Node(3)
root.left_child = Node(4)
root.left_child.left_child = Node(8)
root.left_child.right_child = Node(6)
root.right_child = Node(9)
root.right_child.left_child = Node(2)
root.right_child.right_child = Node(7)


# Duyệt cây theo thứ tự trước và in ra các giá trị
print("Duyệt cây theo thứ tự trước:\n")
duyet_cay_thu_tu_truoc(root)
