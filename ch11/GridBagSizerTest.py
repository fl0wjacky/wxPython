#! /usr/bin/env python
# coding:utf-8

import wx
from BlockWindow import BlockWindow

labels = 'one two three four five six seven eight nine'.split()

class TestFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'GridBagSizer Test')
        self.sizer = wx.GridBagSizer(hgap = 5, vgap = 5)
        for col in range(3):
            for row in range(3):
                bw = BlockWindow(self, label = labels[row*3 + col])
                self.sizer.Add(bw, pos = (row, col))

        #cross row
        bw = BlockWindow(self, label = 'span 3 rows')
        self.sizer.Add(bw, pos = (0, 3), span = (3, 1), flag = wx.EXPAND)

        #cross col
        bw = BlockWindow(self, label = 'span all columns')
        self.sizer.Add(bw, pos = (3, 0), span = (1, 4), flag = wx.EXPAND)

        #self.sizer.AddGrowableCol(3)
        #self.sizer.AddGrowableRow(3)

        self.SetSizer(self.sizer)
        self.Fit()

class App(wx.App):
    def OnInit(self):
        self.f = TestFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
