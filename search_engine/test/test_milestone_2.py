import unittest

from ir_exercise.test.utils import send_request


class LordOfTheRingsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "LoR movie featuring Battle of Helms Deep"
        self.gold = "The Lord of the Rings: The Two Towers"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class InsideOutTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Inside Out two"
        self.gold = "Inside Out 2"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class HundredTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "100"
        self.gold = "100 (2008 film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class GlassOnionTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "COVID movie featuring murder case"
        self.gold = "Glass Onion: A Knives Out Mystery"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class AlienTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "american fiction movie directed by Fede Alvarez"
        self.gold = "Alien: Romulus"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


if __name__ == "__main__":
    unittest.main()

