def dao_nguoc_list(lst):
    return lst[::-1]
input_list = input("Nhap day so cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))
lst_dao_nguoc = dao_nguoc_list(numbers)
print("Day so sau khi dao nguoc la:", lst_dao_nguoc)