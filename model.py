from dataclasses import dataclass

@ dataclass
class Item():
    # Содержит свойства для описания товара, цены и количества
    name_prod: str
    price: float
    amount: int

class Shop():
    # Хранит информацию о товарах, позволяет добавить новый товар, получить информацию о товарах, внести изменения 
    def __init__(self):
        # ининциализируем базу с информацией о товарах
        self.goods: dict[int, Item] = {
            0: Item("роза красная", 160, 200),
            1: Item("роза белая", 160, 220),
            2: Item("роза розовая", 160, 190),
            3: Item("роза кустовая", 120, 120),
            4: Item("пион", 200, 170),
            5: Item("гербера", 150, 220),
            6: Item("орхидея", 150, 195),
            7: Item("ирис", 140, 182),
            8: Item("лилия", 160, 156),
            9: Item("гортензия", 320, 15),
            10: Item("гвоздика", 120, 240),
            11: Item("лизиантус", 150, 206),
            12: Item("альстромерия", 140, 250)
        }
        self.last_id: int = max(self.goods.keys())
            
    def check_amount(self, id_prod) -> int:
        # проверка наличия нужного количества товра
        for k, v in self.goods:
            if k == id_prod:
               return Item.amount
            else:
                return None

    def add_item(self, name: str, price: float, amount: int) -> None:
        # добавление нового товара
        self.last_id += 1
        new_item = Item(name, price, amount)
        self.goods[self.last_id] = new_item

    def get_goods(self) -> list:
        # получение списка с информацией о товарах для дальнейшей передачи во view
        goods_list: list[dict] = []
        for k, v in self.goods.items():
            items: list = [k, v.name_prod, v.price, v.amount]
            goods_list.append(items)
        return goods_list
    
    def check_name_prod(self, name: str) -> bool:
        # проверка на присутствие наименования товара в база
        for value in self.goods.values():
            if name == value.name_prod:
                return True
        return False
    
    def check_id(self, id_prod: int) -> bool:
        # проверка наличия id в базе
        for k in self.goods.keys():
            if id_prod == k:
                return True
        return False

    def add_receipt(self, id_prod: int, amount: int) -> None:
        # добавление поступившего товара
        for k, v in self.goods.items():
            if id_prod == k:
                v.amount += amount
                return
            
    def change_price(self, id_prod: int, price: float) -> None:
        # изменение стоимости товара
        for k, v in self.goods.items():
            if id_prod == k:
                v.price = price
                return