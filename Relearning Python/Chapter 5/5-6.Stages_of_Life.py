import random
def stages(int):
    if person > 1:
        if person < 2:
            print('Baby')
        elif person >= 2 and person < 4:
            print('Todler')
        elif person >= 4 and person < 13:
            print('Kid')
        elif person >= 13 and person < 20:
            print('Teenager')
        elif person >= 20 and person < 65:
            print('Adult')
        else:
            print('Elder')
    else:  
        print()
            
person = random.randrange(1, 100)
print(stages(person))