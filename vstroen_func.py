# #problems1
# values = ("turusbekova 109/1", 10, 1005, ["tables", "chairs"], 23.00)
# set_val = []
# for i in values:
#     if not type(i) in (set,list,tuple):
#         set_val.append(True)
#     else:
#         set_val.append(False)
# print(all(set_val))

# #problems2
# a = set()
# for i in range(5):
#     nums = int(input('Введите число: '))
#     a.add(nums)
# print(min(a))

# #problems3
# def func():
#     return('Beks')

# try:
#     py_func = input('Введите функцию: ')
#     print(eval(py_func))
# except Exception:
#     print('В Python нету такой функции')

# #problems4
# procent = 3.47
# zaim = int(input('Введите займ(минимум 50000): '))
# if zaim < 50000:
#     print("Введите неменьше от 50000")
# else:
#     summa = zaim * (procent/100)
#     print(round(summa,2))