from view import View
from control import Control
from model import Model

def main():
    items_vm1 = [
        { "name": "Samsung", "price": 350000, "quantity": 5 },
        { "name": "Redmi7", "price": 411000, "quantity": 8 },
        { "name": "Iphone 13pro", "price": 2236700, "quantity": 4 }
       
    ]

    items_vm2 = [
        { "name": "Redmi7", "price": 411000, "quantity": 2 },
        { "name": "Iphone 13pro Max", "price": 3276700, "quantity": 4 },
        { "name": "Iphone 13pro", "price": 2236700, "quantity": 4 },
        { "name": "Samsung", "price": 350000, "quantity": 3 }
       ]
    items_vm3 = [
        { "name": "Redmi7", "price": 411000, "quantity": 2 },
        { "name": "Iphone 13pro Max", "price": 3276700, "quantity": 4 },
        { "name": "Iphone 13pro", "price": 2236700, "quantity": 4 },
        { "name": "Samsung", "price": 350000, "quantity": 3 }
       ]
    items_vm4 = [
        { "name": "Samsung", "price": 350000, "quantity": 5 },
        { "name": "Redmi7", "price": 411000, "quantity": 8 },
        { "name": "Iphone 13pro", "price": 2236700, "quantity": 4 }
       
    ]
    items_vm5 = [
        { "name": "Vivo", "price": 250000, "quantity": 5 },
        { "name": "Redmi 11", "price": 421000, "quantity": 8 },
        { "name": "Iphone 13pro", "price": 2236700, "quantity": 4 },
        { "name": "Iphone 14pro Max", "price": 38236700, "quantity": 4 }
       
    ]
    view = View()
    model_vm1 = Model(items_vm1)
    control_vm1 = Control(model_vm1, view)
    model_vm2 = Model(items_vm2)
    control_vm2 = Control(model_vm2 ,view)
    model_vm3 = Model(items_vm3)
    control_vm3 = Control(model_vm3 ,view)
    model_vm4 = Model(items_vm4)
    control_vm4 = Control(model_vm4 ,view)
    model_vm5 = Model(items_vm5)
    control_vm5 = Control(model_vm5 ,view)
    
    # model = Model(control)
    
    # control = Control(model)

    # item_name = input("Enter the name of the item to add quantity: ")
    # quantity_to_add = int(input("Enter the quantity to add: "))

    # control.add_item_quantity(item_name, quantity_to_add)
    while True:
        print("\nSelect a Phone Accessories Shop:")
        print("1. Hlaing Branch MobilePhone")
        print("2. Sanchaung Branch1 MobilePhone")
        print("3. Sanchaung Branch2 MobilePhone")
        print("4. Hledan Branch MobilePhone")
        print("5. North Dagon Branch MobilePhone")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            view.display_items(items_vm1)
            item_name, quantity = view.get_user_selection()
            
            total_amount = control_vm1.process_purchase(item_name, quantity)
            
            if total_amount > 0:
              view.display_total(total_amount)
              payment = int(input("Enter  payment or any other key to cancel: "))
              if payment >= total_amount:
                coin = payment-total_amount
                print("Your remain balance is:" ,coin)
                new_quantity = int(input("Enter the new quantity: "))
                model_vm1.update_item_quantity(item_name, new_quantity- quantity)
                total_amount = total_amount * new_quantity /quantity
                print(f"Remaining {item_name} quantity:", control_vm1.model.get_item(item_name)['quantity']) 
              else:
                print("Your Balance is Insufficinet!")
            
            else:
             print("Item not available or insufficient quantity.")
        elif choice == "2":
           view.display_items(items_vm2)
           item_name, quantity = view.get_user_selection()
           total_amount = control_vm2.process_purchase(item_name, quantity)
           if total_amount > 0:
            view.display_total(total_amount)
            payment = int(input("Enter  payment or any other key to cancel: "))
            if payment >= total_amount:
                coin = payment-total_amount
                print("Your remain balance is:" ,coin)
                new_quantity = int(input("Enter the new quantity: "))
                model_vm2.update_item_quantity(item_name, new_quantity- quantity)
                total_amount = total_amount * new_quantity/ quantity
                print(f"Remaining {item_name} quantity:", control_vm2.model.get_item(item_name)['quantity']) 
            else:
                print("Your Balance is Insufficinet!")
            
           else:
            print("Item not available or insufficient quantity.")
        elif choice == "3":
           view.display_items(items_vm3)
           item_name, quantity = view.get_user_selection()
           total_amount = control_vm3.process_purchase(item_name, quantity)
           if total_amount > 0:
            view.display_total(total_amount)
            payment = int(input("Enter  payment or any other key to cancel: "))
            if payment >= total_amount:
                coin = payment-total_amount
                print("Your remain balance is:" ,coin)
                new_quantity = int(input("Enter the new quantity: "))
                model_vm3.update_item_quantity(item_name, new_quantity- quantity)
                total_amount = total_amount * new_quantity/ quantity
                print(f"Remaining {item_name} quantity:", control_vm3.model.get_item(item_name)['quantity']) 
            else:
                print("Your Balance is Insufficinet!")
            
           else:
            print("Item not available or insufficient quantity.")
        elif choice == "4":
           view.display_items(items_vm4)
           item_name, quantity = view.get_user_selection()
           total_amount = control_vm4.process_purchase(item_name, quantity)
           if total_amount > 0:
            view.display_total(total_amount)
            payment = int(input("Enter  Your payment : "))
            if payment >= total_amount:
                coin = payment-total_amount 
                print("Your remain balance is:" ,coin)
                new_quantity = int(input("Enter the new quantity: "))
                model_vm4.update_item_quantity(item_name,new_quantity- quantity)
                total_amount = total_amount * new_quantity/ quantity
                print(f"Remaining {item_name} quantity:", control_vm4.model.get_item(item_name)['quantity']) 
            else:
                print("Your Balance is Insufficinet!")
            
           else:
            print("Item not available or insufficient quantity.")
        elif choice == "5":
           view.display_items(items_vm5)
           item_name, quantity = view.get_user_selection()
           total_amount = control_vm5.process_purchase(item_name, quantity)
           if total_amount > 0:
            view.display_total(total_amount)
            payment = int(input("Enter  payment or any other key to cancel: "))
            if payment >= total_amount:
                  coin = payment-total_amount
                  print("Your remain balance is:" ,coin)
                  new_quantity = int(input("Enter the new quantity: "))
                  model_vm5.update_item_quantity(item_name,new_quantity- quantity)
                  total_amount = total_amount * new_quantity/ quantity
                  print(f"Remaining {item_name} quantity:", control_vm5.model.get_item(item_name)['quantity']) 
            else:
                  print("Your Balance is Insufficinet!")
            
           else:
            print("Item not available or insufficient quantity.")
        elif choice == "6":
            print("Goodbye!")
            
            break
       
        else:
            print("Invalid choice. Please try again.")

    
if __name__ == "__main__":
    main()
