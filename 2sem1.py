# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
# #     Примеры:
    
# #     - 1, 4, 8, 7, 5 -> 8
# #     - 78, 55, 36, 90, 2 -> 90

# num1 = int (input) ('Введите 1 число: ')
# num2 = int (input) ('Введите 2 число: ')
# num3 = int (input) ('Введите 3 число: ')
# num4 = int (input) ('Введите 4 число: ')
# num5 = int (input) ('Введите 5 число: ')

# if num1 > num2 and num1 >num3 and num1 >  

# numbers = []
# for i in range(5):
#     numbers.append(int(input(f'Введите элемент под номером {i}: ')))
# print(numbers)
# print(max(numbers))

# my_max = num1
# if my_max<num2:
#    my_max = num2
# if my_max<num3:
#    my_max = num3
# if my_max<num4:
#    my_max = num4
# if my_max<num5:
#    my_max = num5
# print(my_max)

# numbers = [1, 4, 6, 2, 3]
# # for i in range(1,6):
# #     numbers.append(int(input(f'Введите элемент под номером {i}: ')))
# print(numbers)
# print(max(numbers))

my_max = 0
for _ in range(5):
    num = int(input('Введите число: '))
    if my_max < num:
        my_max = num

print(my_max)

# range(5) -> range(start=0, stop=5, step=1):
# range(1,5) -> range(start=1, stop=5, step=1)
# range(1,9,2)range(start=1, stop=9, step=2)
# range(9,1,-1)range(start=9, stop=1, step=-1)

