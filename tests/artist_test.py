import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("Madonna")

    def test_artist_has_name(self):
        self.assertEqual("Madonna", self.artist.name)