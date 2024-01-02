# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def isFirst(n):
    n = []
    for num in range(n):

        if num > 1:

            for i in range(2, num):

                if (num % i) == 0:
                    break

            else:
                print(num)
                n.add(num)
        return n


def sort(list1):
    sorted(list1)
    return list1


def func(s):
    print(s)


if __name__ == '__main__':
    print_hi('PyCharm')
    isFirst(100)
    print(sort([5, 3, 8, 7, 9, 1, 2]))
    func('hello for you')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
