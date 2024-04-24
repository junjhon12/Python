"""
Start with a copy of user_profile.py from page 148. Build a
profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

my_profile = build_profile('Quoc', 'Le', interest = 'Front-End', hobby = 'manga', field = 'CS')
print(my_profile)