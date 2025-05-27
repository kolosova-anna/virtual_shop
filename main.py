from controller import ShopController
from model import Shop
from view import ShopView

def main() -> None:
    # выводит меню пользователю и вызывает соответствующие функции классов TodoList, TodoView и TodoController
    shop = Shop()
    shop_view = ShopView(shop)
    controller = ShopController(shop_view)
    controller.run()

if __name__ == "__main__":
    main()