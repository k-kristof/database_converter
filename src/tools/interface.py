import wx
from tools import config, sql
 
class Model:
    def __init__(self):
        self._conn = None
 
    def connect_to_db_from_file(self, path):
        cfg = config.parse(path)
        conn = sql.connect(cfg)
        self._conn = conn
 
    def get_tables(self):
        return sql.fetch_tables(self._conn)
 
    def export_table(self, directory, table):
        sql.export_table(self._conn, directory, table)
 
class MyWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MyWindow, self).__init__(parent, title=title, size=(300,200))
 
        self.model = Model()
        self.init_gui()
        self.Centre()
        self.Show()
 
    def init_gui(self):
        panel = wx.Panel(self)
 
        # gombokat tartalmazó grid
        button_grid = wx.GridSizer(rows=3, cols=1, gap=(0, 10))
 
        # konfigfájl tallózó gomb
        file_dlg_button = wx.Button(panel, label="Tallózás")
        file_dlg_button.Bind(wx.EVT_BUTTON, self.on_file_open)
        button_grid.Add(file_dlg_button, 0, wx.EXPAND | wx.ALL, 5)
 
        # tábla listát frissítő gomb
        refresh_button = wx.Button(panel, label="Frissítés")
        refresh_button.Bind(wx.EVT_BUTTON, self.on_refresh_button_click)
        self.refresh_button = refresh_button
        refresh_button.Disable()
        button_grid.Add(refresh_button, 0, wx.EXPAND | wx.ALL, 5)
 
        # kiválasztott táblákat mentő gomb
        save_button = wx.Button(panel, label="Mentés")
        save_button.Bind(wx.EVT_BUTTON, self.on_save_button_click)
        self.save_button = save_button
        save_button.Disable()
        button_grid.Add(save_button, 0, wx.EXPAND | wx.ALL, 5)
 
        # táblákat tartalmazó checkbox lista
        checklistbox = wx.CheckListBox(panel, choices=[])
        self.clb = checklistbox
 
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(button_grid, 0, wx.EXPAND | wx.ALL, 5)
        main_sizer.Add(checklistbox, 1, wx.EXPAND | wx.ALL, 5)
 
        panel.SetSizer(main_sizer)

    def on_file_open(self, event):
        dialog = wx.FileDialog(
            self, message="Konfigurációs fájl tallózása",
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
            )
        if dialog.ShowModal() == wx.ID_OK:
            try:
                self.model.connect_to_db_from_file(dialog.GetPath())
            except Exception as e:
                wx.MessageBox(str(e), "Hiba", wx.OK | wx.ICON_WARNING)
            else:
                self.update_clb()
                self.enable_buttons()
        dialog.Destroy()

    def on_save_button_click(self, event):
        selected_items = self.get_selected_items()
        if selected_items:
            suggested_names = ' '.join([f'"{table}.csv"' for table in selected_items])
            dialog = wx.FileDialog(
                self, message="Kijelölt táblák mentése",
                style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT
            )
            dialog.SetFilename(suggested_names)
 
            if dialog.ShowModal() == wx.ID_OK:
                directory = dialog.GetDirectory()
                for table in selected_items:
                    self.model.export_table(directory, table)
                wx.MessageBox("Táblák sikeresen elmentve.", "Siker", wx.OK | wx.ICON_INFORMATION)
            dialog.Destroy()
        else:
            wx.MessageBox("Nincsen kijelölt tábla.", "Hiba", wx.OK | wx.ICON_WARNING)

    def get_selected_items(self):
        items = []
        for item in range(self.clb.GetCount()):
            if self.clb.IsChecked(item):
                items.append(self.clb.GetString(item))
        return items

    def on_refresh_button_click(self, event):
        self.clb.Clear()
        self.clb.InsertItems(self.model.get_tables(), 0)
    
    def update_clb(self):
        self.clb.Clear()
        self.clb.InsertItems(self.model.get_tables(), 0)

    def enable_buttons(self):
        self.refresh_button.Enable()
        self.save_button.Enable()
