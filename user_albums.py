def make_album(artist_name, album_title, number_of_song=None):
    dic = {"artist_name": artist_name,
            "album_title": album_title,}
    if number_of_song is not None:
        dic["number_of_song"] = number_of_song
    return dic

while True:
    artist_name = input("Artist name: ")
    if artist_name == "q":
        break
    album_title = input("Album title: ")
    if album_title == "q":
        break
    album = make_album(artist_name, album_title)
    print(f"Album name: {artist_name}")
    print(f"Album title: {album_title}")