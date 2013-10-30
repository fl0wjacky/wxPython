#! /usr/bin/env python
# coding:utf-8

import wx

class BitmapButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Bitmap Example',size=(400,250))
        self.panel = wx.Panel(self,wx.NewId())
        
        bmp = wx.Image("car.png",wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        bmp3 = wx.Image("car3.png",wx.BITMAP_TYPE_PNG).ConvertToBitmap()
       
        self.button = wx.BitmapButton(self.panel,-1,bmp,pos=(10,20),
            style=wx.BU_AUTODRAW)
        self.button.SetBitmapSelected(bmp3)

        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        self.button.SetDefault()
        bmp2x = wx.Image("car2.png",wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.b2 = wx.BitmapButton(self.panel,-1,bmp2x,pos=(150,20),style=0)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.b2)

    def OnClick(self,event):
        pass

class App(wx.App):
    def OnInit(self):
        self.frame = BitmapButtonFrame()
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
