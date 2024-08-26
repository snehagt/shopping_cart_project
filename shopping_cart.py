import string
from items_shopping import items_dict

class ShoppingCart():
    ''' Menu driven program to add carts
    Items =
        {
            1: {
                item_name : 
                item_quantity:
                per_item_cost_ : 
            },
            2: {
                item_name : 
                item_quantity:
                per_item_cost_ : 
            },
        } 
    '''
    
    def __init__(self) -> None:
        self.items = {
            1: {
                'item_name' : 'Laptop',
                'item_quantity': 2,
                'per_item_cost' : 13.33
            },
        }

    def show_items(self):
        print("Item: Price")
        for item, price in items_dict.items():
            print(f"{item}: ${price}")

    def add_item_list(self, item_name, item_quantity) -> None:
        self.show_items()
        self.check_item_list()
        key = len(self.items) + 1
        per_item_cost = items_dict.get(item_name, None)
        if per_item_cost is not None:
            self.items[key] = {
                'item_name': item_name,
                'item_quantity': item_quantity,
                'per_item_cost': per_item_cost
            }
            print(f"{item_name} added to the cart.")
            print(self.items)
        else:
            print("Item not found in the inventory.")

    def check_item_list(self) -> dict:
        print(' :) ---------- Items in your cart are: --------------- ')
        for key, value in self.items.items():
            print(f'Item number : {key}')
            print(f'    Item_name: {value["item_name"]} \n    Quantity: {value["item_quantity"]}')
            total_item_cost = value['per_item_cost'] * value['item_quantity']
            print(f'    Total Item cost: {total_item_cost}')
            
        return self.items
    
    def total_cost(self) -> int:
        total_cart_cost = 0
        for key, value in self.items.items():
            total_item_cost = value['per_item_cost'] * value['item_quantity']
            total_cart_cost+= total_item_cost

        return total_cart_cost

    def remove_item_list(self) -> None:
        self.check_item_list()
        if not self.items: 
            raise Exception("Your cart is empty. There are no items to remove.")

        while True:
            try:
                remove_item = str(input('Enter item to remove from your cart: ')).capitalize()
                if not remove_item.isalpha():
                    raise ValueError("Item name can only contain alphabetic characters.")
                break
            except ValueError as e:
                print(f"Error: {e}")

        for key, value in self.items.items():
            print(value.values())
            if remove_item in value.values():
                try:
                    remove_item_quantity = int(input('Enter quantity to remove: '))
                    print(value['item_quantity'])
                    if value['item_quantity'] - remove_item_quantity < 0 :
                        raise ValueError("Quantity exceeds the limit.")
                    elif value['item_quantity'] - remove_item_quantity == 0:
                        del self.items[key]
                        print('Item removed from your cart')
                        print(self.items)
                        break
                    else:
                        value['item_quantity'] -= remove_item_quantity
                        print("Items Removed!")
                except ValueError as e:
                    print(f"Exception Occurred: {e}")
                    self.remove_item_list()
                    break
                print(self.items)

class checkout(ShoppingCart):
    '''
        checkout():
            address - static of class
            pin code
            total different order items 
            total cost 
        '''
    
    def __init__(self, items, address, pincode):
        super().__init__()
        self.items = items
        self.address = address
        self.pincode = pincode

    def total_items(self):
        return len(self.items)

    def __str__(self):
        total_cart_cost = super().total_cost()
        list_items = list(self.items.values())
        return f'Total Items in your cart is {len(self.items)} while total cost here is {total_cart_cost}. Below is your order {list_items}. \
                Confirmed your order with address {self.address} and pincode {self.pincode}'
class Menu():
    
    def __init__(self):
        self.cart = ShoppingCart()

    @staticmethod
    def print_shopping_cart():
        shopping_cart = [
            "   _______________",
            " /                \\",
            "|   ____________   |",
            "|  |   INSTA    |  |",
            "|  |   ______   |  |",
            "|  |  |      |  |  |",
            "|  |  | MART |  |  |",
            "|  |  |______|  |  |",
            "|  |____________|  |",
            "|__________________|"
        ]
        
        for line in shopping_cart:
            print(line)
            
    def run_program(self) -> None:
        self.print_shopping_cart()

        def add_item_choice():          
                while True:
                    try:
                        item_name = (input('Enter item to add to your cart: ')).capitalize()
                        if item_name.isdigit():
                            raise ValueError("Please enter valid name.")
                        item_quantity = int(input('Please specify quantity for your item: '))
                        break
                    except ValueError as e:
                        print(e)
                self.cart.add_item_list(item_name, item_quantity)

        def checkout_choice():
            adddress = str(input('Enter your address for checkout: '))
            while True:
                try:
                    pincode = int(input('Enter your pin code: '))
                    break        #if pincode is corrct then we need to break 
                except ValueError as e:
                    print('Please enter integer for pin code!')
            obj2 = checkout(self.cart.items,adddress, pincode)
            print(obj2)   #when object is called __str__ is printed

        def remove_item_choice():
            self.cart.remove_item_list()

        def check_item_choice():
            self.cart.check_item_list()

        while True:
            print('\nHello! Welcome to InstaMart\n')
            print(
                '1. Add Items: \n2. Remove Items: \n3. Check Orders \n4. Checkout \n5. Exit'
            ) 
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_item_choice()
            elif choice == 2:
                remove_item_choice()
            elif choice == 3:
                check_item_choice()  # Note: Call as a class method with self.cart as argument
            elif choice == 4:
                checkout_choice()
            elif choice == 5:
                break
            else:
                print('Invalid Choice')

menu_obj = Menu()
menu_obj.run_program()