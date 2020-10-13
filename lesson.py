def input_data(n):
    arr=[]
    for i in range(n):
        x = int(input(f"Input item[{i}]: "))
        arr.append(x)
    return arr
# def input_list(n):
#     arr = []
#     i = 0
#     while True:
#         x = input(f"Input item[{i}]: ")
#         try:
#             arr.append(int(x))
#             i += 1
#             if i >= n:
#                 break
#         except:
#             print("Chưa nhập đúng số nguyên. Nhập lại!")
#     return arr
# # =====================================================================
def tinhtong(arr):
    tong = 0
    for i in arr:
        tong +=i
    return tong
n = int(input("Nhập phần tử tinh tong:"))
arr = input_data(n)
print(arr)
# print(tinhtong(arr))
# # # --------------------------------------
def tinh_tich(n):
    n=input_list(n)
    tich=1
    for i in n:
        tich *= i
    return tich
n = int(input("Nhập phần tử tinh tich :"))
print(input_list(n))
# print(arr)
print(tinh_tich(n))

# # ----------------------------------------
def tim_max(arr):
    max = arr[i]
    for i in range(1,len(arr)):
        if max < arr[i]:
           max = arr[i]
    return max
n = int(input("Nhập phần tử tim max :"))
arr = input_data(n)
print(arr)
print(tim_max(arr))
# # ---------------------------------------
def tim_min(arr):
    min = arr[i]
    for i in range(1,len(arr)):
        if  min > arr[i]:
            min = arr[i]
    return min
n = int(input("Nhập phần tử :"))
arr = input_data(n)
print(arr)
print(tim_min(arr))
# # # =======================================
def so_le(arr):
    result = []
    for i in arr:
        if i%2!=0:
            result.append(i)
    return result
n = int(input("Nhập phần tử :"))
arr = input_data(n)
print(arr)
print(so_le(arr))
# # # ==========================================
def so_chan(arr):
    result = []
    for i in arr:
        if i%2==0:
            result.append(i)
    return result
n = int(input("Nhập phần tử :"))
arr = input_data(n)
print(arr)
print(so_chan(arr))
# # =================================
def kiem_tra_snt(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count == 2:
        return "La so nguyen to"
    return "Khong la so nguyen to"
def tinh_tong(n):
    sum=0
    for i in range(1,n+1):
        if nguyento(n):
            sum+=i
    print(sum)
n=int(input("Nhap so:"))
print(kiem_tra_snt(n))
print(tinh_tong(n))
