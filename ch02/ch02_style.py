#! /usr/bin/env python

import wx

if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = wx.Frame(None,title = "Yes", style=wx.DEFAULT_FRAME_STYLE | wx.FRAME_TOOL_WINDOW)
    frame.Show()
    app.MainLoop()
