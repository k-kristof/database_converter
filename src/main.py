from tools import config, sql, interface

def main():
    conf = config.parse('server.conf')
    conn = sql.connect(conf)
    curs = conn.cursor()

    app = interface.wx.App(False)
    interface.MyWindow(parent=None, title='Database Converter', cursor=curs)
    app.MainLoop()

    return 0

if __name__ == "__main__":
    main()