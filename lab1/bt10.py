def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_chuoi = input("Nhap chuoi can dao nguoc: ")
print("Chuoi sau khi dao nguoc la: ", dao_nguoc_chuoi(input_chuoi))
