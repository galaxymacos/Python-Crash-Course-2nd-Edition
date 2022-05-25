def make_album(artist_name, album_title, number_of_song=None):
    dic = {"artist_name": artist_name,
            "album_title": album_title,}
    if number_of_song is not None:
        dic["number_of_song"] = number_of_song
    return dic


jay_chou_album = make_album("Jay Chou", "Qilixiang")
bruno_mars_album = make_album("Bruno Mars", "Unorthodox Jukebox")
eminem_album = make_album(artist_name="Eminem", album_title="The Eminem Show", number_of_song=20)
print(jay_chou_album["artist_name"])
print(jay_chou_album["album_title"])
print(eminem_album["number_of_song"])
