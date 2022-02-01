import pdb
from models.artist import Artist
import repositories.artist_repository as artist_repository

artist_1 = Artist("The Beatles")
artist_repository.save(artist_1)

result = artist_repository.select_all()

for artist in result:
    print(artist.__dict__)

pdb.set_trace()