from banking_app.backend.customer import CustomerManager


def test_add_customer():
    cm = CustomerManager()
    cust = cm.add_customer("Alice", "alice@mail.com", "99999")
    assert cust.name == "Alice"
    assert cust.email == "alice@mail.com"
    assert cust.phone == "99999"


def test_get_customer():
    cm = CustomerManager()
    c1 = cm.add_customer("Bob", "bob@mail.com", "12345")
    c2 = cm.get_customer(c1.customer_id)
    assert c2.name == "Bob"


def test_list_customers():
    cm = CustomerManager()
    cm.add_customer("Test1", "t1@mail.com", "11111")
    cm.add_customer("Test2", "t2@mail.com", "22222")
    results = cm.list_customers()
    assert len(results) == 2
