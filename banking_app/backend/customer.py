class Customer:
    _id_counter = 1000  # auto-incrementing customer id

    def __init__(self, name, email, phone):
        Customer._id_counter += 1
        self.customer_id = Customer._id_counter
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer({self.customer_id}) | {self.name} | {self.email} | {self.phone}"


class CustomerManager:
    """Manages all customers using a LIST data structure"""

    def __init__(self):
        self.customers = []  # list to store Customer objects

    def add_customer(self, name, email, phone):
        customer = Customer(name, email, phone)
        self.customers.append(customer)
        return customer

    def get_customer(self, customer_id):
        for c in self.customers:
            if c.customer_id == customer_id:
                return c
        return None

    def list_customers(self):
        return [str(c) for c in self.customers]
