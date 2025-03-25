from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def table_exists(table_name):
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=%s;", [table_name])
        return cursor.fetchone() is not None


def get_faculties():
    if table_exists("home_category"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM home_category")
            return dictfetchall(cursor)
    return []


def get_guruh():
    if table_exists("home_product"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM home_product")
            return dictfetchall(cursor)
    return []


def get_subject():
    if table_exists("home_order"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM home_order")
            return dictfetchall(cursor)
    return []


def get_teacher():
    if table_exists("home_user") and table_exists("home_order") and table_exists("home_orderproduct"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("""
                SELECT u.id, u.first_name, u.last_name, u.phone, 
                       COUNT(o.id) AS order_count 
                FROM home_user u
                LEFT JOIN home_order o ON u.id = o.customer_id
                GROUP BY u.id, u.first_name, u.last_name, u.phone
            """)
            return dictfetchall(cursor)
    return []


def get_order_products():

    if table_exists("home_orderproduct"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("""
                SELECT op.id, u.first_name, u.last_name, p.title, op.count, op.price
                FROM home_orderproduct op
                JOIN home_order o ON op.order_id = o.id
                JOIN home_user u ON o.customer_id = u.id
                JOIN home_product p ON op.product_id = p.id
            """)
            return dictfetchall(cursor)
    return []

