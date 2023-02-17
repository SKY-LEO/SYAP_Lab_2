import pandas as pd

main_menu = ("1. Задание Классы\n ",
             "2. Задание Pandas\n ",
             "0. Выход")


class Kitty:
    __num_yes = 0
    __num_no = 0

    def __init__(self, name):
        self.name = name

    def to_answer(self):
        if self.__num_yes == self.__num_no:
            print("moore-moore")
            self.__num_yes += 1
        else:
            print("meow-meow")
            self.__num_no += 1

    def number_yes(self):
        print("Количество 'да': ", self.__num_yes)

    def number_no(self):
        print("Количество 'нет': ", self.__num_no)

    def get_name(self):
        print("Котенок", self.name)


def task1():
    kitty_1 = Kitty("Барсик")
    kitty_2 = Kitty("Мишка")
    kitty_1.get_name()
    kitty_1.to_answer()
    kitty_1.to_answer()
    kitty_1.number_yes()
    kitty_1.number_no()
    kitty_2.get_name()
    kitty_2.to_answer()
    kitty_2.to_answer()
    kitty_2.number_no()
    kitty_2.to_answer()
    kitty_2.number_yes()


def task2():
    sales = pd.read_excel('test.xlsx', sheet_name='sales')
    states = pd.read_excel('test1.xlsx', sheet_name='states')
    print("Содержимое sales:", sales.head(), sep="\n")
    print("Содержимое states:", states.head(), sep="\n")
    sales['MoreThan500'] = sales['Sales'] > 500
    print("Содержимое sales:", sales.head(), sep="\n")

    sales["Period"] = pd.date_range(start="12.31.2003", end="02.12.2023", periods=6)
    print("Содержимое колонки Period:", sales["Period"], sep="\n")

    sales["Date"] = pd.to_datetime(sales["Date"], dayfirst=True)

    print("Содержимое колонки Date:", sales["Date"], sep="\n")
    sales["Month"] = pd.DatetimeIndex(sales["Date"], dayfirst=True).month
    print("Содержимое колонки Month:", sales["Month"], sep="\n")

    pd.merge(sales, states, how='left', on='City').to_excel('test2.xlsx')
    print("Содержимое sales после объединения:", sales.head(), sep="\n")


def menu():
    while True:
        print("Список заданий:\n", "".join(main_menu))
        variant = input("Выберите задание: ")
        try:
            variant = int(variant)
        except ValueError:
            print("Введите целочисленное число!")
            continue
        if variant > len(main_menu) - 1 or variant < 0:
            print("Ошибка, введите число в заданном интервале!")
        else:
            match variant:
                case 1:
                    task1()
                case 2:
                    task2()
                case 0:
                    break
                case _:
                    print("Ошибка!")
                    return -1
    return 0


if __name__ == '__main__':
    menu()
