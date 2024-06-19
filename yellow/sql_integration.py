from sqlite3 import Cursor
from typing import Union
from typing import Literal
import pymysql
from pymysql.cursors import DictCursor
from sql_credentials import get_creds

from dataclasses import dataclass
from datetime import date, time


@dataclass
class Customer_Type:
    CustomerID: int
    Name: str
    PhoneNumber: str
    Status: str
    TimesVisited: int
    TimesCanceled: int
    AmountSpent: int


@dataclass
class Table_Type:
    TableID: int
    Capacity: str
    Status: str


@dataclass
class Employee_Type:
    EmployeeID: int
    FirstName: str
    LastName: str
    Gender: str
    Position: str
    Username: str
    Password: str


@dataclass
class Reservation_Type:
    ReservationID: int
    StartTime: time
    EndTime: time
    BookingDate: date
    TableID: int
    CustomerID: int


def make_connection() -> pymysql.Connection:
    conn = pymysql.connect(
        host="localhost", user="root", password=get_creds(), db="cs_survey"
    )
    return conn


tables = Literal["Customers", "Employees", "Reservations", "Tables"]


def get_data(
    table: tables, page, limit=3
) -> Union[Reservation_Type, Employee_Type, Table_Type, Customer_Type]:
    conn = make_connection()
    cur: Cursor = conn.cursor(DictCursor)
    cur.execute(f"select * from {table} limit {limit} offset {3*(page-1)}")
    conn.close()
    return cur.fetchall()
