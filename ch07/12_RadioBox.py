#! /usr/bin/env python
# coding:utf-8

import wx

class RadioBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Radio Box Example',size = (350,200))
        self.panel = wx.Panel(self,-1)

        sampleList = ['zero','one','two','three','four','five','six','seven','eight']
        self.rb1 = wx.RadioBox(self.panel,-1,"A Radio Box",(10,10),wx.DefaultSize,sampleList,2,wx.RA_SPECIFY_COLS)
        self.rb2 = wx.RadioBox(self.panel,-1,"",(150,10),wx.DefaultSize,sampleList,3,wx.RA_SPECIFY_COLS | wx.NO_BORDER)

class App(wx.App):
    def OnInit(self):
        self.frame = RadioBoxFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
