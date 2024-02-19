"""
Reservation system for hotels
Reservation Class
Mariana Glz Bravo: A01630948
"""


class Reservation:
    """Class to represent a reservation"""

    def __init__(self, reservation_id, customer, hotel, room_count):
        """Initialize a reservation with given parameters"""
        self.reservation_id = reservation_id
        self.customer = customer
        self.hotel = hotel
        self.room_count = room_count

    def get_reservation_info(self):
        """Get information about the reservation"""
        return (
            f"Reservation ID: {self.reservation_id}, "
            f"Customer: {self.customer}, "
            f"Hotel: {self.hotel}, "
            f"Rooms: {self.room_count}"
        )

    def modify_room_count(self, new_room_count):
        """Modify the room count for the reservation"""
        if new_room_count > 0:
            self.room_count = new_room_count
            return (
                f"Room count for Reservation {self.reservation_id} "
                f"modified to {new_room_count}"
            )
        return "Invalid room count. Please provide a positive number."

    def calculate_total_cost(self, room_rate):
        """Calculate the total cost of the reservation"""
        return self.room_count * room_rate
