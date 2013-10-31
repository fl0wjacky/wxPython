#! /usr/bin/env python 
# coding:utf-8

'''wx.TINY_CAPTION_VERT dosn't work,why?'''

import wx

class MiniFrame(wx.MiniFrame):
    def __init__(self):
        wx.MiniFrame.__init__(self,None,-1,'Mini Frame',pos=(10,30),size=(300,100))
        self.panel = wx.Panel(self,-1,size=(300,100))
        self.button = wx.Button(self.panel,-1,'Close Me',pos=(15,15))
        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,self.button)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)

    def OnCloseMe(self,evt):
        self.Close(True)

    def OnCloseWindow(self,evt):
        self.Destroy()

class App(wx.App):
    def OnInit(self):
        self.frame = MiniFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
