"""
Reservation system for hotels
Customer Class
Mariana Glz Bravo: A01630948
"""

from reservation import Reservation


class Customer:
    """Class to represent a customer"""

    def __init__(self, customer_id, name, email):
        """Initialize a customer with given parameters."""
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.reservations = []

    def make_reservation(self, reservation_id, hotel, room_count):
        """Make a reservation for the customer at a hotel"""
        reservation = Reservation(reservation_id, self, hotel, room_count)
        self.reservations.append(reservation)
        return (
            f"Reservation made for Customer {self.customer_id} "
            f"at Hotel {hotel.hotel_id}"
        )

    def cancel_reservation(self, reservation_id):
        """Cancel a reservation made by the customer"""
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                self.reservations.remove(reservation)
                return (
                    f"Reservation {reservation_id} canceled for "
                    f"Customer {self.customer_id}"
                )
        return "Reservation not found."
