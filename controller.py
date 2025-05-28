from model import Shop
from view import ShopView

class ShopController():
    # обрабатывает пользовательский ввод, вызывает соответствующие методы Shop и обновляет ShopView

    def __init__(self, shop_view: ShopView):
        self.shop_view = shop_view

    def get_number(self) -> str:
    # получение числа от пользователя (выбранный пункт меню)
        print("\nВведите число, соответствующее выбранному пункту меню:\n")
        self.number = self.shop_view.check_input()
        return str(self.number)
    
    def get_item(self) -> str: 
        # запрашиваем наименование нового товара у пользователя для добавления в список
        return input("Введите название товара:\n")
    
    def run(self) -> None:
    # выводит меню пользователю и вызывает соответствующие функции классов TodoList, TodoView и TodoController
        shop = Shop()
        view = ShopView(shop)
        print("\n Добро пожаловать в оноайн-магазин цветов!")
        print("Выберите нужный раздел:")
        print("1. Показать информацию по всем цветам в базе")
        print("2. Добавить новую позицию в базу")
        print("3. Внести информацию о поступлении")
        print("4. Изменить цену товара")
        print("5. Удалить позицию")
        print("6. Оформить продажу")
        print("7. Показать отчет о продажах")
        print("0. Выйти")
        while True:
            choice = self.get_number()
            match choice:
                case '1':
                    view.show_goods()
                case '2':
                    view.show_tasks()
                case '3':
                    view.show_tasks(False)
                case '4':
                    view.show_tasks(True)
                case '5':
                    task_id = view.pass_check_task_id()
                    view.pass_change_task_status(task_id)
                case '6':
                    task_id = view.pass_check_task_id()
                    text = self.get_task()
                    view.pass_edit_task_text(task_id, text)
                case '7':
                    task_id = view.pass_check_task_id()
                    view.pass_delete_task(task_id)
                case '0':
                    break
                case _:
                    print("Раздел с введенным номером не найден")