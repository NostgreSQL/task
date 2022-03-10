a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))
op = input("Введи операцию (делить или умножить): ")
error1 = "Ошибка: делить на ноль нельзя!"
if op == "/":
if b == 0:
print(error1)
else:
print(a/b)
else:
print(a*b)
