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
                print("Ошибка. Введите число ")

    def get_price(self) -> float:
        while True:
            try:
                price = float(input("Введите стоимость: "))
                return price
            except ValueError:
                print("Ошибка. Введите число ")

    def get_amount(self) -> int:
        # Запрашивает количество товара у пользователя
        print("Введите количество товара ")
        amount = self.check_input()
        return amount

    def show_goods(self) -> None:
        # вывод информации о товарых в магазине
        goods = self.shop.get_goods()
        if not goods:
            print("Товары в магазине отсутствуют")
            return
        print("Информация о товарах в магазине:")
        headers = ["id", "наименование", "цена", "количество"]
        print(tl.tabulate(goods, headers=headers, tablefmt="grid"))

    def pass_add_item(self, name: str) -> None:
        name_check = self.shop.check_name_prod(name)
        if name_check is False:
            price = self.get_price()
            amount = self.get_amount()
            self.shop.add_item(name, price, amount)
            print("Товар добавлен")
            return
        else:
            print(f"В базе уже есть товар с введенным наименованием.")
            print("Хотите внести информацию о поступлении?")