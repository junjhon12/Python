current_users = ['user1', 'user2', 'user3', 'user4', 'user5']
new_users = ['USER1', 'USER2', 'user6', 'user7', 'user8']

current_users = [x.lower() for x in current_users]
new_users = [x.lower() for x in new_users]

if new_users:
    for new_user in new_users:
        if new_user in current_users:
            print(f'{new_user} will need to enter a new username')
        else:
            print('username is available')
else:
    print('None')