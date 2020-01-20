# The Repository
import atexit
import os
import sqlite3
from DAO import _Employees, _Suppliers, _Products, _Coffee_stands, _Activities, _EmployyesReport, _ActivityReport


class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('moncafe.db')
        self.employee = _Employees(self._conn)
        self.supplier = _Suppliers(self._conn)
        self.product = _Products(self._conn)
        self.coffee_stand = _Coffee_stands(self._conn)
        self.activity = _Activities(self._conn)
        self.employeeReport = _EmployyesReport(self._conn)
        self.activityReport = _ActivityReport(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        cursor = self._conn.cursor()
        cursor.executescript("""
        CREATE TABLE Employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            salary REAL NOT NULL,
            coffee_stand INTEGER REFERENCES Coffee_stands(id)
        );

        CREATE TABLE Suppliers (
            id INTEGER PRIMARY KEY ,
            name TEXT NOT NULL ,
            contact_information TEXT
        );
        CREATE TABLE Products (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        );
        CREATE TABLE Coffee_stands (
            id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            number_of_employees INTEGER
        );
        CREATE TABLE Activities (
            product_id INTEGER REFERENCES Products(id),
            quantity INTEGER NOT NULL,
            activator_id INTEGER NOT NULL,
            date DATE NOT NULl
        );
    """)

    def deleteifExist(self):
        Data_Base_Exist = os.path.isfile('moncafe.db')
        if Data_Base_Exist:
            os.remove('moncafe.db')
            self.__init__()
        # self._conn.cursor().execute("DROP TABLE IF EXISTS Activities")
        # self._conn.cursor().execute("DROP TABLE IF EXISTS Coffee_stands")
        # self._conn.cursor().execute("DROP TABLE IF EXISTS Products")
        # self._conn.cursor().execute("DROP TABLE IF EXISTS Suppliers")
        # self._conn.cursor().execute("DROP TABLE IF EXISTS Employees")


repo = _Repository()
atexit.register(repo._close)
