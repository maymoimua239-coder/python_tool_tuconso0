import logging

def process_data(price_list):
    for price in price_list:
        logging.debug(f"dang su ly du lieu: {price}")
        assert price > 0, "Loi du lieu, phat hien gia tri am!"
        print(f"---> Da luu gia {price} vao co so du lieu.\n")

danh_sach = [100, 200, -50, 100]
process_data(danh_sach)
