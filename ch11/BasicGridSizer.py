#! /usr/bin/env python
# coding:utf-8

import wx
from BlockWindow import BlockWindow

labels = "one two three four five six seven eight nine".split()

class GridSizerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Basic Grid Sizer")
        self.sizer = wx.GridSizer(rows = 3, cols = 3, hgap = 5, vgap = 5)
        for label in labels:
            bw = BlockWindow(self, label = label)
            self.sizer.Prepend(bw, 0, 0)
        self.SetSizer(self.sizer)
        self.Fit()

class App(wx.App):
    def OnInit(self):
        self.f = GridSizerFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
