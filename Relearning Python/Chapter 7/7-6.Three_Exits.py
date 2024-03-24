while True:
    topping = input("What topping would you like:")
    
    if topping != 'quit':
        print(f'Adding {topping} to your pizza.')
        print('Enter "quit" to quit')
    else:
        break
print("Pizza is ready!")