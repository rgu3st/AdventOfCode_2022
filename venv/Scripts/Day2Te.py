import unittest
import Day2 as d2

class Day2TestCases(unittest.TestCase):
    def test_calculate_tie_score(self):
        opp_choice = 'A'
        my_choice = 'Y'
        score = d2.calculate_score(d2.decode_choice(opp_choice), d2.decode_choice(my_choice))
        self.assertEqual(score, 4)
        print("[...] Tie test passed")

    def test_rock_scissors_win_score(self):
        opp_choice = 'C'
        my_choice = 'Y'
        score = d2.calculate_score(d2.decode_choice(opp_choice), d2.decode_choice(my_choice))
        self.assertEqual(score, 7)
        print("[...] Win test passed")

    def test_paper_scissors_lose_score(self):
        opp_choice = 'C'
        my_choice = 'X'
        score = d2.calculate_score(d2.decode_choice(opp_choice), d2.decode_choice(my_choice))
        self.assertEqual(score, 2)
        print("[...] Lose Rock vs. Scissors test passed")

    '''
    test_always_fails(self):
        self.assertEqual(True, False)
    '''
if __name__ == '__main__':
    unittest.main()
