from mysql import connector
import csv

def connect(conf):
    db = connector.connect(
        host=conf['host'],
        user=conf['user'],
        password=conf['password'],
        database=conf['database'],
    )
    return db

def fetch_tables(conn):
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES")
    tables_raw = cursor.fetchall()
    cursor.close()
    return [t[0] for t in tables_raw]

def fetch_table_data(cursor, table):
    cursor.execute(f"SELECT * FROM {table}")
    header = [row[0] for row in cursor.description]
    rows = cursor.fetchall()
    return header, rows

def export_table(conn, directory, table):
    cursor = conn.cursor()
    header, rows = fetch_table_data(cursor, table)
    with open(f'{directory}/{table}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        csv_writer.writerows(rows)
    cursor.close()