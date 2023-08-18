class Model:
    def __init__(self, items):
        self.items = items

    def get_item(self, item_name):
        for item in self.items:
            if item['name'] == item_name:
                return item
        return None

    def update_item_quantity(self, item_name, quantity):
        for item in self.items:
            if item['name'] == item_name:
                item['quantity'] += quantity  
                break
    
