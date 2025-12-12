import unittest
from api.horo import HoroAPI

class TestHoroAPI(unittest.TestCase):
    def setUp(self):
        self.user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.0) AppleWebKit/532.1.0 (KHTML, like Gecko) Chrome/34.0.822.0 Safari/532.1.0"
        self.parser = HoroAPI(self.user_agent)

    def test_today_all(self):
        title, text = self.parser.get_today_all()
        self.assertTrue(len(title) > 0)
        self.assertTrue(len(text) > 0)

    def test_horo(self):
        title, text = self.parser.get_horo("aries", "today")
        self.assertTrue(len(title) > 0)
        self.assertTrue(len(text) > 0)

if __name__ == "__main__":
    unittest.main()