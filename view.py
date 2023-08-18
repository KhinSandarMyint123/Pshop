class View:
    def display_items(self, items):
        print("Available items:")
        print("Item Name\tPrice\tQuantity")
        for item in  items:
            print(f" {item['name']}\t {item['price']}MMK\t {item['quantity']}")

    def get_user_selection(self):
        item_name = input("Enter the name of the item you want to purchase: ")
        quantity = int(input("Enter the quantity: "))
        return item_name, quantity

    def display_total(self, total_amount):
        print(f"Total amount: {total_amount}MMK")
    