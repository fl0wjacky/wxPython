#! /usr/bin/env python

import wx

class MyNewFrame(wx.Frame):
    pass

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyNewFrame(None)
    frame.Show(True)
    app.MainLoop()
