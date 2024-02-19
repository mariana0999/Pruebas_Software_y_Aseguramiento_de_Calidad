"""
Reservation system for hotels
Hotel Class
Mariana Glz Bravo: A01630948
"""

from reservation import Reservation


class Hotel:
    """Class to represent a hotel"""

    def __init__(self, hotel_id, name, rooms):
        """Initialize a hotel with given parameters"""
        self.hotel_id = hotel_id
        self.name = name
        self.rooms = rooms
        self.reservations = []

    def get_available_rooms(self):
        """Get the number of available rooms in the hotel"""
        return self.rooms - len(self.reservations)

    def make_reservation(self, customer, room_count):
        """Make a reservation in the hotel for a customer"""
        if room_count <= self.get_available_rooms():
            reservation_id = len(self.reservations) + 1
            reservation = Reservation(
                reservation_id, customer, self, room_count
            )
            self.reservations.append(reservation)
            return (
                f"Room reserved at Hotel {self.hotel_id} "
                f"for Customer {customer.customer_id}"
            )
        return "Not enough available rooms for reservation."
