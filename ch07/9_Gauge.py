#! /usr/bin/env python
# coding:utf-8

import wx

class GaugeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Gauge Example',size=(350,150))
        self.panel = wx.Panel(self,-1)
        self.count = 0
        self.gauge = wx.Gauge(self.panel,-1,50,(20,50),(250,25),style=wx.GA_HORIZONTAL|wx.GA_PROGRESSBAR)
        self.gauge.SetBezelFace(3)
        self.gauge.SetShadowWidth(3)
        self.Bind(wx.EVT_IDLE,self.OnIdle)

    def OnIdle(self,event):
        self.count = self.count + 1
        print(self.count)
        if self.count >=50:
            self.count = 0
        self.gauge.SetValue(self.count)

class App(wx.App):
    def OnInit(self):
        self.frame = GaugeFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
