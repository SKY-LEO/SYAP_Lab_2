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
    return


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


