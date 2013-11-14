#! /usr/bin/env python
# coding:utf-8

import wx
from BlockWindow import BlockWindow

labels = "one two three four five six seven eight nine".split()

flags = {'one':wx.BOTTOM, 'two':wx.ALL, 'three':wx.TOP,
        'four':wx.LEFT, 'five':wx.ALL, 'six':wx.RIGHT,
        'seven':wx.BOTTOM|wx.TOP,'eight':wx.ALL, 'nine':wx.LEFT|wx.RIGHT}

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'GridSizer Borders')
        self.sizer = wx.GridSizer(rows = 3,cols = 3,hgap = 5, vgap = 5)
        for label in labels:
            bw = BlockWindow(self, label=label)
            flag = flags.get(label, 0)
            self.sizer.Add(bw, 0, flag, 10)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)

class App(wx.App):
    def OnInit(self):
        self.f = TestFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
