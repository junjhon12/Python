class User():
    #Doesn't have a init since it's not storing any information
    def sign_in(self):
        print('logged in')
    
    class Wizard(User):
        def __init__(self, name, power):
            self.anme = name
            self.power = power
        def attack(self):
            print(f'attacking with power of {self.power}')
    
    class Archer(User):
        def __init__(self, name, num_arrows):
            self.anme = name
            self.num_arrows = num_arrows
        def attack(self):
            print(f'attacking with arrows: arrows left - {self.num_arrows}')
    
   
    
    wizard1 = Wizard('Merlin', 50)
    archer1 = Archer('Robin', 100)
    print(wizard1.attack()) isinstance(wizard1, Wizard)
    print(isinstance(wizard1, User))