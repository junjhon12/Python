topping = ''
while topping != 'quit':
    topping = input("Enter a topping: ")
    if topping != 'quit':
        print(f'Adding {topping} to your pizza.')
        print('Enter "quit" to ')
    else:
        break
print("Your pizza is ready.")