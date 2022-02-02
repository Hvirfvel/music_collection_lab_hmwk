import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("The Beatles")
artist_repository.save(artist_1)

artist_result = artist_repository.select_all()

for artist in artist_result:
    print(artist.__dict__)

album_1 = Album("Abbey Road", "rock", "The Beatles")
album_repository.save(album_1)

album_result = album_repository.select_all()

for album in album_result:
    print(album.__dict__)

pdb.set_trace()