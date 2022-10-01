import unittest
from src.card import Card
from src.card_game import CardGame


class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card_1 = Card("Hearts", 1)
        self.card_2 = Card("Spades", 5)
        self.card_3 = Card("Clubs", 8)
        self.card_game = CardGame()
        self.cards = [self.card_1, self.card_2, self.card_3]

    def test_card_has_a_suit(self):
        self.assertEqual("Hearts", self.card_1.suit)

    def test_card_has_a_value(self):
        self.assertEqual(5, self.card_2.value)

    def test_for_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_1))
    
    def test_for_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_2))

    def test_for_highest_card_first_highest(self):
        self.assertEqual(self.card_2, self.card_game.highest_card(self.card_2, self.card_1))

    def test_for_highest_card_second_highest(self):
        self.assertEqual(self.card_3, self.card_game.highest_card(self.card_2, self.card_3))

    def test_for_total(self):
        self.assertEqual("You have a total of 14", self.card_game.cards_total(self.cards))

    