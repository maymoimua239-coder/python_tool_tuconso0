import logging
logging.basicConfig(level=logging.DEBUG)
def chia_tai_cong_viec(tong_so_link, so_may_chu):
    
    assert tong_so_linh > 0, "Loi: Khong co du lieu de cao!"

    try:
        linh_moi_ngay = tong_so_link/so_may_chu
        logging.debug(f"Hệ thống đã chia tải: {link_moi_may} link/máy chủ.")
        return link_moi_may

    except ZeroDivisionError:
        print("Cảnh báo: Số lượng máy chủ bằng 0. Tool đang chờ cấp phát máy...")
        return None

print("Kịch bản 1: Hoạt động bình thường (1000 link, 5 máy)")
chia_tai_cong_viec(1000, 5)

print("\nKịch bản 2: Máy chủ sập hết về 0 (1000 link, 0 máy)")
chia_tai_cong_viec(1000, 0)

print("\nKịch bản 3: Không có link nào (0 link, 5 máy) - Bỏ comment dòng dưới để thấy assert hoạt động")
chia_tai_cong_viec(0, 5)


