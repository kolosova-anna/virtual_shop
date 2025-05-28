from model import Shop
import tabulate as tl

class ShopView():
    # отвечает за отображение товаров в магазине и обработки взаимодействия с пользователем

    def __init__(self, shop: dict):
        self.shop: dict = shop

    def check_input(self) -> int:
    # проверка введенного пользователем числа
        while True:
            try:
                number = int(input())
                return number
            except ValueError:
                print("Ошибка. Введите число")

    def show_goods(self) -> None:
        # вывод информации о товарых в магазине
        goods = self.shop.get_goods()
        if not goods:
            print("Товары в магазине отсутствуют")
            return
        print("Информация о товарах в магазине:")
        headers = ["id", "наименование", "цена", "количество"]
        print(tl.tabulate(goods, headers=headers, tablefmt="grid"))