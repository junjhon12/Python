responses = {}
active = True

while active:
    name = input("Your name: ")
    response = input("If you could visit one place in the world, where would you go? ")
    
    responses[name] = response
    
    repeat = input("Finish? (yes or no) ")
    if repeat == 'no':
        active = False
    
    for name, response in responses.items():
        print(f'{name} dream is {response}')