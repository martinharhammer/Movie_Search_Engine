import unittest

from ir_exercise.test.utils import send_request


class DarkShadowsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Johnny Depp as a Vampire"
        self.gold = "Dark Shadows (film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class SuperSizeMe(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Mordan Spurlogg documentary about fast food"
        self.gold = "Super Size Me"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class ZootopiaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "rabbit police officer"
        self.gold = "Zootopia"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class JumperTest(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "2008 action movie about teleportation"
        self.gold = "Jumper (2008 film)"

    def test_top_10(self):
        docs = send_request(self.text, 10)
        self.assertIn(self.gold, docs)

    def test_top_5(self):
        docs = send_request(self.text, 5)
        self.assertIn(self.gold, docs)

    def test_top_1(self):
        docs = send_request(self.text, 1)
        self.assertIn(self.gold, docs)


class ChangeOfHeart(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "Change of He"
        self.gold = "A Change of Heart (film)"

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

