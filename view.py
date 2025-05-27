from model import Shop

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