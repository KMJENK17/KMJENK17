
shopping_list =[]

class ShoppingList:
    def __init__(self, title, address):
        self.title = title
        self.address = address
        self.items = []
        
        
class Items:
    def __init__(self, title, price, quantity):
        self.title = title
        self.price = price
        self.quantity = quantity 
    

while True:
    print("------------- Grocery App -------------")
    print("")
    print("1. to Add a store to your shopping list")
    print("2. to Add items to your shopping list")
    print("3. to View your shopping lists")
    print("4. to Delete an item from a list")
    print("5. to Quit")
    print("")
    print ("--------------------------------------")
    option = input("Enter your option: ")

    
    if option == "1":
        store_name = input("Enter store name: ")
        store_addy = input("Enter store address: ")
        store = ShoppingList(store_name, store_addy)
        shopping_list.append(store)

    if option == "2":
      

        for i in range(0, len(shopping_list)):
            print(f"{i + 1} - {shopping_list[i].title}")
            store = shopping_list[i]
        store_index = int(input("Enter the store number: "))
        item_name = input("Enter the name of the item: ")
        price = float(input("Enter the price: "))
        quantity = int(input("Enter the quantity: "))
        thing = Items(item_name, price, quantity)
        
        shopping_list[store_index -1].items.append(thing)
      
     

    if option == "3":
        i = 1
        for index in range(0, len(shopping_list)):
            store = shopping_list[index]
            print(f"{i} - store name: {store.title},   store address: {store.address}")
            i += 1
        for index in range(0, len(store.items)):
            title = store.items[index].title
            quantity = store.items[index].quantity 
            print(title, quantity)
    
    if option == "5":
        for i in range(0, len(shopping_list)):
           print(f"{i +1}--{shopping_list[i].name}")
           store = shopping_list[i]
        choice3 = int(input("Enter store choice: "))
        store = shopping_list[choice3 - 1]
        for i in range(0, len(store.items)):
            print(f"{i + 1} {store.items[i].title}")
        itemToDeleteIndex = int(input("Enter item to delete: "))
        del store.items[itemToDeleteIndex]
        print("Item deleted.")
        
       
    if option == "5":
        break

    else: 
        print("Please enter a choice from the menu.")