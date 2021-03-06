import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album("Abbey Road", "rock", "The Beatles")

    def test_album_has_title(self):
        self.assertEqual("Abbey Road", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("rock", self.album.genre)

    def test_album_has_artist(self):
        self.assertEqual("The Beatles", self.album.artist)