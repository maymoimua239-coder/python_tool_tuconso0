def extract_price(text):
    try:
        price = int(text)
        return price
    
    except ValueError:
        print("Loi: Khong the hien thi gia nay")
        return None

n = input('>')
print(extract_price(n))


