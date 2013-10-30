#! /usr/bin/env python
# coding:utf-8

import wx

class ButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Button Example',size=(300,100))
        self.panel = wx.Panel(self,-1)
        self.button = wx.Button(self.panel,-1,"Hello",pos=(50,20))
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)
        self.button.SetDefault()
        self.b2 = wx.Button(self.panel,-1,"This is a test",pos=(50,50),
            style=wx.BU_RIGHT|wx.BU_EXACTFIT)

    def OnClick(self,event):
        self.button.SetLabel("Clicked")

class App(wx.App):
    def OnInit(self):
        self.frame = ButtonFrame()
        self.frame.Show(True)
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
