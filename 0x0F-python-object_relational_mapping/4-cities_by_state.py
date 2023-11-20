#!/usr/bin/python3
"""
Script that lists all states with a name starting with N.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name 
        FROM cities INNER JOIN states ON states.id=cities.state_id
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
