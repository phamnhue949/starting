# Bubble Sort
# Sắp xếp đơn giản nhất tìm giá trị nhỏ nhất rồi đôn lên đầu

# arr = [3,2,5,4]
# n = len(arr) # 3
# x = []
# for i in range(n):
#     vitri = i 
#     for j in range(i+1, n): # loop thêm một lần nữa mảng [i+1, n]
#         if arr[j] < arr[vitri]:
#             vitri = j
#     x.append(arr[vitri])      
#     arr[vitri], arr[i] = arr[i], arr[vitri]
#     print(arr)

# print(x)


d = {}

x = '11012'
for i in x:
    if i not in d:
        d[i] = 1
    else:
        d[i] +=1
        
print(d)