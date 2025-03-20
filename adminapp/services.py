from django.db import connection
from contextlib import closing


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def table_exists(table_name):
    """ Jadval bazada mavjudligini tekshiradi """
    with closing(connection.cursor()) as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=%s;", [table_name])
        return cursor.fetchone() is not None


def get_faculties():
    if table_exists("adminapp_faculty"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_faculty")
            return dictfetchall(cursor)
    return []




def get_guruh():
    if table_exists("adminapp_guruh"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_guruh")
            return dictfetchall(cursor)
    return []


def get_subject():
    if table_exists("adminapp_subject"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM adminapp_subject")
            return dictfetchall(cursor)
    return []


def get_teacher():
    if table_exists("adminapp_teacher") and table_exists("adminapp_subject") and table_exists("adminapp_teacher_subjects"):
        with closing(connection.cursor()) as cursor:
            cursor.execute("""
                SELECT t.id, t.first_name, t.last_name, GROUP_CONCAT(s.name) as subjects
                FROM adminapp_teacher t
                LEFT JOIN adminapp_teacher_subjects ts ON t.id = ts.teacher_id
                LEFT JOIN adminapp_subject s ON ts.subject_id = s.id
                GROUP BY t.id, t.first_name, t.last_name
            """)
            return dictfetchall(cursor)
    return []

