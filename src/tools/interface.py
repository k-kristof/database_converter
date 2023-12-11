import wx
from tools import sql

class MyWindow(wx.Frame):

    def __init__(self, parent, title, cursor):
        super(MyWindow, self).__init__(parent, title=title, size=(300,200))
        self.InitUI(cursor)
        self.Centre()
        self.Show()

    def InitUI(self, cursor): 
        panel = wx.Panel(self)
        tables = sql.fetch_tables(cursor)
        rows, columns = len(tables), 2

        gs_outer = wx.GridSizer(2, 1, 50, 5)
        gs = wx.GridSizer(rows, columns, 5, 5)
        checkboxes = []
        for table in tables:
            checkbox = wx.CheckBox(panel)
            gs.Add(checkbox, 0, wx.EXPAND)
            gs.Add(wx.StaticText(panel, label=table), 0, wx.EXPAND)
            checkboxes.append((checkbox, table))
        gs_outer.Add(gs)
        
        button = wx.Button(panel, label="Kijelöltek mentése")
        button.Bind(wx.EVT_BUTTON, lambda event: self.saveTables(checkboxes, cursor))
        gs_outer.Add(button)
 
        panel.SetSizer(gs_outer)
 
    def saveTables(self, checkboxes, cursor):
        for checkbox, table in checkboxes:
            if checkbox.GetValue():
                sql.export_data(cursor, table)