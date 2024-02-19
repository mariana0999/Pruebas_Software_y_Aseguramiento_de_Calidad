import unittest
from customer_manager import CustomerManager
from customer import Customer


class TestCustomerManager(unittest.TestCase):
    def setUp(self):
        self.customer_manager = CustomerManager()
        self.customer1 = Customer("1", "Alice", "alice@example.com")
        self.customer2 = Customer("2", "Bob", "bob@example.com")
        self.customer3 = Customer("3", "Charlie", "charlie@example.com")

        self.customer_manager.customers.append(self.customer1)
        self.customer_manager.customers.append(self.customer2)

    def test_create_customer(self):
        self.customer_manager.create_customer(
            "4", "David", "david@example.com"
        )
        self.assertEqual(len(self.customer_manager.customers), 3)

    def test_delete_customer(self):
        self.customer_manager.delete_customer("1")
        self.assertEqual(len(self.customer_manager.customers), 1)
        self.assertNotIn(self.customer1, self.customer_manager.customers)

        self.assertEqual(
            self.customer_manager.delete_customer("2"), "Customer 2 deleted."
        )

        self.assertEqual(
            self.customer_manager.delete_customer("4"), "Customer not found."
        )

    def test_display_customer_info(self):
        self.assertEqual(
            self.customer_manager.display_customer_info("1"),
            "Customer ID: 1, Name: Alice, Email: alice@example.com",
        )
        self.assertEqual(
            self.customer_manager.display_customer_info("4"),
            "Customer not found.",
        )

    def test_modify_customer_info(self):
        self.customer_manager.modify_customer_info(
            "1", "Alice Smith", "alice@example.com"
        )
        self.assertEqual(self.customer1.name, "Alice Smith")
        self.assertEqual(
            self.customer_manager.modify_customer_info(
                "1", "Alice", "alice@example.com"
            ),
            "Customer information modified: 1",
        )

        self.assertEqual(
            self.customer_manager.modify_customer_info(
                "4", "David", "david@example.com"
            ),
            "Customer not found.",
        )


if __name__ == "__main__":
    unittest.main()
