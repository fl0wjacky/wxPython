#! /usr/bin/env python
# coding:utf-8

import wx, glob
columns = [['additions to RTTD','wxTextCtrl-disable auto-scrolling','Less flicker when resizing a window'],['2004-07-08','2003-11-20','2003-11-20']]
rows = []
class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'wx.ListCtrl in wx.LC_REPORT mode',   size = (600, 400))
        il = wx.ImageList(16, 16, True)
        for name in glob.glob('smicon??.png'):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(bmp)

        self.list = wx.ListCtrl(self, -1, style = wx.LC_REPORT)
        self.list.AssignImageList(il, wx.IMAGE_LIST_SMALL)

        for col, text in enumerate(data.columns):
            self.list.InsertColumn(col, text)
