from tools import interface

def main():
    app = interface.wx.App(False)
    interface.MyWindow(parent=None, title='Database Converter')
    app.MainLoop()

    return 0

if __name__ == "__main__":
    main()