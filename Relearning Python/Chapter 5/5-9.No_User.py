usernames = ['user1', 'user2', 'user3', 'user4', 'Admin']
#Checks if list is empty
if usernames:
    for username in usernames:
        if username == 'Admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again')
else:
    print("We need to find some users!")
    
