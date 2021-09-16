import wx
import os
import webbrowser


class Frame(wx.Frame):

    def __init__(self):
        super(Frame, self).__init__(None)

        # ここで Alt+Space のホットキーを登録しています。
        new_id = wx.NewIdRef(count=1)
        self.RegisterHotKey(new_id, wx.MOD_ALT, wx.WXK_SPACE)
        self.Bind(wx.EVT_HOTKEY, self.Foo, id=new_id)

        # ここで Ctrl+Space のホットキーを登録しています。
        new_id = wx.NewIdRef(count=1)
        self.RegisterHotKey(new_id, wx.MOD_CONTROL, wx.WXK_SPACE)
        self.Bind(wx.EVT_HOTKEY, self.Bar, id=new_id)


    def Foo(self, event):
        """新しいファイルをデスクトップに作ります。"""
        filepath = os.path.join(
            os.path.expanduser('~'),
            'Desktop',
            'NewFile.txt',
        )
        with open(filepath, 'w') as f:
            f.write('')


    def Bar(self, event):
        """Qiita を開きます。"""
        webbrowser.open('https://qiita.com/midoriiro')

app = wx.App(False)
Frame()
app.MainLoop()