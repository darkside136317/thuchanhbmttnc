def tinh_tong_chan(lst):
    tong=0
    for i in lst:
        if i%2==0:
            tong+=i
    return tong
input_list = input("Nhap day so cach nhau boi dau phay: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_chan(numbers)
print("Tong cac so chan trong day la:", tong_chan)