class VendingMachine:
    def __init__(self, soda_count, coffee_count, water_count):
        self.soda_count = soda_count
        self.coffee_count = coffee_count
        self.water_count = water_count

    def purchase(self, drink_type):
        if drink_type == 1:
            if self.soda_count > 0:
                print("Enjoy your Soda!")
                self.soda_count -= 1
            else:
                print("Sorry, Soda is out of stock.")
        elif drink_type == 2:
            if self.coffee_count > 0:
                print("Enjoy your Coffee!")
                self.coffee_count -= 1
            else:
                print("Sorry, Coffee is out of stock.")
        elif drink_type == 3:
            if self.water_count > 0:
                print("Enjoy your Water!")
                self.water_count -= 1
            else:
                print("Sorry, Water is out of stock.")
        else:
            print("Invalid drink type.")

    def restock(self, drink_type, amount):
        if drink_type == 1:
            self.soda_count += amount
        elif drink_type == 2:
            self.coffee_count += amount
        elif drink_type == 3:
            self.water_count += amount
        else:
            print("Invalid drink type.")

    def report_inventory(self):
        print("Inventory")
        print(f"Soda: {self.soda_count} bottles")
        print(f"Coffee: {self.coffee_count} bottles")
        print(f"Water: {self.water_count} bottles")


# Program implementation
vending_machine = VendingMachine(soda_count=10, coffee_count=10, water_count=10)

while True:
    print("(buy, inventory, or restock. (Quit by typing 'quit or 'q')): ", end="")
    command = input().lower()

    if command in ['quit', 'q']:
        break

    if command == 'buy':
        print("Please select an option:")
        print("1 - Soda\n2 - Coffee\n3 - Water")
        drink_type = int(input(" "))
        vending_machine.purchase(drink_type)

    elif command == 'inventory':
        vending_machine.report_inventory()

    elif command == 'restock':
        print("Please select an option:")
        print("1 - Soda\n2 - Coffee\n3 - Water")
        try:
            drink_type = int(input(" "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        print("Please Enter an amount:")
        try:
            amount = int(input(" "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        vending_machine.restock(drink_type, amount)

    else:
        print("Invalid command. Try again.")
