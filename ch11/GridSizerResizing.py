#! /usr/bin/env python
# coding:utf-8

import wx
from BlockWindow import BlockWindow

labels = "one two three four five six seven eight nine".split()

flags = {'one':wx.ALIGN_BOTTOM, 'two':wx.ALIGN_CENTER,
        'four':wx.ALIGN_RIGHT, 'six':wx.EXPAND, 'seven':wx.GROW,
        'eight':wx.SHAPED}

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'GridSizer Resizing')
        self.sizer = wx.GridSizer(rows = 3, cols = 3, hgap = 5, vgap = 5)
        for label in labels:
            bw = BlockWindow(self, label = label)
            flag = flags.get(label, 0)
            self.sizer.Add(bw, 0, flag)
        self.SetSizer(self.sizer)
        self.Fit()

class App(wx.App):
    def OnInit(self):
        self.f = TestFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
