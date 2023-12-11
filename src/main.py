from tools import config, sql

def main():
    conf = config.parse('server.conf')
    conn = sql.connect(conf)
    print(conn.is_connected())

    return 0

if __name__ == "__main__":
    main()