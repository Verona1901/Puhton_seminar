# print('hello world')
# value = None
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))

# value = 123456
# print(type(value))
# s = 'cdjhfishfis'
# print(type(s))
# print(a, b, s)
# print(a, '-', b, '-', s)
# print('{} - {} - {}' .format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{0} - {2} - {1}' .format(a, b, s))

# f = True
# print(f)

# list = [1, 2, 3]
# print(list)

# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, ' + ', b, ' = ', a + b)

# print('Введите а')
# a = int (input())
# print('Введите b')
# b = int (input())
# print(a, ' + ', b, ' = ', a + b)

# print('Введите а')
# a = float (input())
# print('Введите b')
# b = float (input())
# print(a, ' + ', b, ' = ', a + b)

# a = 123
# b = 8
# c = a**b
# print (c)


# a = 1.312354
# b = 3
# c = round(a*b, 5)
# print(c)

# a = 5
# a = a+5
# a += 5
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a= 1<3<5<10
# print (a)

# func = 1
# T = 4
# x = 123
# print(func < T > x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1, 2, 3, 4]
# # print(f)
# # print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# original = 152
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print (original)
# else:
#     print ('Пожалуй')
#     print ('хватит')
# print(inverted)


# for i in 1,2,3,4,5:
#     print (i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print (i)


# for i in range(10):
#     print(i)

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)  # red green blue
# for e in colors:
#     print(e*2)  # redred greengreen blueblue
# colors.append('gray')  # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])  # True
# colors.remove('red')  # del colors[0] # удалить элемент


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg =2.3
print (f (arg))
print (type (f(arg)))