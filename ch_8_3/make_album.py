def make_album(singer, title, num_songs = None):
    """Return a dictionary representing a music album."""
    album = {'singer': singer.title(), 'title': title.title()}
    if num_songs:
        album['num_songs'] = num_songs
    return album

# print(make_album('Taylor Swift', '1989'))
# print(make_album('Ed Sheeran', 'Divide', 12))
# print(make_album('Adele', '25', 11))

while True:
    print("\nPlease enter the singer and album title (or 'q' to quit):")
    singer = input("Singer: ")
    if singer.lower() == 'q':
        break
    title = input("Album title: ")
    if title.lower() == 'q':
        break
    num_songs = input("Number of songs (optional): ")
    if num_songs.lower() == 'q':
        break
    if num_songs.isdigit():
        album_info = make_album(singer, title, int(num_songs))
    else:
        album_info = make_album(singer, title)
    print(album_info)