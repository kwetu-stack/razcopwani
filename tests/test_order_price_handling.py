import unittest
from decimal import Decimal

from blueprints.orders.routes import normalize_price


class OrderPriceNormalizationTests(unittest.TestCase):
    def test_keeps_whole_number_prices_without_cents(self):
        self.assertEqual(normalize_price("1200"), Decimal("1200"))

    def test_rounds_decimals_to_the_nearest_whole_number(self):
        self.assertEqual(normalize_price("1200.49"), Decimal("1200"))
        self.assertEqual(normalize_price("1200.50"), Decimal("1201"))


if __name__ == "__main__":
    unittest.main()
