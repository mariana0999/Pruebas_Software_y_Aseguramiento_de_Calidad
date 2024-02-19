"""
Reservation system for hotels
Hotel Manager Class
Mariana Glz Bravo: A01630948
"""

from hotel import Hotel
from reservation import Reservation


class HotelManager:
    """Class to manage hotels"""

    def __init__(self):
        """Initialize a HotelManager"""
        self.hotels = []
        self.customers = []
        self.reservations = []

    def create_hotel(self, hotel_id, name, rooms):
        """Create a new hotel"""
        hotel = Hotel(hotel_id, name, rooms)
        self.hotels.append(hotel)

    def delete_hotel(self, hotel_id):
        """Delete a hotel with the given ID"""
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                self.hotels.remove(hotel)
                break
        return "Hotel not found."

    def display_hotel_info(self, hotel_id):
        """Display information about a hotel with the given ID"""
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                return (
                    f"Hotel ID: {hotel.hotel_id}, "
                    f"Name: {hotel.name}, Rooms: {hotel.rooms}"
                )
        return "Hotel not found."

    def modify_hotel_info(self, hotel_id, new_name, new_rooms):
        """Modify information about a hotel with the given ID"""
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                hotel.name = new_name
                hotel.rooms = new_rooms
                return f"Hotel information modified: {hotel_id}"

        return "Hotel not found."

    def reserve_room(self, hotel_id, customer, room_count):
        """Reserve a room in a hotel for a customer"""
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                if room_count <= hotel.rooms:
                    reservation_id = len(self.reservations) + 1
                    reservation = Reservation(
                        reservation_id, customer, hotel, room_count
                    )
                    self.reservations.append(reservation)
                    hotel.rooms -= room_count
                    return (
                        f"Room reserved at Hotel {hotel_id} "
                        f"for Customer {customer.customer_id}"
                    )
                return "Not enough available rooms for reservation."

        return "Hotel not found."
