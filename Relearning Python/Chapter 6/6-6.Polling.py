"""
6-6. Polling: Use the code in favorite_languages.py (page 96).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""

need_Poll = {
    'Person A',
    'Person B',
    'Person C',
    'Person D',
    'Person E'
}

finish_Poll = {
    'Person B',
    'Person D',
    'Person E'
}

for name in need_Poll:
    if name in finish_Poll:
        print(f'Thanks for taking the poll {name}')
    else:
        print(f'Please take the poll {name}')