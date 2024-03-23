def make_album(name, album):
    album = {
        f'Artist name': name,
        'Album': album,
    }
    return album

while True:
    name = input("Enter an artist's name: ")
    if name == 'q':
        break
    
    album = input("Enter album's name: ")
    if album == 'q':
        break
    
    print(make_album(name, album))