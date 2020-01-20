# Data Access Objects:
# All of these are meant to be singletons
from DTO import Product, Activity, Coffee_stand


class _Employees:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, employee):
        self._conn.execute("""
        INSERT INTO Employees VALUES (?,?,?,?)""", [employee.id, employee.name, employee.salary, employee.coffee_stand])

    def findall(self):
        c = self._conn.cursor()
        c.execute("""SELECT * FROM Employees ORDER BY id asc""")
        return c.fetchall()


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
        INSERT INTO Suppliers VALUES (?,?,?) """, [supplier.id, supplier.name, supplier.contact_information])

    def findall(self):
        c = self._conn.cursor()
        c.execute("""SELECT * FROM Suppliers ORDER BY id asc""")
        return c.fetchall()


class _Products:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, product):
        self._conn.execute("""
            INSERT INTO Products VALUES (?, ?, ?,?)
        """, [product.id, product.description, product.price, product.quantity])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""SELECT id,description,price,quantity FROM Products WHERE id=(?)""", [id])
        return Product(*c.fetchone())

    def update(self, product, quantity):
        self._conn.execute("""UPDATE Products SET quantity=(?) WHERE id=(?)""", [quantity, product.id])

    def findall(self):
        c = self._conn.cursor()
        c.execute("""SELECT * FROM Products ORDER BY id asc""")
        return c.fetchall()


class _Coffee_stands:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, coffee_stand):
        self._conn.execute("""
                INSERT INTO Coffee_stands VALUES (?, ?, ?)
        """, [coffee_stand.id, coffee_stand.location, coffee_stand.number_of_employees])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,location FROM Coffee_stands WHERE id = ?
            """, [id])

        return Coffee_stand(*c.fetchone())

    def findall(self):
        c = self._conn.cursor()
        c.execute("""SELECT * FROM Coffee_stands ORDER BY id asc""")
        return c.fetchall()


class _Activities:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, activity):
        self._conn.execute("""
                INSERT INTO Activities  VALUES (?,?,?,?)
        """, [activity.product_id, activity.quantity, activity.activator_id, activity.date])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                SELECT product_id,quantity,activator_id,date FROM Activities WHERE activator_id = ?
            """, [id])

        return Activity(*c.fetchone())

    def findall(self):
        c = self._conn.cursor()
        c.execute("""SELECT * FROM Activities ORDER BY date asc""")
        activitieslist = c.fetchall()
        return activitieslist


class _EmployyesReport:
    def __init__(self, con):
        self._con = con

    def findall(self):
        c = self._con.cursor()
        c.execute("""SELECT Employees.name,Employees.salary,Coffee_stands.location,
        SUM(Products.price *(Activities.quantity)*(-1))
        FROM Employees 
        LEFT JOIN Coffee_stands ON Employees.coffee_stand=Coffee_stands.id
        LEFT JOIN Activities ON Employees.id=Activities.activator_id
        LEFT JOIN Products ON Activities.product_id=Products.id
        GROUP BY Employees.name""")

        return c.fetchall()


class _ActivityReport:
    def __init__(self, con):
        self._con = con

    def findall(self):
        c = self._con.cursor()
        c.execute("""SELECT Activities.date,Products.description,Activities.quantity,Employees.name,Suppliers.name
        FROM Activities
        JOIN Products ON Activities.product_id=Products.id 
        LEFT JOIN Employees ON Activities.activator_id=Employees.id
        LEFT JOIN Suppliers ON Activities.activator_id=Suppliers.id 
        ORDER BY Activities.date""")
        return c.fetchall()