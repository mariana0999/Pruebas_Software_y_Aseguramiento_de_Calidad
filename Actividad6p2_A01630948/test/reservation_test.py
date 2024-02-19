"""
Testing Reservation Class
Mariana Glz Bravo: A01630948
"""

import unittest

from reservation import Reservation


class TestReservation(unittest.TestCase):
    """Class to test Reservations"""

    reservation = Reservation(1, "Mariana G", "Hotel California", 2)

    def setUp(self) -> None:
        self.reservation = Reservation(1, "Mariana G", "Hotel California", 2)

    def test_get_reservation_info(self):
        """Should return the reservation info string succesfully"""
        info = self.reservation.get_reservation_info()
        self.assertTrue(isinstance(info, str))

    def test_modify_room(self):
        """Should change the room count succesfully"""
        room_count = self.reservation.modify_room_count(3)
        self.assertIn(f"modified to {3}", room_count)

    def test_modify_room_neg(self):
        """Should change the room count unsuccesfully"""
        room_count = self.reservation.modify_room_count(-1)
        self.assertNotIn(f"modified to {3}", room_count)

    def test_calculate_total_cost(self):
        """Sould calculate total cost succesfully"""
        total_cost = self.reservation.calculate_total_cost(100)
        self.assertEqual(total_cost, 200)


if __name__ == "__main__":
    unittest.main()
