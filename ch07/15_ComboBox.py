#! /usr/bin/env python
# coding:utf-8

import wx

class ComboBoxFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Combo Box Example',size = (350,350))
        self.panel = wx.Panel(self,-1)

        sampleList = ['zero','one','two','three','four','five','six','seven','eight']
        wx.StaticText(self.panel,-1,'Select one:',(15,15))
        self.cb = wx.ComboBox(self.panel,-1,'',(15,30),wx.DefaultSize,sampleList,wx.CB_READONLY)
        #self.cb2 = wx.ComboBox(self.panel,-1,'default value',(200,30),wx.DefaultSize,sampleList,wx.CB_SIMPLE)

class App(wx.App):
    def OnInit(self):
        self.frame = ComboBoxFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
