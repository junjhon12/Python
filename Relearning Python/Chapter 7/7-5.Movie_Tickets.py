movie_tickets = False

while movie_tickets == False:
    age = int(input("Enter your age: "))
    if age < 3:
        print(f"Your ticket is free.")
        movie_tickets = True
    elif age < 12:
        print(f"Your ticket is $10.")
        movie_tickets = True
    else:
        print(f"Your ticket is $15.")
        movie_tickets = True
print("Enjoy the movie!")