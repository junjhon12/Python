def make_album(name, album):
    album = {
        f'Artist name': name,
        'Album': album,
    }
    return album

print(make_album('name1', 'album1'))
print(make_album('name2', 'album2'))
print(make_album('name3', 'album3'))