print("nhap cac dong van ban( nhap 'done' de ket thuc): ")
lines = []
while True:
    line = input()
    if line == 'done':
        break
    lines.append(line)
print("\n cac dong da nhap sau khi chuyen thanh chu in hoa:  ")
for line in lines:
    print(line.upper())