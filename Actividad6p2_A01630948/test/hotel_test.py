"""
Testing Hotel Class
Mariana Glz Bravo: A01630948
"""

import unittest

from customer import Customer
from hotel import Hotel


class TestHotel(unittest.TestCase):
    """Class to test Hotel Class"""

    hotel = Hotel(1, "Hotel California", 100)

    def setUp(self) -> None:
        self.hotel = Hotel(1, "Hotel California", 100)

    def test_get_available_rooms(self):
        """should get the number of available rooms in the hotel"""
        res = self.hotel.get_available_rooms()

        self.assertEqual(res, 100)

    def test_make_reservation(self):
        """should make a reservation in the hotel for a customer"""
        customer = Customer(1, "Mariana G", "mariana@mariana.com")

        res = self.hotel.make_reservation(customer, 2)

        self.assertIn("Room reserved at Hotel", res)

    def test_make_reservation_negative(self):
        """should not make a reservation in the hotel for a customer"""
        customer = Customer(1, "Mariana G", "mariana@mariana.com")

        res = self.hotel.make_reservation(customer, 120)

        self.assertNotIn("Room reserved at Hotel", res)


if __name__ == "__main__":
    unittest.main()
