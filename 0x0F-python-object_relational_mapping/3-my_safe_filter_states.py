#!/usr/bin/python3
"""
script lists all states from the database where name matches
the provided argument (safe from MySQL injection).
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    match = sys.argv[4]
    query = """
        SELECT *
        FROM states
        WHERE name LIKE %s
    """
    cursor.execute(query, ('%' + match + '%',))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
