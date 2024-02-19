"""
Reservation system for hotels
Customer Manager Class
Mariana Glz Bravo: A01630948
"""

from customer import Customer


class CustomerManager:
    """Class to manage customers"""

    def __init__(self):
        """Initialize a CustomerManager"""
        self.customers = []

    def create_customer(self, customer_id, name, email):
        """Create a new customer with the given parameters"""
        customer = Customer(customer_id, name, email)
        self.customers.append(customer)

    def delete_customer(self, customer_id):
        """Delete a customer with the given ID"""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                self.customers.remove(customer)
                return f"Customer {customer_id} deleted."

        return "Customer not found."

    def display_customer_info(self, customer_id):
        """Display information about a customer with the given ID"""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return (
                    f"Customer ID: {customer.customer_id}, "
                    f"Name: {customer.name}, Email: {customer.email}"
                )
        return "Customer not found."

    def modify_customer_info(self, customer_id, new_name, new_email):
        """Modify information about a customer with the given ID"""
        for customer in self.customers:
            if customer.customer_id == customer_id:
                customer.name = new_name
                customer.email = new_email
                return f"Customer information modified: {customer_id}"

        return "Customer not found."
