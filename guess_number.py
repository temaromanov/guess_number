from random import randint


m = randint(1, 5)
print("Угадай число")
while True:
    num = int(input("input your nunber: "))
    if m < num:
        print("введите число меньше")
    elif m > num:
        print("введите число ,больше")
    else:
        break
print('Отлично')
