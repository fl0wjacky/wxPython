#! /usr/bin/env python
# coding:utf-8

import wx

class RadioButtonFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Radio Example',size = (200,200))
        self.panel = wx.Panel(self,-1)

class App(wx.App):
    def OnInit(self):
        self.frame = RadioButtonFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
