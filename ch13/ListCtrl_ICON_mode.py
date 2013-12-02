#! /usr/bin/env python
# coding:utf-8

import wx
import glob 

class DemoFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'wx.ListCtrl in wx.LC_ICON mode',
            size = (750, 400))

        #load some images into an image list
        il = wx.ImageList(128, 128, True)
        for name in glob.glob('icon??.png'):
            bmp = wx.Bitmap(name, wx.BITMAP_TYPE_PNG)
            il_max = il.Add(bmp)

        self.list = wx.ListCtrl(self, -1, style = wx.LC_ICON | wx.LC_AUTOARRANGE)
        self.list.AssignImageList(il, wx.IMAGE_LIST_NORMAL)
        for x in range(10):
            img = x % (il_max + 1)
            self.list.InsertImageStringItem(x, 'This is item %02d' % x, img)

        
class App(wx.App):
    def OnInit(self):
        self.f = DemoFrame()
        self.f.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
