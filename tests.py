from unittest import TestCase
import analyze

class Testing(TestCase):
    def test_make_decision(self):
        snippet = [0,0,0,0,0,1,2,3,4,5,6,7,8,9,10]
        method = 'Repeating Direction'
        decision = analyze.make_decision(snippet, method)
        self.assertEqual(decision, analyze.HOLD)

    def test_repeating_direction(self):
        rising = [1,2,3,4,54,56,57,77]
        decision = analyze.repeating_direction(rising)
        self.assertEqual(decision, analyze.SELL)

        falling = [9,8,7,6,6,5,4,3,2]
        decision = analyze.repeating_direction(falling)
        self.assertEqual(decision, analyze.BUY)

        neither = [1,1,1,1,2,2,2,2,2,1]
        decision = analyze.repeating_direction(neither)
        self.assertEqual(decision, analyze.HOLD)

    def test_trade_over_entire_series(self):
        price_vector = list(range(5000))
        start, end, current = analyze.trade_over_entire_series(price_vector)
        print(start, end, current)
        self.assertTrue(True)


