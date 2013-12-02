#! /usr/bin/env python
# coding:utf-8

import wx
import glob

class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'wx.ListCtrl in wx.LC_SMALL_ICON mode',
            size = (600, 400))
        il = wx.ImageList(16, 16, True)
        for name in glob.glob('smicon??.png'):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(bmp)

        self.list = wx.ListCtrl(self, -1, style = wx.LC_SMALL_ICON | wx.LC_AUTOARRANGE)
        self.list.AssignImageList(il, wx.IMAGE_LIST_SMALL)

        for x in range(25):
            img = x % (il_max + 1)
            self.list.InsertImageStringItem(x, 'This is item %02d' % x, img)

class App(wx.App):
    def OnInit(self):
        self.f = DemoFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
