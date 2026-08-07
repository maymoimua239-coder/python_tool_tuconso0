danh_sach_sp = [
    {"ten": "Laptop Dell", "gia": 15000},
    {"ten": "Chuột Logitech", "gia": 500}
]

# 1. Code sửa giá Chuột Logitech tại đây
danh_sach_sp[1]["gia"] = 1200

# 2. Code thêm sản phẩm Bàn phím cơ tại đây
danh_sach_sp.append({"ten": "Ban phim co", "gia": 2000})

# 3. Kiểm tra kết quả
print(danh_sach_sp)
