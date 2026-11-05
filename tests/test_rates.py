import unittest

from warehouse.rates import shipping_quote


class RateTests(unittest.TestCase):
    # ------------------------------------------------------------------
    # Standard service (existing behaviour must be unchanged)
    # ------------------------------------------------------------------
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", service="standard"), 11.0)

    # ------------------------------------------------------------------
    # Express service ($7 surcharge on top of standard)
    # ------------------------------------------------------------------
    def test_express_local(self):
        # local base 5.0 + express surcharge 7.0 + 1.5*2 = 15.0
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        # regional base 8.0 + express surcharge 7.0 + 1.5*2 = 18.0
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # local base 5.0 + 7.0 + 1.5*1.5 = 14.25
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "international")

    def test_invalid_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
