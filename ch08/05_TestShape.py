#! /usr/bin/env python 
# coding:utf-8
import wx
class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Shaped Frame')
        self.panel = wx.Panel(self,-1)
        self.button = wx.Button(self.panel,-1,'Shape Me')
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)

    def OnClick(self,evt):
        bmp = wx.Image('vippi.png').ConvertToBitmap()
        r = wx.RegionFromBitmap(bmp)
        self.SetShape(r)

if __name__ == "__main__":
    app = wx.PySimpleApp()
    Frame().Show()
    app.MainLoop()
