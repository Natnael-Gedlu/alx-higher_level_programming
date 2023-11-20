#!/usr/bin/python3
"""
script displays all values in the states table
of hbtn_0e_0_usa where the name matches the provided argument.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = """
        SELECT *
        FROM states
        WHERE name LIKE BINARY '{}'
    """.format(sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
