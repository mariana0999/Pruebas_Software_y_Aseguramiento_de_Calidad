"""
Reservation system for hotels
Reservation Manager Class
Mariana Glz Bravo: A01630948
"""

from reservation import Reservation


class ReservationManager:
    """Class to manage reservations"""

    def __init__(self):
        """Initialize a ReservationManager"""
        self.reservations = []

    def create_reservation(self, reservation_id, customer, hotel, room_count):
        """Create a new reservation"""
        reservation = Reservation(reservation_id, customer, hotel, room_count)
        self.reservations.append(reservation)

    def cancel_reservation(self, reservation_id):
        """Cancel a reservation with the given ID"""
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.hotel.rooms += reservation.room_count
                self.reservations.remove(reservation)
                return (
                    f"Reservation {reservation_id} canceled. "
                    f"{reservation.room_count} rooms released."
                )
        return "Reservation not found."
