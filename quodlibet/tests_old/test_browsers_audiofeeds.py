from tests import TestCase, add

from quodlibet.browsers.audiofeeds import AudioFeeds
from quodlibet.player import PlaylistPlayer
from quodlibet.library import SongLibrary

class TAudioFeeds(TestCase):
    def setUp(self):
        self.library = SongLibrary()
        AudioFeeds.init(self.library)
        self.bar = AudioFeeds(self.library, PlaylistPlayer('fakesink'))

    def test_can_filter(self):
        for key in ["foo", "title", "fake~key", "~woobar", "~#huh"]:
            self.failIf(self.bar.can_filter(key))

    def tearDown(self):
        self.bar.destroy()
        self.library.destroy()
add(TAudioFeeds)