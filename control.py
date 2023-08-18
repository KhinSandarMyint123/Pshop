class Control:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def calculate_total_amount(self, item_name, quantity):
        item = self.model.get_item(item_name)
        if item and item['quantity'] >= quantity:
            total_amount = item['price'] * quantity
            return total_amount
        else:
            return 0

    def process_purchase(self, item_name, quantity):
        total_amount = self.calculate_total_amount(item_name, quantity)
        if total_amount > 0:
            purchased_item = self.model.get_item(item_name)
            if purchased_item and purchased_item['quantity'] >= quantity:
                purchased_item['quantity'] -= quantity
                self.model.update_item_quantity(item_name, quantity) 
                return total_amount
            else:
                print("Item not available or insufficient quantity.")
                return 0
        else:
            return 0
        
    