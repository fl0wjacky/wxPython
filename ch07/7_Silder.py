#! /usr/bin/env python
# coding:utf-8

import wx

class SliderFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Slider Example',size = (300,350))
        self.panel = wx.Panel(self,-1)
        self.count = 0
        self.slider = wx.Slider(self.panel,-1,25,1,100,pos = (10,10),size = (250,-1),style = wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.slider.SetTickFreq(5,1)
        self.s2 = wx.Slider(self.panel,-1,50,1,100,pos=(125,70),size=(25,250),style=wx.SL_VERTICAL | wx.SL_AUTOTICKS | wx.SL_LABELS)
        self.s2.SetTickFreq(20,1)

class App(wx.App):
    def OnInit(self):
        self.frame = SliderFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = App()
    app.MainLoop()
