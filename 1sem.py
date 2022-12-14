# Задачи:

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
    
#     *Примеры:* 
    
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет
# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
    
#     Примеры:
    
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

num1 =int (input("Ввесдите первое число: "))
num2 =int (input("Введите второе число: "))
print (f'{num1}, {num2} -> ', end= '')

if num1 == num1 **2 or num2 == num1 ** 2:
    print("да")
else:
    print ("нет")


#     first_user_number = int(input(' Enter first number: '))
# second_user_number = int(input(' Enter second number: '))
# print (f'{first_user_number}, {second_user_number} ->', end=' ')

# if first_user_number == second_user_number ** 2 or second_user_number == first_user_number ** 2:
#     print ('yes')
# else:
#     print ('no')
