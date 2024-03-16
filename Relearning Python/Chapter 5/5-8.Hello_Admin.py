usernames = ['user1', 'user2', 'user3', 'user4', 'Admin']

for username in usernames:
    if username == 'Admin':
        print(f'Hello {username}, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again')