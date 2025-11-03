#strings
# 1) написати прогу, яка вибирає зі введеної строки цифри і виводить їх через кому

st='as 23 fdfdg544'

res = [ch for ch in st if ch.isdigit()]
# print(', '.join(res))

# 2)написати прогу, яка вибирає зі введеної строки числа і виводить їх так, як вони написані

st1='as 23 fdfdg544 34'
res1 = (''.join(ch if ch.isdigit() else ' ' for ch in st1 ).split())
# print(', '.join(res1))



# list comprehension
# 1) є строка:

greeting = 'Hello, world'

# записати кожний символ, як окремий елемент списку, і зробити його заглавним

res2=[ch.upper() for ch in greeting]
# print(res2)

# 2) з діапазону від 0-50 записати тільки непарні числа, при цьому піднести їх до квадрату
l = [i for i in range(50)]
res3=[j**2 for j in l if j%2]
# print(res3)



# function
#
# - створити функцію яка виводить List
def show_list(l):
    print(l)
# show_list('List')

# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def show_max(a,b,c):
    print(max(a, b, c))
    return max(a, b, c)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def ret_min_show_max(*args):
    print(max(args))
    return min(args)

# - створити функцію яка повертає найбільше число з List
def ret_max(l):
    return max(l)

# - створити функцію яка повертає найменьше число з List
def ret_min(l):
    return min(l)

# - створити функцію яка приймає List чисел та складає значення елементів List та повертає його.
def sum_list(l):
    return sum(l)

# - створити функцію яка приймає List чисел та повертає середнє арифметичне його значень.
def avg_list(l):
    return sum(l)/len(l)



# 1)Дан list:
lst = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
# print(min(lst))
#   - видалити усі дублікати
def delet_dub(l):
    print(list(dict.fromkeys(l)))
#   - замінити кожне 4-те значення на 'X'
def cheng_4_value_X(l):
    for i in range(3, len(l), 4):
        l[i] = 'X'
    return l
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
def square(n):
    for i in range(n):
        if i==0 or i==n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')


# 3) вывести табличку множення за допомогою цикла while
def multi_table():
    i = 1
    while i <= 10:
        j=1
        while j <= 10:
            print(f"{i * j:4}", end="")
            j+=1
        print()
        i+=1

# 4) переробити це завдання під меню
while True:
    print('1) знайти мін число')
    print('2) видалити усі дублікати')
    print('3) замінити кожне 4-те значення на "X"')
    print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5) вывести табличку множення за допомогою цикла while')
    print('9) вихід')

    choice = input('Зробіть свій вибір: ')

    if choice == '1':
        print(ret_min(lst))
    elif choice == '2':
        delet_dub(lst)
    elif choice == '3':
        print(cheng_4_value_X(lst))
    elif choice == '4':
        square(7)
    elif choice == '5':
        multi_table()
    elif choice == '9':
        break