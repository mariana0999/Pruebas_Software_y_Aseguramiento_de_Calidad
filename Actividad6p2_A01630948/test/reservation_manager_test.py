import unittest
from reservation_manager import ReservationManager
from reservation import Reservation
from customer import Customer
from hotel import Hotel


class TestReservationManager(unittest.TestCase):
    def setUp(self):
        self.reservation_manager = ReservationManager()
        self.customer = Customer("1", "Alice", "alice@example.com")
        self.hotel = Hotel("123", "Hotel A", 50)

        self.reservation1 = Reservation("1", self.customer, self.hotel, 2)
        self.reservation2 = Reservation("2", self.customer, self.hotel, 3)

        self.reservation_manager.reservations.append(self.reservation1)
        self.reservation_manager.reservations.append(self.reservation2)

    def test_create_reservation(self):
        self.reservation_manager.create_reservation(
            "3", self.customer, self.hotel, 1
        )
        self.assertEqual(len(self.reservation_manager.reservations), 3)

    def test_cancel_reservation(self):
        self.assertEqual(
            self.reservation_manager.cancel_reservation("1"),
            "Reservation 1 canceled. 2 rooms released.",
        )
        self.assertEqual(len(self.reservation_manager.reservations), 1)

        self.assertEqual(self.hotel.rooms, 52)

        self.assertEqual(
            self.reservation_manager.cancel_reservation("4"),
            "Reservation not found.",
        )


if __name__ == "__main__":
    unittest.main()
