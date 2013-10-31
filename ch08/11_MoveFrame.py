#! /usr/bin/env python n
# coding:utf-8

import wx

class ShapedFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(None,-1,'Shaped Window',style = wx.FRAME_SHAPED | wx.SIMPLE_BORDER)
        self.hasShape = False
        self.delta = wx.Point(0,0)
        self.bmp = images.getVippiBitmap()
        self.SetClientSize((self.bmp.GetWidth(),self.bmp.GetHeight()))
        dc = wx.ClientDC(self)
        dc.DrawBitmap(self.bmp,0,0,True)
        self.SetWindowShape()
