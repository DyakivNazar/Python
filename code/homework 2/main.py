from itertools import count
from typing import Callable, List, Tuple


# 1) написати функцію (notebook) на замикання,
# котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
#
# – перший записує в список нову справу
#
# – другий повертає всі записи
#

def notebook():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        nonlocal todo_list
        return todo_list

    return add_todo, get_all


# add, get = notebook()
# add('todo 1')
# print(get())
# add('todo2')
# print(get())


# 2) протипізувати перше завдання

def notebook1() -> Tuple[Callable[[str], None], Callable[[], list[str]]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        todo_list.append(todo)

    def get_all() -> List[str]:
        return todo_list

    return add_todo, get_all


# 3) створити функцію, котра буде повертати суму розрядів числа у вигляді строки (також використовуємо типізацію)

def expanded_form(num: int) -> str:
    parts = []
    num_str = str(num)
    length = len(num_str)
    for i, ch in enumerate(num_str):
        if ch != '0':
            zero = length - i - 1
            parts.append(ch + '0' * zero)
    return ' + '.join(parts)


# print(expanded_form(120324))


# 4) створити декоратор, котрий буде підраховувати, скільки разів була запущена функція,
# продекорована цим декоратором, та буде виводити це значення після виконання функцій

def decor(fun):
    count = 0

    def inner(*args):
        nonlocal count
        count += 1
        print(f'Count: {count}')
        fun(*args)
        print('----------------------------')

    return inner

@decor
def fun1():
    print('fun1')
@decor
def fun2():
    print('fun2')

fun1()
fun1()
fun2()
fun1()
