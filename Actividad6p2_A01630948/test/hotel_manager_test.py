import unittest
from hotel_manager import HotelManager
from hotel import Hotel
from customer import Customer
from reservation import Reservation


class TestHotelManager(unittest.TestCase):
    def setUp(self):
        self.hotel_manager = HotelManager()
        self.hotel1 = Hotel("1", "Hotel A", 50)
        self.hotel2 = Hotel("2", "Hotel B", 100)

        self.hotel_manager.hotels.append(self.hotel1)
        self.hotel_manager.hotels.append(self.hotel2)

        self.customer = Customer("1", "Alice", "alice@example.com")

    def test_create_hotel(self):
        self.hotel_manager.create_hotel("3", "Hotel C", 75)
        self.assertEqual(len(self.hotel_manager.hotels), 3)

    def test_delete_hotel(self):
        self.assertEqual(
            self.hotel_manager.delete_hotel("1"), "Hotel not found."
        )
        self.assertEqual(len(self.hotel_manager.hotels), 1)
        self.assertEqual(
            self.hotel_manager.delete_hotel("4"), "Hotel not found."
        )

    def test_display_hotel_info(self):
        self.assertEqual(
            self.hotel_manager.display_hotel_info("1"),
            "Hotel ID: 1, Name: Hotel A, Rooms: 50",
        )
        self.assertEqual(
            self.hotel_manager.display_hotel_info("3"), "Hotel not found."
        )

    def test_modify_hotel_info(self):
        self.hotel_manager.modify_hotel_info("1", "Hotel Alpha", 60)

        self.assertEqual(self.hotel1.name, "Hotel Alpha")
        self.assertEqual(self.hotel1.rooms, 60)
        self.assertEqual(
            self.hotel_manager.modify_hotel_info("3", "Hotel C", 75),
            "Hotel not found.",
        )

    def test_reserve_room(self):
        self.assertEqual(
            self.hotel_manager.reserve_room("1", self.customer, 5),
            "Room reserved at Hotel 1 for Customer 1",
        )
        self.assertEqual(self.hotel1.rooms, 45)
        self.assertEqual(
            self.hotel_manager.reserve_room("3", self.customer, 5),
            "Hotel not found.",
        )

        self.assertEqual(
            self.hotel_manager.reserve_room("2", self.customer, 150),
            "Not enough available rooms for reservation.",
        )

    def test_cancel_reservation(self):
        self.assertEqual(
            self.hotel_manager.cancel_reservation("1"),
            "Reservation not found.",
        )

        reservation_id = len(self.hotel_manager.reservations) + 1
        self.hotel_manager.reservations.append(
            Reservation(reservation_id, self.customer, self.hotel1, 2)
        )

        self.assertEqual(
            self.hotel_manager.cancel_reservation(reservation_id),
            f"Reservation {reservation_id} canceled. 2 rooms released.",
        )

        self.assertEqual(
            self.hotel_manager.cancel_reservation("5"),
            "Reservation not found.",
        )


if __name__ == "__main__":
    unittest.main()
