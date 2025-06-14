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
                print("Ошибка. Введите целое число ")

    def get_price(self) -> float:
        # Запрос стоимости товара
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
        headers = ["id", "наименование", "цена, руб.", "количество, шт."]
        print(tl.tabulate(goods, headers=headers, tablefmt="grid"))

    def pass_add_item(self, name: str) -> None:
        # получение и передача данных для добавления нового товара в базу
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

    def get_id(self) -> int:
        # запрос id товара у пользователя
        while True:
            try:
                print("Введите id товара")
                id_prod = self.check_input()
                check_id = self.shop.check_id(id_prod)
                if check_id is True:
                    return id_prod
                print(f"Ошибка. Товар с id {id_prod} не найден")
                self.show_goods()
            except ValueError:
                print("ошибка ввода")
                

    def pass_add_receipt(self, id_prod: int) -> None:
        # запрос и изменение количества товара
        new_amount = self.get_amount()
        self.shop.add_receipt(id_prod, new_amount)
        print("Количество товара изменено")
        self.show_goods()

    def pass_change_price(self, id_prod: int) -> None:
        # заспрос и изменение стоимости товара
        new_price = self.get_price()
        self.shop.change_price(id_prod, new_price)
        print("Стоимость товара изменена")
        self.show_goods()

    def pass_delete_item(self, id_prod: int) -> None:
        # удаление товара из базы
        self.shop.delete_item(id_prod)
        print(f"Товар с id {id_prod} удален из базы")
        self.show_goods()

    def check_amount(self, id_prod: int, amount: int) -> bool:
        # получение ответа о наличии достаточного количества товара для продажи
        quantity = self.shop.get_amount(id_prod)
        if quantity >= amount:
            return True
        else:
            return False

    def complete_sale(self, id_prod: int, amount: int) -> list:
        # оформление продажи
        check_amount = self.check_amount(id_prod, amount)
        if check_amount is True:
            check: list = self.shop.new_sale(id_prod, amount)
            headers = ["id", "наименование", "цена", "количество", "стоимость"]
            print("Чек о продаже сформирован:")
            print(tl.tabulate(check, headers=headers, tablefmt="grid"))
        else:
            quantity = self.shop.get_amount(id_prod)
            print(f"Недостаточно товара для продажи. В наличии есть {quantity} шт.")

    def show_report(self) -> None:
        # вывод отчета о продажах
        report: list = self.shop.sale_report()
        if not report:
            print("Ни одной продажи не найдено")
            return
        print("Отчкт о продажах:")
        headers = ["id", "наименование", "цена", "количество", "сумма"]
        print(tl.tabulate(report, headers=headers, tablefmt="grid"))
        total_sum = self.shop.get_total_sum()
        print(f"Сумма всех продаж составила {total_sum:,.2f} руб.")
