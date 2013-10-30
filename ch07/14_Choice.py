#! /usr/bin/env python 
# coding:utf-8

import wx

class ChoiceFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,'Choice Example',size=(250,200))
        self.panel = wx.Panel(self,-1)
        sampleList = ['zero','one','two','three','four','five','six','seven','eight']
        wx.StaticText(self.panel,-1,'Select one:',(15,20))
        self.c = wx.Choice(self.panel,-1,(85,18),choices=sampleList)

class App(wx.App):
    def OnInit(self):
        self.frame = ChoiceFrame()
        self.frame.Show()
        return True

if __name__ == "__main__":
    App().MainLoop()
