#! /usr/bin/env python
# coding:utf-8
import wx

class SubclassFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Frame Subclass',size=(300,100),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self,-1)
        button = wx.Button(panel,-1,"Close Me",pos=(15,15))
        button.SetDefault()
        self.Bind(wx.EVT_BUTTON,self.OnCloseMe,button)
        self.Bind(wx.EVT_CLOSE,self.OnCloseWindow)

    def OnCloseMe(self,event):
        self.Close(True)

    def OnCloseWindow(self,event):
        self.Destroy()

if __name__ == "__main__":
        app = wx.PySimpleApp()
        SubclassFrame().Show()
        app.MainLoop()
