"""
Testing Customer Class
Mariana Glz Bravo: A01630948
"""

import unittest

from customer import Customer
from hotel import Hotel


class TestCustomer(unittest.TestCase):
    """Class to test Customer Class"""

    customer = Customer(1, "Mariana G", "mariana@mariana.com")

    def setUp(self) -> None:
        self.customer = Customer(1, "Mariana G", "mariana@mariana.com")
        self.hotel = Hotel(1, "Hotel California", 100)

    def test_make_reservation(self):
        """should make a reservation for the customer at a hotel"""
        res = self.customer.make_reservation(1, self.hotel, 2)
        self.assertIn("Reservation made for Customer", res)

    def test_cancel_reservation(self):
        """should cancel a reservation made by the customer"""
        self.customer.make_reservation(1, self.hotel, 2)
        res = self.customer.cancel_reservation(1)
        self.assertIn(f"Reservation {1} canceled", res)


if __name__ == "__main__":
    unittest.main()
