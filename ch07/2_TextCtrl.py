#! /usr/bin/env python

import wx

class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,wx.NewId(),"Text Entry Example",size=(300,100))
        self.panel = wx.Panel(self,wx.NewId())
        self.basicLabel = wx.StaticText(self.panel,wx.NewId(),"Basic Control:")
        self.basicText = wx.TextCtrl(self.panel,wx.NewId(),"I've entered some text!",size = (175,-1))
        self.basicText.SetInsertionPoint(0)

        self.pwdLabel = wx.StaticText(self.panel,wx.NewId(),"Password:",)
        self.pwdText = wx.TextCtrl(self.panel,wx.NewId(),"password",size=(175,-1),style=wx.TE_PASSWORD)
        sizer = wx.FlexGridSizer(cols=2,hgap=6,vgap=6)
        sizer.AddMany([self.basicLabel,self.basicText,self.pwdLabel,self.pwdText])
        self.panel.SetSizer(sizer)

        

class App(wx.App):
    def OnInit(self):
        self.frame = TextFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
