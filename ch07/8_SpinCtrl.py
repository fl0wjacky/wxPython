#! /usr/bin/env python
# coding:utf-8

import wx

class SpinnerFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Spinner Example',size = (100,100))
        self.panel = wx.Panel(self,-1)
        self.sc = wx.SpinCtrl(self.panel,-1,"",(30,20),(80,-1))
        self.sc.SetRange(1,100)
        self.sc.SetValue(5)
        self.Bind(wx.EVT_SPINCTRL,self.OnSpin,self.sc)
        self.Bind(wx.EVT_TEXT,self.OnText,self.sc)

    def OnSpin(self,event):
        print('EVT_SPINCTRL')
    def OnText(self,event):
        print('EVT_TEXT')

class App(wx.App):
    def OnInit(self):
        self.frame = SpinnerFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
