import sqlite3
import atexit
from dbtools import Dao


# Data Transfer Objects:
class Employee(object):
    # TODO: implement
    def __init__(self, id, name, salary, branch_id):
        self.id = id
        self.name = name
        self.salary = salary
        self.branch_id = branch_id

    def __str__(self):
        return f'({self.id}, {self.name.decode("utf-8")} , {self.salary}, {self.branch_id})'


class Supplier(object):
    # TODO: implement
    def __init__(self, id, name, contact_information):
        self.id = id
        self.name = name
        self.contact_information = contact_information

    def __str__(self):
        return f"{self.id},{self.name}, {self.contact_information}"


class Product(object):
    # TODO: implement
    def __init__(self, id, description, price, quantity):
        self.id = id
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.id},{self.description}, {self.price}, {self.quantity}"


class Branche(object):
    # TODO: implement
    def __init__(self, id, location, number_of_employees):
        self.id = id
        self.location = location
        self.number_of_employees = number_of_employees

    def __str__(self):
        return f'({self.id}, {self.location.decode()} , {self.number_of_employees})'


class Activitie(object):
    # TODO: implement
    def __init__(self, product_id, quantity, activator_id, date):
        self.product_id = product_id
        self.quantity = quantity
        self.activator_id = activator_id
        self.date = date

    def __str__(self):
        return f"{self.product_id},{self.quantity},{self.activator_id},{self.date}"


# Repository
class Repository(object):
    def __init__(self):
        self._conn = sqlite3.connect('bgumart.db')
        self._conn.text_factory = bytes
        # TODO: complete

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
            CREATE TABLE employees (
                id              INT         PRIMARY KEY,
                name            TEXT        NOT NULL,
                salary          REAL        NOT NULL,
                branche    INT REFERENCES branches(id)
            );
    
            CREATE TABLE suppliers (
                id                   INTEGER    PRIMARY KEY,
                name                 TEXT       NOT NULL,
                contact_information  TEXT
            );

            CREATE TABLE products (
                id          INTEGER PRIMARY KEY,
                description TEXT    NOT NULL,
                price       REAL NOT NULL,
                quantity    INTEGER NOT NULL
            );

            CREATE TABLE branches (
                id                  INTEGER     PRIMARY KEY,
                location            TEXT        NOT NULL,
                number_of_employees INTEGER
            );
    
            CREATE TABLE activities (
                product_id      INTEGER REFERENCES products(id),
                quantity        INTEGER NOT NULL,
                activator_id    INTEGER NOT NULL,
                date            TEXT    NOT NULL
            );
        """)

    def execute_command(self, script: str) -> list:
        return self._conn.cursor().execute(script).fetchall()

    # adds an employee to the database
    def add_employee(self, employee: Employee):
        self._conn.execute("INSERT INTO employees VALUES (?,?,?,?)",
                           (employee.id, employee.name, employee.salary, employee.branch_id))

    # adds a supplier to the database
    def add_supplier(self, supplier: Supplier):
        self._conn.execute("INSERT INTO suppliers VALUES (?,?,?)",
                           (supplier.id, supplier.name, supplier.contact_information))

    # adds a product to the database
    def add_product(self, product: Product):
        self._conn.execute("INSERT INTO products VALUES (?,?,?,?)",
                           (product.id, product.description, product.price, product.quantity))

    # adds a branch to the database
    def add_branch(self, branch: Branche):
        self._conn.execute("INSERT INTO branches VALUES (?,?,?)",
                           (branch.id, branch.location, branch.number_of_employees))

    # adds an activity to the database
    def add_activity(self, product_id, quantity, activator_id, date):
        self._conn.execute("INSERT INTO activities VALUES (?,?,?,?)", (product_id, quantity, activator_id, date))

    # gets the product quantity from the products table
    def get_product_quantity(self, product_id):
        return self._conn.execute("SELECT quantity FROM products WHERE id = ?", (product_id,)).fetchone()[0]

    # updates the products quantity
    def update_product_quantity(self, product_id: int, quantity: int):
        current_quantity = self.get_product_quantity(product_id)
        self._conn.execute("UPDATE products SET quantity = ? WHERE id = ?", (current_quantity + quantity, product_id))

    # gets all the activities from the activities table ordered by their date
    def get_activities(self):
        return self.execute_command("SELECT * FROM activities ORDER BY date")

    # gets all the branches from the branches table ordered by their id
    def get_branches(self):
        return self.execute_command("SELECT * FROM branches ORDER BY id")

    # gets all the employees from the employees table ordered by their id
    def get_employees(self):
        return self.execute_command("SELECT * FROM employees ORDER BY id")

    # gets all the products from the branches table ordered by their id
    def get_products(self):
        return self.execute_command("SELECT * FROM products ORDER BY id")

    # gets all the suppliers from the branches table ordered by their id
    def get_suppliers(self):
        return self.execute_command("SELECT * FROM suppliers ORDER BY id")

    def get_employees_report(self):
        return self.execute_command("""
            SELECT e.name,e.salary,b.location,
            COALESCE(sum(p.price * a.quantity * -1),0)
            FROM employees as e
            JOIN branches as b on e.branche = b.id
            LEFT JOIN activities as a ON a.activator_id = e.id
            LEFT JOIN products as p ON a.product_id = p.id
            GROUP by e.name
        """)

    def get_activity_report(self):
        return self.execute_command("""
            SELECT activities.date,products.description,activities.quantity,employees.name,suppliers.name
            FROM activities
            JOIN products ON activities.product_id = products.id
            LEFT JOIN suppliers ON activities.activator_id = suppliers.id
            LEFT JOIN employees ON employees.id = activities.activator_id
        """)


# singleton
repo = Repository()
atexit.register(repo._close)
